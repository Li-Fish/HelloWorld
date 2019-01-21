from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask('helloworld')
app.config.from_pyfile('settings.py')

bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

from helloworld import errors, views, commands
