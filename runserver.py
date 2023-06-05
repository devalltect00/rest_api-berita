from api import create_app
from api.config.config import config_dict

if __name__ == '__main__':
    app = create_app(config=config_dict['production'])
    app.run()