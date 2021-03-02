from flask import Flask, request, render_template
from flask_restful import Resource, Api
from Routes.index import get_articles

app = Flask(__name__)
api = Api(app)


class Get_Articles(Resource):
    def get(self, organization):
        return get_articles(organization)


@app.route("/")
def index():
    return render_template("index.html", token="Hello React")


api.add_resource(Get_Articles, "/api/<string:organization>")


if __name__ == "__main__":
    app.run(debug=True)
