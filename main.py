from flask import Flask

# creating the object for the Flask class
app = Flask(__name__)


@app.route("/")

def intro():
    return "Hello Aniket!!"

# route() specifies the endpoint of the url which helps the func to get triggered/call
@app.route("/flask2")

def hola():
    return "Hello 2222222222"


app.run(debug = True)









