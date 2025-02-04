from flask import Flask, render_template
import datetime
import socket

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def home():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hostname = socket.gethostname()
    return render_template("index.html", time=current_time, hostname=hostname)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
