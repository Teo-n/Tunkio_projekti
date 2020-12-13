class Config:
    DEBUG = True

    # alle pgadmin tiedot
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://Tunkiouser:TunkioPass@localhost/TunkioDB'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SECRET_KEY = 'super-secret-key'
    # JWT_ERROR_MESSAGE_KEY = 'message'

# pitää kutsua app.py:ssa
