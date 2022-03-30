"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet, Vehicle, Favoritescharacter, Favoritesplanet, Favoritesvehicle
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():
    query_user = User.query.all()
    query_user = list(map(lambda User: username.serialize(), query_user))
    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "users":query_user
    }

    return jsonify(response_body), 200

@app.route('/character', methods=['GET'])
def get_character():
    query_character = Character.query.all()
    query_character = list(map(lambda Character: Character.serialize(), query_character))
    response_body = {
        "msg": "Hello, this is your GET /Character response",
        "Character" : query_character
    }

    return jsonify(response_body), 200

@app.route('/character/<int:character_id>', methods=['DELETE'])
def delete_character(id):
    character_delete = Character.query.get(id)
    if not character_delete:
        response_body = {
            "msg": "Hello, this is your DELETE /Character response",
            "Character" : "Character doesn't exist, can't be eliminated"
        }
        return jsonify(response_body), 200
    db.session.delete(character_delete)
    db.session.commit()
    response_body = {
        "msg": "Hello, this is your DELETE /Character response",
        "Character" : "Character eliminated"
    }

@app.route('/character', methods=['POST'])
def post_character():
    body = request.get_json()
    character = Character(character_name=body['character_name'],  home_planet=body['home_planet'])
    db.session.add(character)
    db.session.commit()
    response_body = {
        "msg": "Hello, this is your POST /character response "
    }

    return jsonify(response_body), 200

@app.route('/planet', methods=['GET'])
def get_planets():
    query_planet = Planet.query.all()
    query_planet = list(map(lambda Planet: Planet.serialize(), query_planet))
    response_body = {
        "msg": "Hello, this is your GET /planet response",
        "Planet" : query_planet
    }

    return jsonify(response_body), 200

@app.route('/planet/<int:planet_id>', methods=['DELETE'])
def delete_planet(id):
    planet_delete = Planet.query.get(id)
    if not planet_delete:
        response_body = {
            "msg": "Hello, this is your DELETE /planet response",
            "Planet" : "Planet doesn't exist, can't be eliminated"
        }
        return jsonify(response_body), 200
    db.session.delete(planet_delete)
    db.session.commit()
    response_body = {
        "msg": "Hello, this is your DELETE /planet response",
        "Planet" : "Planet eliminated"
    }


    return jsonify(response_body), 200

@app.route('/planet', methods=['POST'])
def post_planet():
    body = request.get_json()
    planet = Planet(planet_name=body['planet_name'], density=body['density'], population=body['population'])
    db.session.add(planet)
    db.session.commit()
    response_body = {
        "msg": "Hello, this is your POST /planet response "
    }

    return jsonify(response_body), 200

@app.route('/vehicle', methods=['GET'])
def get_vehicles():
    query_vehicles = Vehicle.query.all()
    query_vehicles = list(map(lambda Vehicle: Vehicle.serialize(), query_vehicles))
    response_body = {
        "msg": "Hello, this is your GET /vehicles response",
        "Vehicle" : query_vehicles
    }

    return jsonify(response_body), 200

@app.route('/vehicle/<int:vehicle_id>', methods=['DELETE'])
def delete_vehicle(id):
    vehicle_delete = Vehicle.query.get(id)
    if not vehicle_delete:
        response_body = {
            "msg": "Hello, this is your DELETE /vehicle response",
            "Vehicle" : "Vehicle doesn't exist, can't be eliminated"
        }
        return jsonify(response_body), 200
    db.session.delete(vehicle_delete)
    db.session.commit()
    response_body = {
        "msg": "Hello, this is your DELETE /vehicle response",
        "Vehicle" : "Vehicle eliminated"
    }

    return jsonify(response_body), 200

@app.route('/vehicles', methods=['POST'])
def post_vehicles():
    body = request.get_json()
    vehicle = Vehicles(vehicle_name=body['vehicle_name'],vehicle_model=body['vehicle_model'],vehicle_manufacturer=body['vehicle_manufacturer'],vehicle_pilot=body['vehicle_pilot'])
    db.session.add(Vehicle)
    db.session.commit()
    response_body = {
        "msg": "Hello, this is your POST /vehicles response "
    }

    return jsonify(response_body), 200  

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)