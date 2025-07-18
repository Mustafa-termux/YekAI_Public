from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "BekirGPT Render Sunucusu Çalışıyor!"

@app.route("/soru", methods=["POST"])
def cevap():
    data = request.json
    soru = data.get("soru", "")
    # Burada openai çağrısı veya BekirGPT fonksiyonunu kullanabilirsin
    yanit = f"Senin soruna cevap: {soru}"  # Demo amaçlı
    return jsonify({"cevap": yanit})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
