from flask import Flask, request, render_template
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class Get_Stocks(Resource):
    def get(self):
        return {"TYPE": "request"}


@app.route("/")
def index():
    return render_template("index.html", token="Hello React")


api.add_resource(Get_Stocks, "/apis")


if __name__ == "__main__":
    app.run(debug=True)
