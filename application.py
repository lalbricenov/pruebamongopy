from flask import Flask, render_template, redirect, request
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://lbriceno:SjC91ombnfM1N5hI@cluster0.ykukg.mongodb.net/sample_airbnb?retryWrites=true&w=majority")
db = client.sample_airbnb
#SjC91ombnfM1N5hI
#lbriceno

@app.route("/")
def index():
    fiveBeds = db.listingsAndReviews.find_one({'beds':5})
    return render_template("index.html", title = "Hola", result = fiveBeds)