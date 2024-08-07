from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/helloworld")
def helloworld():
    user = request.args.get('user')
    if user:
        return f"Hello {user}!"
    return jsonify({"message": "Hello World!"})
# return "Hello World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
    

