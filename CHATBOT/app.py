from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)



# Set your API key
openai.api_key = "YOUR_OPENAI_API_KEY"
@app.route("/")
def home():
    
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json.get("message")

    # Call OpenAI GPT API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Or gpt-4
        messages=[{"role": "user", "content": user_message}]
    )

    bot_reply = response.choices[0].message["content"]
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
