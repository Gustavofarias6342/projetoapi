<<<<<<< HEAD
from flask import Flask, jsonify, render_template
=======
from flask import Flask, render_template
>>>>>>> main

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
<<<<<<< HEAD

from api import bp
app.register_blueprint(bp)

if __name__ == "__main__":
=======


from api import bp 
app.register_blueprint(bp)

if __name__ == "_main_":
>>>>>>> main
    app.run(host="0.0.0.0")