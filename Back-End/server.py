from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///geodata.db'
db = SQLAlchemy(app)

# database model
class Place(db.Model):
    # fields here
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lat = db.Column(db.Integer, nullable=False)
    lon = db.Column(db.Integer, nullable=False)
    ele = db.Column(db.Integer, nullable=False)
    street = db.Column(db.Text)

    def __repr__(self):
        return '<Place {}'.format(self.name)
        

# Routes
@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/positions')
def positions():
    start = request.args.get('start')
    end = request.args.get('end')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
