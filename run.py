import logging
import os

from structlog import wrap_logger


if not os.getenv('APP_SETTINGS'):
    os.environ['APP_SETTINGS'] = 'Config'

from category_mapper import app  # NOQA # pylint: disable=wrong-import-position

logger = wrap_logger(logging.getLogger(__name__))


if __name__ == '__main__':
    logger.info("Starting listening on port {}".format(app.config['PORT']))
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=int(app.config['PORT']))
