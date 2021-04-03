from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# in-memory dictionary
memcache = {}

@app.route("/")
@app.route("/<name>")
def hello(name=None):
    return render_template('base.html', name=name, greetings=memcache)


# @app.route("/cache", methods=["GET", "POST"])
# def cache():
#     if request.method == "POST":
#         memcache.update(request.json)
#         return "Success"
#     else:
#         return jsonify(memcache)


@app.route("/greetings", methods=["POST"])
def greetings():
    memcache.update(request.json)
    return "Success"