from flask import Flask, request, jsonify, render_template
import re
import hashlib
import ipaddress

app = Flask(__name__)

def luhn_check(card_number: str) -> bool:
    """Validate credit card number using Luhn's Algorithm"""
    digits = [int(d) for d in card_number if d.isdigit()]
    checksum = 0
    reverse_digits = digits[::-1]

    for i, digit in enumerate(reverse_digits):
        if i % 2 == 1:
            doubled = digit * 2
            if doubled > 9:
                doubled -= 9
            checksum += doubled
        else:
            checksum += digit

    return checksum % 10 == 0

def detect_type(user_input: str) -> str:
    user_input = user_input.strip()

    # Credit Card (check format + validate with Luhn)
    if re.match(r"^\d{13,19}$", user_input.replace(" ", "")):  # Detect if input is a credit card number (13–19 digits).
        card_num = user_input.replace(" ", "")
        if luhn_check(card_num):
            return "Valid Credit Card"
        # else:
        #     return "Invalid Credit Card && It's Integer"

    # Phone Number (basic global match, 7–15 digits, with +, spaces, or -)
    if re.match(r"^\+?[0-9\s\-]{7,15}$", user_input):
        return "Phone Number && Integer"
    
    # Integer
    if user_input.isdigit():
        return "Integer"

    # Float
    try:
        float(user_input)
        if "." in user_input:
            return "Float"
    except ValueError:
        pass

    # URL (http, https, ftp)
    if re.match(r"^(https?|ftp)://[^\s/$.?#].[^\s]*$", user_input):
        return "URL"

    # Phone Number (basic global match, 7–15 digits, with +, spaces, or -)
    if re.match(r"^\+?[0-9\s\-]{7,15}$", user_input):
        return "Phone Number"

    # Email
    if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", user_input):
        return "Email"

    # IPv4 / IPv6
    try:
        ipaddress.ip_address(user_input)
        return "IP Address"
    except ValueError:
        pass

    # Credit Card (check format + validate with Luhn)
    if re.match(r"^\d{13,19}$", user_input.replace(" ", "")):  # 13–19 digits
        card_num = user_input.replace(" ", "")
        if luhn_check(card_num):
            return "Valid Credit Card"
        else:
            return "Invalid Credit Card"
    
    # Hash detection (common lengths: MD5, SHA1, SHA256)
    hash_patterns = {
        "MD5": r"^[a-f0-9]{32}$",
        "SHA1": r"^[a-f0-9]{40}$",
        "SHA256": r"^[a-f0-9]{64}$",
    }
    for htype, pattern in hash_patterns.items():
        if re.match(pattern, user_input.lower()):
            return f"Hash ({htype})"

    # Default case
    return "String"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/check", methods=["POST"])
def check_input():
    data = request.json or {}
    user_input = data.get("input", "")
    if not user_input:
        return jsonify({"error": "No input provided"}), 400
    
    result = detect_type(user_input)
    return jsonify({"input": user_input, "type": result})

if __name__ == "__main__":
    app.run(debug=True)
