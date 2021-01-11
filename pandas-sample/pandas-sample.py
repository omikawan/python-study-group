"""
◆pandasを利用したexcelシートの抽出スクリプト
・概要
pandasを利用し、以下のようなexcelシートのデータを抽出する。
|ID|名前|
|1|田中|
|2|鈴木|
jsonライブラリを利用し、抽出したデータをjson形式に変換する。
{{'ID':'1','名前':'田中'}, {'ID':'2', '名前':'鈴木'}}
"""
import pandas as pd

df = pd.read_excel("sample-list.xlsx",header=2)
print(df.to_json(orient='records', lines=True, force_ascii=False))