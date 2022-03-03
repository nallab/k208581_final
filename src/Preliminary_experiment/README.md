# 予備実験手順方法
## データの抽出と前処理
[src/Preliminary_experiment/access_DB.py](access_DB.py) では、SPARQLWrapper ライブラリを利用したSPARQL抽出クエリが記述されている。
今回は都道府県データの抽出を行うため、[src/Preliminary_experiment/prefecture.csv](prefecture.csv) に都道府県名を準備し、
その都道府県名をSPARQL抽出クエリの入力値としてデータ抽出の制御を行なっている。

[src/Preliminary_experiment/access_DB.py](access_DB.py)の実行後、
[src/Preliminary_experiment/embedding_rel.ipynb](embedding_rel.ipynb)にて、
意味リンクの要素から画像などの利用しない情報や、サブカテゴリ情報を省くなどのWord2vecに対応する形式への前処理を実施している。

## 単語の分散表現
https://github.com/shiroyagicorp/japanese-word2vec-model-builder
より、学習済みWord2vecモデルをダウンロードすることで、
[src/Preliminary_experiment/embedding_rel.ipynb](embedding_rel.ipynb)における、
単語の分散表現を実行することが出来る。

## 階層型クラスタリング
獲得した単語の分散表現を用いて、
[src/Preliminary_experiment/clustering.ipynb](clustering.ipynb)
で階層型クラスタリングの結果を獲得することができる。
