
from CartePizzeria import CartePizzeria
class Pizza: 
    def __init__(self , nom , ingredients , prix):
        self.nom = nom
        self.ingredients = ingredients
        self.prix = prix



# Exemple d'utilisation
carte = CartePizzeria()

pizza1 = Pizza("Margherita", ["tomato", "mozzarella", "basil"], 10.99)
pizza2 = Pizza("Pepperoni", ["tomato", "mozzarella", "pepperoni"], 12.99)

carte.add_pizza(pizza1)
carte.add_pizza(pizza2)
print("Nombre de pizzas dans la carte:", carte.nb_pizzas())
carte.remove_pizza("Margherita")
print("Nombre de pizzas dans la carte après suppression:", carte.nb_pizzas())

