# 1. import Flask
from flask import Flask, jsonify

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Routes available:<br/> /api/v1.0/ <br/> precipitation, stations, tobs, start and start/end"


# 4. Define what to do when a user hits the /about route
@app.route("/precipitation")
def precipitation():
    print("working...")
    return "Welcome to my 'About' page!"

@app.route("/stations")
def stations():
    print("working...")
    
@app.route("/tobs")
def tobs():
    print("working...")

@app.route("/<start>")
def start():
    print("working...")

@app.route("/<start>/<end>")
def startend():
    print("working...")


if __name__ == "__main__":
    app.run(debug=True)
