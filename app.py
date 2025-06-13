from flask import Flask, render_template, request
from func import insert, get_avg


app = Flask("cafeteria-status")
ver = "v0.2.1"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        insert(request.remote_addr, int(request.form.get("state")))
    return render_template("layout.html", ver=ver, avg=get_avg(10))


def start_server():
    app.run(host="0.0.0.0", port=5050, debug=True)


if __name__ == "__main__":
    start_server()
