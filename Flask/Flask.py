
from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "hello"

# 通过路由指定请求方式
@app.route("/post_only", methods = ["POST"])
def post_only():
    return "post_only"

# 两个路径访问一个页面
@app.route("/hello")
@app.route("/hello2")
def doubleUrl():
    return "doubleUrl all can go to this page"

# 重定向  利用url_for进行反转，寻找视图所对应的路由路径
@app.route("/login")
def redirectToHome():
    url = url_for("index")
    return redirect(url)


# 打印全部路由
print(app.url_map)

app.run(host="127.0.0.1",port = 5000 ,debug=True)

