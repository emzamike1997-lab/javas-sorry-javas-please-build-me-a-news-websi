```python
# Configuration file for the news website

class Config:
    """Base configuration class"""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///news.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'secret_key_here'

class DevelopmentConfig(Config):
    """Development configuration class"""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration class"""
    pass

class TestingConfig(Config):
    """Testing configuration class"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_news.db'
```

###