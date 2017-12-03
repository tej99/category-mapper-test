import logging
from functools import wraps

from structlog import wrap_logger

from category_mapper.models.models import db

log = wrap_logger(logging.getLogger(__name__))


def with_db_session(f):
    """
    Wraps the supplied function, and introduces a correctly-scoped database session which is passed into the decorated
    function as the named parameter 'session'.
    :param f: The function to be wrapped.
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        log.info("Acquiring database session.")
        session = db.session()
        try:
            result = f(*args, session=session, **kwargs)
            log.info("Committing database session.")
            session.commit()
            return result
        except Exception as e:
            log.info("Rolling-back database session.")
            session.rollback()
            raise e
        finally:
            log.info("Removing database session.")
            db.session.remove()
    return wrapper