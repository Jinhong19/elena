from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys
sys.path.insert(1, os.path.abspath("algorithms"))
# from pathfinder import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///geodata.db'
db = SQLAlchemy(app)
CORS(app)

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
        return '<Place {}>'.format(self.name)
        
class Intersection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Integer, nullable=False)
    lon = db.Column(db.Integer, nullable=False)
    firstStreet = db.Column(db.Text)
    secondStreet = db.Column(db.Text)

    def __repr__(self):
        return '<Intersection at {} and {}>'.format(self.firstStreet, self.secondStreet)

# Routes
@app.route('/positions', methods=['POST'])
def positions():
    data = request.json
    # res = {'start': start, 'end': end}
    start = data['start']
    end = data['end']
    
    print(start, end, file=sys.stderr)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
