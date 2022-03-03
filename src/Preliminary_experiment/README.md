# 予備実験手順方法
## データの抽出と前処理
access_DB.py では、SPARQLWrapper ライブラリを利用したSPARQL抽出クエリを実行することで、都道府県データを抽出した。

その後、embedding_rel.ipynbにて、意味リンクの要素から画像などの利用しない情報や、
サブカテゴリ情報を省くことで、Word2vecに利用可能な情報への前処理を実施した。

## 単語の分散表現
https://github.com/shiroyagicorp/japanese-word2vec-model-builder
より、事前学習済みWord2vecモデルをダウンロードすることで、
embedding_rel.ipynbにおける単語の分散表現の獲得を実施する。

## 階層型クラスタリング
獲得した単語の分散表現を用いて、clustering.ipynbより、
階層型クラスタリングの結果を獲得することができる。
