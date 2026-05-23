# AI-Cybersecurity-Assistant
from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""

    if request.method == "POST":
        user_input = request.form["question"]

        prompt = f"""
        You are an AI Cybersecurity Assistant.

        Explain cybersecurity concepts clearly and safely.

        User Question:
        {user_input}
        """

        try:
            result = model.generate_content(prompt)
            response = result.text
        except Exception as e:
            response = f"Error: {str(e)}"

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
