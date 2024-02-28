import unittest

from CartePizzeria import CartePizzeria
from CartePizzeriaException import CartePizzeriaException
from Pizza import Pizza

class TestCartePizzeria(unittest.TestCase):
    def setUp(self):
        self.carte = CartePizzeria()
        self.pizza1 = Pizza("Margherita", ["tomato", "mozzarella", "basil"], 10.99)
        self.pizza2 = Pizza("Pepperoni", ["tomato", "mozzarella", "pepperoni"], 12.99)

    def test_carte_empty(self):
        self.assertTrue(self.carte.is_empty())

    def test_add_remove_pizza(self):
        self.carte.add_pizza(self.pizza1)
        self.assertFalse(self.carte.is_empty())
        self.assertEqual(self.carte.nb_pizzas(), 1)

        self.carte.remove_pizza("Margherita")
        self.assertTrue(self.carte.is_empty())
        self.assertEqual(self.carte.nb_pizzas(), 0)

    def test_remove_nonexistent_pizza(self):
        with self.assertRaises(CartePizzeriaException):
            self.carte.remove_pizza("NonExistentPizza")
