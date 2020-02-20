import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from workshop import add, multiply

# add(1, 1) == 2
class TestWorkshop(unittest.TestCase):
    def test_add_1_and_1_should_return_2(self):
        # arrange
        actual = add(1, 1)

        # act 
        expected = 2

        # assert
        self.assertEquals(expected, actual)

    def test_multiply_by_10_should_return_df_with_values_multiplied_by_10(self):
        # arrange
        df_test = pd.DataFrame({'age': [1, 2, 3]})
        actual = multiply(df_test, 10)

        # act 
        expected = pd.DataFrame({'age': [10, 20, 30]})

        # assert
        self.assert_frame_equal(expected, actual)


