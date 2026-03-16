```python
# Initialize the Flask application

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    """Create the Flask application"""
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    from app import routes, services
    return app
```

###