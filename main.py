from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user/<user-id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "jake",
        "email": "example@example.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    
    return jsonify(user_data), 200

if __name__ == "__main__":
    app.run(debug=True)