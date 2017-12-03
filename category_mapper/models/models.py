import logging

from structlog import wrap_logger
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer

logger = wrap_logger(logging.getLogger(__name__))

db = SQLAlchemy()


class CategoryMap(db.Model):
    """Category maps database model"""

    __tablename__ = "category_map"

    id = Column("id", Integer(), primary_key=True)
    retailer_category = Column("retailer_category", String(), unique=True)
    normalised_category = Column("normalised_category", String())

    def __init__(self, retailer_category, normalised_category):

        logger.debug("Initialised Category Maps entity: retailer_category: {} normalised_category: {}".format(
            retailer_category,
            normalised_category
        ))
        self.retailer_category = retailer_category
        self.normalised_category = normalised_category

    def serialize(self):
        """Return object data in easily serializeable format"""
        category_map = {
            "retailer_category": self.retailer_category,
            "normalised_category": self.normalised_category
        }

        return category_map
