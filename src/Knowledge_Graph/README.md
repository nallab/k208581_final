# 本実験手順方法
## データの抽出と前処理
ターミナルにて以下のコマンドを実行することで、本実験で利用したデータを抽出することが出来る。
```
query=$(curl -H "Accept:text/sparql" https://databus.dbpedia.org/hiroki_u/collections/dbpedia_ja-202105)
files=$(curl -H "Accept: text/csv" --data-urlencode "query=${query}" https://databus.dbpedia.org/repo/sparql | tail -n+2 | sed 's/"//g')
while IFS= read -r file ; do wget $file; done <<< "$files"
```

その後、[temp_preprocessing.py](https://github.com/nallab/k208581_final/blob/main/src/Knowledge_Graph/temp_preprocessing.py)
にて、意味リンクの要素から画像などの利用しない情報や、
サブカテゴリ情報を省くなどの、
予備実験と同じ前処理を実施している。

前処理済みデータは、ファイル名がadd\_cons\_drop\_dup.txtのテキストファイル形式で保存される。
add\_cons\_drop\_dup.txtをベースに、
- 訓練データとして扱いたいデータを**add\_cons\_drop\_dup-train.txt**
- テストデータとして扱いたいデータを**add\_cons\_drop\_dup-test.txt**
- 検証データとして扱いたいデータを**add\_cons\_drop\_dup-valid.txt**

と準備することで、ナレッジグラフの分散表現で利用するデータの準備が完了する。

## ナレッジグラフの分散表現
ナレッジグラフの分散表現を実施する環境として、
[Dockerfile](https://github.com/nallab/k208581_final/blob/main/src/Knowledge_Graph/Dockerfile)
を準備した。
このDockerfileでは、TransEアルゴリズムを用いたナレッジグラフ分散表現を獲得するためのライブラリである
[Pykg2vec](https://github.com/Sujit-O/pykg2vec)
のセットアップ準備も実施している。

セットアップ準備の終了後、
\url{https://github.com/nallab/k208581_final/blob/main/src/Knowledge_Graph/Hyperparameters/TransE.yaml}
のように、ナレッジグラフ分散表現で利用したいハイパーパラメータの記述ファイルを用意する。

最後に、\ref{transe}を実行することでナレッジグラフの分散表現を獲得することができる。
\begin{lstlisting}[caption=TransEの実行, label=transe]
pykg2vec-train -exp True -mn TransE -ds add_cons_drop_dup -dsp {data_dir_path} -hpf {hyperparameter_file} -device cuda
\end{lstlisting}

獲得したナレッジグラフの分散表現は、
全データの分散表現のため、
単語の分散表現と比較するためのデータ範囲などの抽出を
\url{https://github.com/nallab/k208581_final/blob/main/src/Knowledge_Graph/embedding_rel.ipynb}
にて実施している。

## 階層型クラスタリング
獲得したナレッジグラフの分散表現を用いて、
\url{https://github.com/nallab/k208581_final/blob/main/src/Knowledge_Graph/clustering.ipynb}
より、階層型クラスタリングの結果を獲得することができる。
