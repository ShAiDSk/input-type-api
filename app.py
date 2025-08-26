from flask import Flask, request, jsonify, render_template
import re
import hashlib

app = Flask(__name__)

def detect_type(user_input):
    # Check if it's an integer
    if user_input.isdigit():
        return "Integer"

    # Check if it's a float
    try:
        float(user_input)
        return "Float"
    except ValueError:
        pass

    # Check if it's a hash (MD5, SHA1, SHA256, etc.)
    hash_patterns = {
        "MD5": r"^[a-f0-9]{32}$",
        "SHA1": r"^[a-f0-9]{40}$",
        "SHA256": r"^[a-f0-9]{64}$",
    }
    for htype, pattern in hash_patterns.items():
        if re.match(pattern, user_input.lower()):
            return f"Hash ({htype})"

    # Default: String
    return "String"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/check", methods=["POST"])
def check_input():
    data = request.json
    user_input = data.get("input", "")
    result = detect_type(user_input)
    return jsonify({"input": user_input, "type": result})

if __name__ == "__main__":
    app.run(debug=True)
