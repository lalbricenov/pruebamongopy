from flask import Flask, render_template, redirect, request
import pymongo
import os

app = Flask(__name__)
dbUser = os.environ['dbUser']
dbPass = os.environ['dbPass']

client = pymongo.MongoClient(f"mongodb+srv://{dbUser}:{dbPass}@cluster0.ykukg.mongodb.net/sample_airbnb?retryWrites=true&w=majority")
db = client.sample_airbnb

@app.route("/")
def index():
    fiveBeds = db.listingsAndReviews.find_one({'beds':5})
    return render_template("index.html", title = "Hola", result = fiveBeds)