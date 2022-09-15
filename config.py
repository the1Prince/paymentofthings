from flask_swagger_ui import get_swaggerui_blueprint


class Config(object):
    SQLALCHEMY_DATABASE_URI= 'mysql+pymysql://root:@localhost:3306/pot'#'sqlite:///pot.db'     
    
    
    SECRET_KEY = '8de9ceda-f1c9-4b62-8e1b-36fe45f98ecc'


    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    SWAGGER_BLUEPRINT = get_swaggerui_blueprint(SWAGGER_URL,API_URL,
    config = {
        'app_name':'Payment of Things API'
    }
    )
