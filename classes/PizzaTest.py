import unittest

class TestPizza(unittest.TestCase):
    def test_pizza_creation(self):
        pizza = Pizza("Margherita", ["tomato", "mozzarella", "basil"], 10.99)
        self.assertEqual(pizza.nom, "Margherita")
        self.assertEqual(pizza.ingredients, ["tomato", "mozzarella", "basil"])
        self.assertEqual(pizza.prix, 10.99)