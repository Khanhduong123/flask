from flask import Flask, redirect, url_for, render_template, request,session
from datetime import timedelta
"""
Get: là 1 cách thông thường để gửi và nhận thông tin đến 1 trang web
POST: là 1 cách thực hiện việc này 1 cách an toàn, vì vậy về cơ bản,
get là 1 cách không an toàn để lấy thông tin vì thông tin có thể lưu
trên hệ thống dữ liệu. Còn post là sẽ gửi thông tin an toàn được mã hóa mà bạn
không biết đc từ cả 2 đầu và không lưu trên máy chủ.

Permanent session: phiên cố định, lưu thông tin người dùng trong 1 khoảng
thời gian nhất định, để nhanh chóng đăng nhập mà không cần đăng nhập lại

"""
app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime =timedelta(minutes=1)
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent = True # không được đặt false here vì nó sẽ tồn tại trong browser
        user= request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")



@app.route("/user")
def user():
    # check the information in session
    if "user" in session:
        user = session["user"] #dictionary
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)