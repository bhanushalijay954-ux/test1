from flask import Flask, render_template, request

app = Flask(__name__)

def check_phishing(text):
    suspicious_words = [
        "urgent", "click here", "verify", "password",
        "account suspended", "login", "bank", "free",
        "winner", "claim now"
    ]

    score = 0

    for word in suspicious_words:
        if word in text.lower():
            score += 1

    if score >= 2:
        return "⚠️ Suspicious Message (Possible Phishing)"
    else:
        return "✅ Looks Safe"

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        message = request.form["message"]
        result = check_phishing(message)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
