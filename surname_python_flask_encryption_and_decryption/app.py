from flask import Flask, request, jsonify
from cryptography.fernet import Fernet

app = Flask(__name__)

key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route('/encrypt', methods=['POST'])
def encrypt():
    try:
        data = request.json.get("text")
        if not data:
            return jsonify({"error": "No text provided for encryption"}), 400

        encrypted_text = cipher_suite.encrypt(data.encode()).decode()
        return jsonify({"encrypted_text": encrypted_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/decrypt', methods=['POST'])
def decrypt():
    try:
        encrypted_data = request.json.get("encrypted_text")
        if not encrypted_data:
            return jsonify({"error": "No encrypted text provided for decryption"}), 400

        decrypted_text = cipher_suite.decrypt(encrypted_data.encode()).decode()
        return jsonify({"decrypted_text": decrypted_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
