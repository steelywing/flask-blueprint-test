from flask import Flask, render_template
import blueprint_0
import blueprint_1

app = Flask(__name__)
app.register_blueprint(blueprint_0.blueprint, url_prefix='/bp-0')
app.register_blueprint(blueprint_1.blueprint, url_prefix='/bp-1')

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
