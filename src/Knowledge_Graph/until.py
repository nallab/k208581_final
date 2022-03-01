# ファイルの先頭に無駄なデータがないか確認する.
import pandas as pd
import dask.dataframe as dd

def readcsv_map(fileslist):
	df = dd.read_csv(fileslist, sep=' ', header=None, skiprows = 1, 
			escapechar='\\', usecols=[0,1,2], names=('key', 'pred', 'obj'),
			dtype={'key':str, 'pred':str, 'obj':str})
	return df

def preprocessing(obj):
    output = obj.replace('http://ja.dbpedia.org/resource/','')
    return output

def obj_preprocessing(series):
    # 記号等の削除
    drop_symbol = str.maketrans('','','、+[「『]|[」』]※[()][（）]')
    series_dp_symbol = series.map(lambda x: x.translate(drop_symbol))
    
    # @jaの削除
    obj_series = series_dp_symbol.map(lambda x: x.replace('@ja',''))

    # XML表記の削除
    pattern = r'[\^].+http:.+'
    obj_series_xml = obj_series.replace(pattern, '', regex=True)

    # リンクの削除
    pattern = r'http:.+'
    obj_series_link = obj_series_xml.replace(pattern, '', regex=True)

    pattern = r'[\^].'
    output = obj_series_link.replace(pattern, '', regex=True)
    return output

def add_constraints(df):
    # predの要素で, propertyが含まれる値を返す
    out_df = df[df['pred'].str.contains('property')]
    
    # 'wikiPage'を含まないprepertyを返す
    out_df = out_df[~out_df['pred'].str.contains('wikiPage')]
    
    # '画像'を含まないprepertyを返す
    out_df = out_df[~out_df['pred'].str.contains('画像')]
    return out_df

def obj_split(obj):
    if type(obj) != str:
        output = obj
    elif len(obj.split("：")) != 1:
        output = obj.split("：")[1]
    elif len(obj.split(":")) != 1:
        output = obj.split(":")[1]
    else:
        output = obj
    return output.strip()  

def obj_split_2(obj):
    if type(obj) != str:
        output = obj
    elif len(obj.split("_")) != 1:
        output = obj.split("_")[0]
    elif len(obj.split("、")) != 1:
        output = obj.split("、")[0]
    elif len(obj.split(" ")) != 1:
        output = obj.split(" ")[0]
    elif len(obj.split("、")) != 1:
        output = obj.split("、")[0]
    elif len(obj.split("・")) != 1:
        output = obj.split("・")[0]
    elif len(obj.split("・")) != 1:
        output = obj.split("・")[0]
    else:
        output = obj
    return output.strip()
