"""
◆Flaskを利用したweb画面
・概要
Flaskを利用したweb画面を作成してください。
ページは以下の二つを用意してください。
index.html テキスト入力フォームと「送信」ボタンが存在し、ボタンを押すと「next.html」の画面に遷移する。
next.html 「index.html」の画面で入力したテキストを表示する画面。「戻る」ボタンが存在し、押下すると「index.html」の画面に遷移する。
"""

from flask import Flask, render_template, request

app = Flask(__name__)


# 「/」へアクセスがあった場合の動作
@app.route("/", methods = ["POST"])
def menu():
    return render_template("index.html")

# 「/next」へアクセスがあった場合の動作
@app.route('/next', methods = ["POST"])
def next():
    text = request.form["text"]
    return render_template("next.html", message="「{}」と入力されました。".format(text))

if __name__ == '__main__':
    app.run()