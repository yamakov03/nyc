from flask import Flask, app, Blueprint, render_template
from flask_talisman import Talisman
import os
import random

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'nuoiGIughiugP(N@#$FGNPIUdglfiuGNPifngn2nGFLIwgdkjfgnoi23ngfaqfewgdsj'
    csp = {
    'default-src': [
            '\'self\'',
            '\'unsafe-inline\'',
            'cdnjs.cloudflare.com',
            'cdn.jsdelivr.net',
            'code.jquery.com',
            'maxcdn.bootstrapcdn.com',
            'fontawesome.com',
            'fonts.googleapis.com',
            'cdn.ckeditor.com',
            'w3.org',
            'unpkg.com',
            'unsafe-eval',
            'data:',
            'blob:',
            '*.mapbox.com',
        ],
        'img-src': [
            '*',
            'data:',
        ],
    }
    app.register_blueprint(views, url_prefix='/')
    Talisman(app, content_security_policy=csp)
    return app

views = Blueprint('views', __name__)

@views.route('/')
def index():
    imageFolders = [f for f in os.listdir('app/static/images') if not f.startswith('.')]


    brooklyn_bridge = os.listdir('app/static/images/brooklyn_bridge')
    central_park = os.listdir('app/static/images/central_park')
    chinatown_little_italy = os.listdir('app/static/images/chinatown_little_italy')
    financial = os.listdir('app/static/images/financial')
    flatiron_district = os.listdir('app/static/images/flatiron_district')
    hudson = os.listdir('app/static/images/hudson')
    hudson_yards_chelsea = os.listdir('app/static/images/hudson_yards_chelsea')
    koreatown = os.listdir('app/static/images/koreatown')
    midtown_5th_ave = os.listdir('app/static/images/midtown_5th_ave')
    midtown_broadway = os.listdir('app/static/images/midtown_broadway')

    brooklyn_bridge = ['images/brooklyn_bridge/' + f for f in brooklyn_bridge if not f.startswith('.')]
    central_park = ['images/central_park/' + f for f in central_park if not f.startswith('.')]
    chinatown_little_italy = ['images/chinatown_little_italy/' + f for f in chinatown_little_italy if not f.startswith('.')]
    financial = ['images/financial/' + f for f in financial if not f.startswith('.')]
    flatiron_district = ['images/flatiron_district/' + f for f in flatiron_district if not f.startswith('.')]
    hudson = ['images/hudson/' + f for f in hudson if not f.startswith('.')]
    hudson_yards_chelsea = ['images/hudson_yards_chelsea/' + f for f in hudson_yards_chelsea if not f.startswith('.')]
    koreatown = ['images/koreatown/' + f for f in koreatown if not f.startswith('.')]
    midtown_5th_ave = ['images/midtown_5th_ave/' + f for f in midtown_5th_ave if not f.startswith('.')]
    midtown_broadway = ['images/midtown_broadway/' + f for f in midtown_broadway if not f.startswith('.')]

    random.shuffle(brooklyn_bridge)
    random.shuffle(central_park)
    random.shuffle(chinatown_little_italy)
    random.shuffle(financial)
    random.shuffle(flatiron_district)
    random.shuffle(hudson)
    random.shuffle(hudson_yards_chelsea)
    random.shuffle(koreatown)
    random.shuffle(midtown_5th_ave)
    random.shuffle(midtown_broadway)

    return render_template('index.html', brooklyn_bridge=brooklyn_bridge, central_park=central_park, chinatown_little_italy=chinatown_little_italy, financial=financial, flatiron_district=flatiron_district, hudson=hudson, hudson_yards_chelsea=hudson_yards_chelsea, koreatown=koreatown, midtown_5th_ave=midtown_5th_ave, midtown_broadway=midtown_broadway)

if __name__ == '__main__':
    app = create_app()
    # app.run(debug=True, host= '192.168.1.140', port=5000)
    app.run(debug=True)
else:
    gunicorn_app = create_app()