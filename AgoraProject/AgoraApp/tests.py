from django.test import TestCase

# Create your tests here.
class ExampleTestCase(TestCase):
    def test_example(self):
        x = 1+1
        self.assertEqual(x,2)