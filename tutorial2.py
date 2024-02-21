from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)


@app.route("/<name>")
def home(name):
    return render_template("index.html",content=["tim","Khanh"])


# @app.route("/<name>")
# def user(name):
#     return f"Hello! {name}"

# #redirect to specific URL: dễ nhất là nhập tên tham số của trang web 
# #mà bạn cần trỏ đến 
# @app.route("/admin")
# def admin():
#     return redirect(url_for("user", name="Admin!"))

if __name__ =="__main__":
    app.run(debug = True)