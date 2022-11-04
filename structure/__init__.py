import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)


app.config['SECRET_KEY'] = 'asecretkey'
############################
### DATABASE SETUP ##########
########################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)
migrate = Migrate(app, db)
with app.app_context():
    if db.engine.url.drivername == "sqlite":
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

#########################
# LOGIN CONFIGS
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'



##################################################


from structure.core.views import core
from structure.users.views import users
from structure.web_features.views import web_features
from structure.error_pages.handlers import error_pages
from structure.about.views import abouts
from structure.pricing.views import pricings 
from structure.faq.views import faqs
from structure.testimonial.views import testimonials
from structure.team.views import teams
from structure.block.views import blocks
from structure.appearance.views import appearances

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(web_features)
app.register_blueprint(error_pages)
app.register_blueprint(abouts)
app.register_blueprint(pricings)
app.register_blueprint(faqs)
app.register_blueprint(testimonials)
app.register_blueprint(teams)
app.register_blueprint(blocks)
app.register_blueprint(appearances)
