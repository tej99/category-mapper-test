from category_mapper.decorators.session_decorator import with_db_session
from category_mapper.models.models import CategoryMap

category_mapper = {
        ('Women', 'female', 'women', 'feminine', 'her'): {
            ('Accessories', 'accessory', 'belt', 'glove', 'hat', 'purses'): None,
            ('Bags', 'bag', 'backpacks', 'clutch', 'luggage', 'shoulder', 'tote'): None,
            ('Clothing', 'clothes', 'apparel', 'costume'): None,
            ('Footwear', 'shoe', 'boot', 'slipper', 'sneaker', 'trainer'): None,
            ('Jewellery', 'jwelery', 'bracelet', 'earring', 'necklace', 'watches'): None,
            'Others': None
        },
        ('Men', 'male', 'his'): {
            ('Accessories', 'accessory','belt', 'glove', 'hat', 'wallet'): None,
            ('Bags', 'bag', 'backpacks', 'clutch', 'luggage', 'shoulder', 'tote'): None,
            ('Clothing', 'clothes', 'apparel', 'costume'): None,
            ('Footwear', 'shoe', 'boot', 'slipper', 'sneaker', 'trainer'): None,
            ('Jewellery', 'bracelet', 'earring', 'necklace', 'watches'): None,
            'Others': None
        },
        'Others': None
    }


def get_normalised_category(retailer_cat):
    normalised_category = ''
    category_dict = category_mapper

    while category_dict:
        sub_category, category_dict = get_sub_category(category_dict, retailer_cat)
        normalised_category = normalised_category + '/' + sub_category

    return normalised_category


def get_sub_category(category_dict, retailer_cat):
    for k, v in category_dict.items():
        if k == 'Others':
            return 'Others', None
        else:
            for word in k:
                if word.lower() in retailer_cat.lower():
                    return k[0], category_dict[k]


@with_db_session
def create_normalised_category(retialer_cat, session):
    normalised_category = get_normalised_category(retialer_cat)
    category_map = CategoryMap(retialer_cat, normalised_category)

    session.merge(category_map)
    return category_map.serialize()
