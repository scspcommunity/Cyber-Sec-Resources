from flask import Flask, request
from jinja2 import Environment

app = Flask(__name__)
jinja2 = Environment()

@app.route("/")
def index():
    imie = request.values.get('scsp')
    return jinja2.from_string('Hey ' + imie).render()

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=8888)
