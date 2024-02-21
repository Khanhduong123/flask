"""
Welcome to Flask backend
"""
from flask import Flask, redirect, url_for


app = Flask(__name__)

#app.route: Dùng để chuyển hướng trang web của mình sang 1 miền khác

#Dùng để trỏ để domain của trang web của mình
@app.route("/") 
def home():
    return "Hello! This is a main page <h1>HELLO<h1>"


#<string>: Nhập bất cứ 1 chuỗi gì đó vào tên của URL
@app.route("/<name>") 
def user(name):
    return f"Hello {name}!"


@app.route("/admin")
def admin():
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run()
