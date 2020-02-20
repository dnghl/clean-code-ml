import unittest
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from workshop import add, multiply, impute_nan

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
        df_expected = pd.DataFrame({'age': [10, 20, 30]})


        # act 
        df_actual = multiply(df_test)


        # assert
        assert_frame_equal(df_expected, df_actual)

    def test_impute_nan_should_return_df_with_nan_replaced_by_median_value(self):
        # arrange
        df_test = pd.DataFrame({
            'fare': [2, np.nan, 2],
            'price': [0, 0, np.nan]
            })

        df_expected = pd.DataFrame({
            'fare': [2, 2, 2],
            'price': [0, 0, 0]
            })
        
        # act
        df_actual = impute_nan(df_test)

        # assert
        assert_frame_equal(df_expected, df_test, check_dtype = False)

    def test_get_gamily_size_should_return_df_with_correct_FamilySize_and_IsAlone_col(self):
        # arrange
        df_test = pd.DataFrame({
           'SibSp': [0, 1, 2],
           'Parch': [0, 1, 2]
        })
        
        df_expected = pd.DataFrame({
           'FamilySize': [1, 3, 5]
           'IsAlone': [1, 0, 0]
         })
        
        # act
        df_actual = get_is_alone()
