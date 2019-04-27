import os 

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://@localhost/mo'
    SECRET_KEY=os.environ.get("SECRET_KEY")
    #  email configurations

    # We setup the SMTP server and configure the port to use the gmail SMTP server port. 
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    # Then we set MAIL_USE_TLS configuration to true which enables a transport layer security to secure the emails when sending the emails.
    MAIL_USE_TLS = True
    # MAIL_USERNAME and MAIL_PASSWORD are our email address and password to authenticate to the gmail SMTP server. We set them as environment variables.
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

   



class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    pass


class DevConfig(Config):

    DEBUG = True

config_options = { 
'development':DevConfig,
'production':ProdConfig
}
