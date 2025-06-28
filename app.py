from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.is_json:
        data = request.get_json()
        print("Signal reçu :", data)
        return jsonify({"status": "ok"}), 200
    else:
        print("⚠️ Requête non-JSON reçue")
        return jsonify({"error": "Unsupported Media Type"}), 415

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
