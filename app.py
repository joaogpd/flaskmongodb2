from flask import Flask, redirect, url_for, render_template, request, abort
import pymongo
from bson.objectid import ObjectId

app = Flask(__name__)

# client connected to mongodb atlas
client = pymongo.MongoClient("mongodb+srv://pstud:gVJQTsM2ftVKES5d@inf1039cardapuc.1cskrne.mongodb.net/?retryWrites=true&w=majority")
# database named cardapuc
db = client.cardapuc
# collection named restaurant
col = db.restaurantes

# this creates a route at url / with methods post and get, associated with a form with input text value in the index.html file
@app.route("/", methods=["POST", "GET"])
def landing_page():
    # by checking the method to be POST, it takes the input text value and parses the collection for the given key (in this case the name)
    if request.method == "POST":
        # takes the input value
        nome = request.form["nome"]
        # parses collection for given key
        result = col.find_one({"nome": nome})
        # checks whether or not the key is present in the collection
        try:
            # turns the id of the found object into a string (may not be strictly necessary)
            result['_id'] = str(result['_id'])
            # shows the information found
            # return "<p>Horario: {}</p>".format(result["horario"])
        # aborts with error 404 if not found
        except:
            abort(404)
        return render_template("index.html", result = result)
    
    return render_template("index.html")

    
