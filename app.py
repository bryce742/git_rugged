from flask import Flask
from blueprints.home.home import home_bp
from blueprints.buy.buy import buy_bp
from blueprints.rug_map.rug_map import rug_map_bp
from blueprints.watch.watch import watch_bp


app = Flask(__name__, template_folder='templates')

# Register blueprints
app.register_blueprint(home_bp, url_prefix='/')
app.register_blueprint(buy_bp, url_prefix='/buy')
app.register_blueprint(watch_bp, url_prefix='/watch')
app.register_blueprint(rug_map_bp, url_prefix='/rug-map')

if __name__ == '__main__':
    app.run()
