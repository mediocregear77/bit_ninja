# frontend/server.py
# Flask frontend server to host the Bitcoin_Ninja GPU dashboard

from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder=".", static_url_path="")

@app.route("/")
def serve_index():
    return send_from_directory(".", "index.html")

@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory(".", path)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"[*] Serving frontend on http://localhost:{port}")
    app.run(host="0.0.0.0", port=port)
