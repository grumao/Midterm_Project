
from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/hello', methods=['GET', 'POST'])
def hello_world():
    return "Hello, world!"

@app.route('/hello/<name>', methods=['GET'])
def hello_name(name):
    return f"Hello, {name}"

@app.route('/interesting/<name>', methods=['GET'])
def serve_html(name):
    return f"""
    <html>
    <body>
    <h1>Hello {name}</h1>
    <p>This is my fancy webpage</p>
    </body>
    </html>
    """

@app.route('/sample_post', methods=['POST'])
def sample_post():
    # Extract the json from the incoming request.
    content = request.json
    # Do some work on the content
    if "text" not in content:
        return jsonify({"error": "Required field 'text' is missing"}), 400
    else:
        print(content["text"])
    # Return what you need when processing is done.
    return jsonify({"text": content["text"]})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
