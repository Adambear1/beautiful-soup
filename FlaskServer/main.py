from flask import Flask, request, render_template, jsonify
from flask_restful import Resource, Api
from Routes.index import *

app = Flask(__name__)
api = Api(app)


class Get_Articles(Resource):
    def get(self, organization):
        response = get_articles(organization)
        return jsonify(response)

class Search_Topics(Resource):
    def get(self, query):
        response = search_for(query)
        print(response)
        return (response)

class Get_All_Saved_Articles(Resource):
    def get(self):
        response = get_all_saved_articles()
        return (response)

class Get_Article_By_Value(Resource):
    def get(self, value):
        response = get_articles_by_value(value)
        return (response)

class Save_Articles(Resource):
    def post(self):
        body = request.get_json(force=True)
        response = save_articles(body)
        return (jsonify(response))
        # print(request.get_json())



@app.route("/")
def index():
    return render_template("index.html", token="Hello React")


api.add_resource(Get_Articles, "/api/search/<string:organization>")
api.add_resource(Search_Topics, "/api/search_topic/<string:query>")
api.add_resource(Save_Articles, "/api/save")
api.add_resource(Get_All_Saved_Articles, "/api/saved/all")
api.add_resource(Get_Article_By_Value, "/api/saved/<string:value>")

if __name__ == "__main__":
    app.run(debug=True)
