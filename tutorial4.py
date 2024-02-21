from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)
"""
Get: là 1 cách thông thường để gửi và nhận thông tin đến 1 trang web
POST: là 1 cách thực hiện việc này 1 cách an toàn, vì vậy về cơ bản,
get là 1 cách không an toàn để lấy thông tin vì thông tin có thể lưu
trên hệ thống dữ liệu. Còn post là sẽ gửi thông tin an toàn được mã hóa mà bạn
không biết đc từ cả 2 đầu và không lưu trên máy chủ.
"""


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        user= request.form["nm"]
        return redirect(url_for("user",usr=user))
    else:
        return render_template("login.html")



@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run(debug=True)