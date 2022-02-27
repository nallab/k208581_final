from SPARQLWrapper import SPARQLWrapper
from util import json_util, csv_util
import time

# DBpedia Japanese からデータを取得するコード
def get_dbpedia_data(data_name):
    sparql = SPARQLWrapper(
        endpoint='http://ja.dbpedia.org/sparql',returnFormat='json')
    sparql.setQuery("""                                                                                                                                                                      
    select distinct ?pred ?obj where {
        <http://ja.dbpedia.org/resource/%s> ?pred ?obj.
    }
    """%data_name)
    result = sparql.query()
    result = result.convert()
    return result


if __name__ == "__main__":
    load_path = "prefecture.csv"
    prefecture_list = csv_util.get_data_csv(load_path)
    for prefecture in prefecture_list:
        try:
            save_path = "data/" + prefecture + ".csv"
            result = get_dbpedia_data(prefecture)
            time.sleep(10)
            row_values = [json_util.get_start(value) for value in result.values()][1]
            value = json_util.get_value(prefecture, row_values)
            csv_util.write_value(save_path, value)
        except:
            print(prefecture + "の動作中でエラーが発生しました")
        finally:
            print(prefecture + "は, データ収集が完了しました")