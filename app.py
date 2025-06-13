from flask import Flask, render_template, request
from func import insert, get_avg, get_trend, classify


app = Flask("cafeteria-status")
ver = "v0.3.0"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        insert(request.remote_addr, int(request.form.get("state")))
    return render_template(
        "layout.html", ver=ver, avg=classify(get_avg(10)), trend=get_trend()
    )


def start_server(port):
    app.run(host="0.0.0.0", debug=False, port=port)


port = 5004
if __name__ == "__main__":
    start_server(port=port)
