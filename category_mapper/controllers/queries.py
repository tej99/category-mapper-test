import logging

from structlog import wrap_logger

from category_mapper.decorators.session_decorator import with_db_session
from category_mapper.models.models import CategoryMap

log = wrap_logger(logging.getLogger(__name__))


@with_db_session
def query_category_map_by_retailer_category(retailer_category, session):
    """
    Query to return category map based on retailer category
    :param retailer_category: the retailer category you want to map
    :return: category map or none
    """
    log.debug('Querying category map with retailer category {}'.format(retailer_category))

    mapped_category = session.query(CategoryMap).filter(CategoryMap.retailer_category == retailer_category).first()

    if mapped_category:
        return mapped_category.serialize()
    else:
        return
