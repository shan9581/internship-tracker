from mainProject import app



@app.route("/")
def home():
    return("hello world")