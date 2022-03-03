# 予備実験手順方法
## データの抽出と前処理
\url{https://github.com/nallab/k208581_final/blob/main/src/Preliminary_experiment/access_DB.py}
のソースコードにてSPARQLWrapper ライブラリを利用した、
SPARQL抽出クエリを実行することで、都道府県データを抽出した。

その後、
\url{https://github.com/nallab/k208581_final/blob/main/src/Preliminary_experiment/embedding_rel.ipynb}
にて、意味リンクの要素から画像などの利用しない情報や、
サブカテゴリ情報を省くことで、Word2vecに利用可能な情報への前処理を実施した。

\subsection{単語の分散表現}
参考文献\cite{word2vec}の
\url{https://github.com/shiroyagicorp/japanese-word2vec-model-builder}
より、事前学習済みWord2vecモデルをダウンロードすることで、
\url{https://github.com/nallab/k208581_final/blob/main/src/Preliminary_experiment/embedding_rel.ipynb}
における単語の分散表現の獲得を実施する。

\subsection{階層型クラスタリング}
獲得した単語の分散表現を用いて、
\url{https://github.com/nallab/k208581_final/blob/main/src/Preliminary_experiment/clustering.ipynb}
より、階層型クラスタリングの結果を獲得することができる。
