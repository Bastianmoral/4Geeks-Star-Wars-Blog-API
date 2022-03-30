from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(150), nullable=False)
    home_planet = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<Character %r>' % self.character_name

    def serialize(self):
        return {
            "id": self.id,
            "character_name": self.character_name,
            "home_planet": self.home_planet,
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(150), nullable=False)
    population = db.Column(db.Integer)
    density = db.Column(db.String(50), nullable=False) 
    
    def __repr__(self):
        return '<Planet %r>' % self.planet_name

    def serialize(self):
        return {
            "id": self.id,
            "planet_name": self.planet_name,
            "population": self.population,
            "density": self.density,
        }

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_name = db.Column(db.String(150), nullable=False)
    vehicle_model = db.Column(db.String(150),nullable=False)
    vehicle_manufacturer = db.Column(db.String(150),nullable=False)
    vehicle_pilot = db.Column(db.String(150))
    
    def __repr__(self):
        return '<Vehicle %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.vehicle_name,
            "model": self.vehicle_model,
            "manufacturer": self.vehicle_manufacturer,
            "pilots": self.vehicle_pilots
        }

class Favoritescharacter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return self.id

    def serialize(self):
        return {
            "id": self.id,
            "character_id": self.character_id,
            "user_id":self.user_id
        }

class Favoritesplanet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return self.id

    def serialize(self):
        return {
            "id": self.id,
            "planet_id": self.planet_id,
            "user_id":self.user_id
        }

class Favoritesvehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return self.id

    def serialize(self):
        return {
            "id": self.id,
            "vehicle_id": self.vehicle_id,
            "user_id":self.user_id
        }


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(100), nullable=False, unique=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.first_name

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "Favoritescharacter": self.getFavoritescharacter(),
            "Favoritesplanet": self.getFavoritesplanet(),
            "Favoritesvehicle": self.getFavoritesvehicle(),
        }

    def getFavoritescharacter(self):
        return list(map(lambda fav: fav.serialize(),self.favorite_character))
    
    def getFavoritesPlanet(self):
        return list(map(lambda fav: fav.serialize(),self.favorite_character))
    
    def getFavoritescharacter(self):
        return list(map(lambda fav: fav.serialize(),self.favorite_character))
    




""" from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        } """