from flask import Flask, render_template, request
from func import insert, get_avg_recent, get_trend, classify, predict_congestion


app = Flask("cafeteria-status")
ver = "v0.5.0"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        insert(request.remote_addr, int(request.form.get("state")))
    return render_template(
        "layout.html",
        ver=ver,
        avg=classify(get_avg_recent(10, 0)),
        trend=get_trend(10),
        hysteresis=predict_congestion(),
    )


def start_server(port):
    app.run(host="0.0.0.0", debug=True, port=port)


port = 5004
if __name__ == "__main__":
    start_server(port=port)
