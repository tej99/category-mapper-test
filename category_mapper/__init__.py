import logging
import os

from flask import Flask, jsonify
from flask_restful import Api
from structlog import wrap_logger

from category_mapper.models import models
from category_mapper.resources.category_map import CategoryMap

logger = wrap_logger(logging.getLogger(__name__))

app = Flask(__name__)

api = Api(app)

app_config = 'config.{}'.format(os.environ.get('APP_SETTINGS', 'Config'))
app.config.from_object(app_config)

models.db.init_app(app)

logger.info('Starting Category Mapper Service ...')


def drop_database():
    models.db.drop_all()

with app.app_context():
    models.db.create_all()
    models.db.session.commit()

api.add_resource(CategoryMap, '/category/<retailer_cat>')


@app.errorhandler(Exception)
def handle_exception(error):
    logger.error("There was an error. Details: {}".format(error))
    response = jsonify({"error": "Internal error"})
    response.status_code = 500
    return response
