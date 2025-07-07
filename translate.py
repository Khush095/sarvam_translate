from flask import Flask, request, jsonify
from sarvamai import SarvamAI

app = Flask(__name__)

client = SarvamAI(
    api_subscription_key="sk_04h8qmg4_XbZEK4zL756OwGdGt16MntAD",
)

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    input_text = data.get("input", "")
    source_language_code = data.get("source_language_code", "en-IN")
    target_language_code = data.get("target_language_code", "hi-IN")
    speaker_gender = data.get("speaker_gender", "Male")
    model = data.get("model", "sarvam-translate:v1")

    try:
        response = client.text.translate(
            input=input_text,
            source_language_code=source_language_code,
            target_language_code=target_language_code,
            speaker_gender=speaker_gender,
            model=model,
        )
        return jsonify({"translated_text": response.translated_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
