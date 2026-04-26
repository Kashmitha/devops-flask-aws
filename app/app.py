from flask import Flask, jsonify
import platform, socket

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "running",
        "message": "DevOps Internship Project 🚀",
        "host": socket.gethostname(),
        "python": platform.python_version()
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
