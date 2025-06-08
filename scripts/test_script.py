
import unittest
import joblib
import numpy as np

class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = joblib.load("model.pkl")
    
    def test_prediction_shape(self):
        pred = self.model.predict(np.array([[1.0, 2.0, 3.0]]))
        self.assertEqual(pred.shape, (1,))

if __name__ == '__main__':
    unittest.main()
