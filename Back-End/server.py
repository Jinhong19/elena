from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys
sys.path.insert(1, os.path.abspath("algorithms"))
from pathfinder import *

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
    start = data['start']
    end = data['end']
    percentage = float(data['percentage'])
    min = True if data['mM'] == 'Min' else False
    # routes = main_controller("Bruno's", "Northampton Cooperative Bank", 1.0)
    routes = main_controller(start, end, percentage)
    res = {'start': start, 'end': end}
    thePath = routes[0]
    if min:
        for path in routes:
            if thePath[1] > path[1]:
                thePath = path
    else:
       for path in routes:
            if thePath[1] < path[1]:
                thePath = path
    pathJ = [{'lat': p[0], 'lon': p[1]} for p in thePath[0]]
    res['route'] = pathJ
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
