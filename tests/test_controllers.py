import unittest

from category_mapper.controllers.category_map import get_normalised_category


class TestControllers(unittest.TestCase):

    def test_get_normalised_category_case_1(self):
        input_category = 'Mens+clothing'
        expected = '/Men/Clothing'
        output = get_normalised_category(input_category)
        
        self.assertEqual(expected, output)

    def test_get_normalised_category_case_2(self):
        input_category = 'adult+-+female+-+jewelry+and+watches+-+fashion+jewelry'
        expected = '/Women/Jewellery'
        output = get_normalised_category(input_category)

        self.assertEqual(expected, output)
