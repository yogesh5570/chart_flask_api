from flask import Flask, app, jsonify, redirect, url_for
from pymongo import MongoClient
from flask_cors import CORS
from flask_restful import Api, Resource

app = Flask(__name__)
cors = CORS(app)

client = MongoClient("mongodb+srv://Dbp_user:dbp_877086@cluster0.tenfk.mongodb.net/GraphTimeData?retryWrites=true&w=majority")

db = client.GraphTimeData
graphData = db.graphData

class Graphs(Resource):
    def get(self):
        graphs = graphData.find({}, {"_id":0}).limit(50)
        doc = [doc["samples"] for doc in graphs]
        return doc

class Index(Resource):
    def get(self):
        return redirect(url_for("graphs"))

api = Api(app)
api.add_resource(Index, "/", endpoint="index")
api.add_resource(Graphs, "/graphs", endpoint="graphs")

if __name__ == '__main__':
    app.run(debug=True)
