import json
import logging

from flask import Response
from flask_restful import Resource
from structlog import wrap_logger

from category_mapper.controllers import category_map
from category_mapper.controllers.queries import query_category_map_by_retailer_category

logger = wrap_logger(logging.getLogger(__name__))

"""Rest endpoint for Category Mapper resource."""


class CategoryMap(Resource):
    """Resource for Category Mapper"""

    @staticmethod
    def get(retailer_cat):
        """Get normalised category by retailer category"""

        logger.info("Attempting to normalise category {}".format(retailer_cat))
        normalised_category = category_map.get_normalised_category(retailer_cat)

        response_data = json.dumps({"normalised_category": normalised_category})

        return Response(response_data, status=200, mimetype='application/json')

    @staticmethod
    def post(retailer_cat):
        """Create category map for retailer category"""

        logger.info("Attempting to normalise category {}".format(retailer_cat))

        existing_category_map = query_category_map_by_retailer_category(retailer_cat)
        if existing_category_map:
            response_data = json.dumps(existing_category_map)
            return Response(response_data, status=200, mimetype='application/json')
        else:
            mapped_category = category_map.create_normalised_category(retailer_cat)
            response_data = json.dumps(mapped_category)
            return Response(response_data, status=201, mimetype='application/json')
