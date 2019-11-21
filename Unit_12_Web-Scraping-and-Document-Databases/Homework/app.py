# Import Dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("/Users/aaronmorgan/Desktop/marsexploration-32382-firebase-adminsdk-rpeot-08957f0383.json")
# Import database module.
from firebase_admin import db

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://marsexploration-32382.firebaseio.com/'
})


# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_data_db"
# mongo = PyMongo(app)

@app.route("/")
def index():
    ref = db.reference('mars')
    mars_data = ref.get()

    return render_template("index.html", mars=mars_data)

#@app.route("/scrape")
#def scrape():
#    mars_data = mongo.db.mars_data_db
#    mars_data_new = scrape_mars.scrape()
#    mars_data.update({}, mars_data_new, upsert=True)
#    return "Scraping Successful"

#    return redirect("/", code=302)
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    ref = db.reference('mars')
    ref.update(mars_data)
    # mars_data["last_updated"] = str(mars_data["last_updated"])

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)