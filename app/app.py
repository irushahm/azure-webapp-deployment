from flask import Flask, render_template
from datetime import datetime 
import socket
import platform
import os

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def home():
    # Get current time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Get hostname
    hostname = socket.gethostname()

    # Get IP address (for localhost)
    ip_address = socket.gethostbyname(hostname)

    # Get OS version
    os_version = platform.system() + " " + platform.release()

    #Return to index html
    return render_template("index.html", time=current_time, hostname=hostname, ip_address=ip_address,os_version=os_version)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
