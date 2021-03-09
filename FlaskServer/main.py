from flask import Flask, request, render_template, jsonify
from flask_restful import Resource, Api
from Routes.index import get_articles

app = Flask(__name__)
api = Api(app)


class Get_Articles(Resource):
    def get(self, organization):
        response = get_articles(organization)
        print(response)
        return jsonify(response)

class Save_Articles(Resource):
    def post(self):
        body = request.get_json(force=True)
        return (request.get_json(force=True))
        # print(request.get_json())



@app.route("/")
def index():
    return render_template("index.html", token="Hello React")


api.add_resource(Get_Articles, "/api/search/<string:organization>")
api.add_resource(Save_Articles, "/api/save")

if __name__ == "__main__":
    app.run(debug=True)
