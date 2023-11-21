from flask import Flask, render_template


app = Flask(__name__)

@app.route("/flask3")

def demoWeb():
    name = 'Aniket'
    return render_template('index.html', index_variable = name)



@app.route("/flask4")

def Web():
    name = 'Ankit'
    return render_template('index.html', index_variable = name)


app.run(debug = True)