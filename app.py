from flask import Flask, render_template, request
from func import insert, print_table


app = Flask("cafeteria-status")
ver = "v0.1.0"
debug = True


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print("POST received")
        print(request.form.get("state"))
        insert(request.remote_addr, int(request.form.get("state")))
        print_table()
    return render_template("layout.html", ver=ver)


def start_server(debug):
    app.run(host="0.0.0.0", port=5050, debug=debug)


start_server(debug)
