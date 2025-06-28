from flask import Flask, request, jsonify
import sys

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    print("Webhook déclenché")
    sys.stdout.flush()

    if request.is_json:
        data = request.get_json()
        print("Signal reçu :", data)
        sys.stdout.flush()
        return jsonify({"status": "ok"}), 200
    else:
        print("⚠️ Requête non-JSON reçue")
        sys.stdout.flush()
        return jsonify({"error": "Unsupported Media Type"}), 415

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
