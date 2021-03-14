from flask import Flask, render_template
import pymongo
import json
import os

app = Flask(__name__)
CONNECTION_STRING = "mongodb+srv://" + os.environ.get('mongodb_user') + ":" + os.environ.get('mongodb_password') + "@cluster0.6sidv.mongodb.net/articles?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client['articles']
col = db['data']


@app.route("/articles")
def all_articles():
    dataList = list(col.find({}, {'_id': False}))
    return render_template('index.html', title="Articles", articlesjson=json.dumps(dataList))


@app.route('/articles/<string:search_name>')
def search_articles(search_name):
    dataList = list(col.find({'description': {"$regex": search_name, "$options": "-i"}}, {'_id': False}))
    return render_template('index.html', title="Articles", articlesjson=json.dumps(dataList))


if __name__ == '__main__':
    app.run(port=8000)
