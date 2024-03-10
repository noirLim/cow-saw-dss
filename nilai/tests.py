from django.test import TestCase
from .utils import *

# Create your tests here.
# command menjalankan test case python manage.py test nilai
class NilaiTestCase(TestCase):
   
    def test_calculate_sum(self):
        result = calculate_sum(2,3)
        self.assertEqual(result,5)
    
