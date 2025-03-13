from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS

PVC_MOUNT_PATH = os.getenv('PVC_MOUNT_PATH', '/mnt/pvc')

@app.route('/list')
def list_files():
    try:
        files = os.listdir(PVC_MOUNT_PATH)
        return jsonify({
            "path": PVC_MOUNT_PATH,
            "files": files
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
