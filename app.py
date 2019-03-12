import random


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<html>Hi, Hachimantai!</html>"


@app.route("/hachimantai")
def hello_hachimantai():
    return "<html>スパルタキャンプ in 八幡平</html>"


@app.route("/goodbye")
def goodbye():
    return "<html>Good Bye!</html>"


@app.route("/omikuji")
def omikuji():
    fortune_list = ["大吉", "中吉", "小吉", "凶", "大凶"]
    fortune = random.choice(fortune_list)

    return f"今日の運勢は...{fortune}です！"


if __name__ == '__main__':
    app.run(debug=True)

"""
課題

http://127.0.0.1:5000/goodbye というURLを入力したら､｢Good Bye!｣と表示する
"""
