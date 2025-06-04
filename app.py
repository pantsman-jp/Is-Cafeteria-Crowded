from flask import Flask, render_template, request
from func import write_csv


app = Flask("cafeteria-status")
ver = "v0.1.0"
debug = True


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        write_csv(request.remote_addr, request.form.get("state"))
    return render_template("layout.html", ver=ver)


def start_server(debug):
    app.run(host="localhost", debug=debug)


def start_server2(debug):
    app.run(host="0.0.0.0", port=5000, debug=debug)


start_server(debug)
# start_server2(debug)
