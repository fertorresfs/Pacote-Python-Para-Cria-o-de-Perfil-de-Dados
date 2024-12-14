import unittest
import pandas as pd
from data_profiler import profile_data


class TestProfiler(unittest.TestCase):

    def test_profile_data(self):
        data = {'col1': [1, 2, 3, None, 5], 'col2': ['a', 'b', 'c', 'a', 'b']}
        df = pd.DataFrame(data)
        profile = profile_data(df)

        self.assertEqual(profile['col1']['tipo'], 'float64')
        self.assertEqual(profile['col1']['nao_nulos'], 4)
        self.assertEqual(profile['col1']['nulos'], 1)
        self.assertEqual(profile['col2']['tipo'], 'object')


if __name__ == '__main__':
    unittest.main()
