import pandas as pd
import glob
import os
import time
from until import *
import sys
import numpy as np

# データの読み込み
print("データの読み込み")
file_path = "/home/student/k20/k208581/file_dir/data/"
d_files = glob.glob(os.path.join(file_path, "*.ttl"))
df = readcsv_map(d_files)
print("データの読み込みが完了")

# ダスク読み込みのため, 複数のパーティションに分割される
print('生成されたパーティションの数：' + str(df.npartitions))

# データの前処理
print("データの前処理")
# データのcolumns名の設定
main_df = df.rename(columns={0: 'key', 1: 'pred', 2:'obj'})

# predの要素で, propertyが含まれる値, 'wikiPage'を含まない, '画像'を含まない値の抽出
df_1 = add_constraints(main_df)

# <>の削除
drop_table = str.maketrans('','','<>')
df_1 = df_1.applymap(lambda x: x.translate(drop_table))

# リンク部分の削除
df_2 = df_1.applymap(lambda x: preprocessing(x))
df_2['prepro_obj'] = obj_preprocessing(df_2['obj'])

# 数値のみ要素の削除
df_3 = df_2[df_2['prepro_obj'].apply(lambda x: pd.to_numeric(x, errors='coerce')).isnull()]

# 区切り文字の処理
df_3['new_obj'] = df_3['prepro_obj'].map(lambda x: obj_split(x))
df_3['re_obj'] = df_3['new_obj'].map(lambda x: obj_split_2(x))

print("データの前処理が完了")

print("データの保存")
output_df = df_3.loc[:,['key','pred','re_obj']]
output_df = output_df.applymap(lambda x: x.strip())
output_df = output_df.apply(lambda x: x.replace('', np.nan), axis=1)
output_df = output_df.dropna()
output_df = output_df.drop_duplicates()
output_df.compute().to_csv('add_cons_drop_dup.txt', sep='\t', index=False, header=False)
print("全データの保存が完了")
