from flask import Flask
from flask_mongoengine import MongoEngine





app = Flask(__name__)
db_config= {
    'db': 'YOGA_Studio.user',
    'host': 'mongodb://localhost/YOGA_Studio.user',
    'port': 27017
}

db = MongoEngine()


    
db.init_app(app, config=db_config)
 

class User(db.Document):
    name = db.StringField()
    email = db.StringField()
    def to_json(self):
        return {"name": self.name,
                "email": self.email}


if __name__ == "__main__":
    app.run(debug=True)