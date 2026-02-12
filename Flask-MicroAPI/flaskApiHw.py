from flask import Flask, jsonify, request

app = Flask(__name__)

DATA = [
    {"id":1,"campus":"MMC","lat":25.76,"lon":-80.36},
    {"id":2,"campus":"BBC","lat":25.90,"lon":-80.13},
    {"id":3,"campus":"DC","lat":38.89,"lon":-77.01}
]

@app.route("/")
def index():
    return """
    <h1>FIU Campuses API</h1>
    <p> Try these endpoints:</p>
    <ul>
        <li><a href="/hello">/hello</a></li>
        <li><a href="/data">/data</a></li>
    </ul>
    """

@app.route("/hello")
def health():
    return jsonify({"message": "Hello World!"}), 200


@app.route("/data", methods=["GET", "POST"])
def campuses():
    # GET: Returns all campus data
    # POST: Adds a new campus to the DATA list
    if request.method == "POST":
        new_campus = request.get_json()
        if not all(key in new_campus for key in ["id", "campus", "lat", "lon"]):
            return jsonify({"error": "Missing required fields"}), 400
        DATA.append(new_campus)
        return jsonify({"message": "Campus added", "data": new_campus}), 201

    return jsonify(DATA), 200



if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
