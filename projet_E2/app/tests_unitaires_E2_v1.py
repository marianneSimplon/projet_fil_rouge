import unittest
import pandas as pd
from app_v1 import inputs_to_df, preprocess_inputs, predict
# import warnings
# warnings.filterwarnings('ignore')  # setting ignore as a parameter


class MyTestCase(unittest.TestCase):

    def test_inputs_to_df_type(self):
        self.assertEqual(
            type(inputs_to_df("-119.84", "36.77", 6, 1853, 473, 1397, 417, "1.4817", "INLAND")), pd.core.frame.DataFrame)

    def test_inputs_to_df_output_nbcol(self):
        self.assertEqual(
            len(inputs_to_df("-119.84", "36.77", 6, 1853, 473, 1397, 417, "1.4817", "INLAND").columns), 9)

    def test_preprocess_inputs_output_nbcol(self):
        self.assertEqual(len(preprocess_inputs(pd.DataFrame({'longitude': [float("-119.84")], 'latitude': [float("36.77")], 'housing_median_age': [6], 'total_rooms': [1853], 'total_bedrooms': [
            473], 'population': [1397], 'households': [417], 'median_income': [float("1.4817")], 'ocean_proximity': ["INLAND"]})).columns), 11)

    def test_preprocess_inputs_type(self):
        self.assertEqual(
            type(preprocess_inputs(pd.DataFrame({'longitude': [float("-119.84")], 'latitude': [float("36.77")], 'housing_median_age': [6], 'total_rooms': [1853], 'total_bedrooms': [
                473], 'population': [1397], 'households': [417], 'median_income': [float("1.4817")], 'ocean_proximity': ["INLAND"]}))), pd.core.frame.DataFrame)

    # def test_predict(self):
    #     self.assertTrue(predict(pd.DataFrame(
    #         [[0.457404, 0.448936, 0.098039, 0.046981, 0.073103, 0.038936, 0.068257, 0.067709, 1.0, 0.0, 0.0]], columns=["longitude", "latitude", "housing_median_age", "total_rooms", "total_bedrooms", "population", "households", "median_income", "INLAND", "NEAR_BAY", "NEAR_OCEAN"])) > 0)


if __name__ == '__main__':
    unittest.main()
