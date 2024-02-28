from CartePizzeriaException import CartePizzeriaException

class CartePizzeria :

    def __init__(self):
        self.pizzas = []

    def isEmpty(self):
        return len(self.pizzas) == 0
    
    def nb_pizzas(self):
        return len(self.pizzas)
    
    def add_pizza(self,pizza):
        self.pizzas.append(pizza)

    def remove_pizza(self,nom):
        for pizza in self.pizzas:
            if pizza.nom == nom :
                self.pizzas.remove(pizza)
                return        
        raise CartePizzeriaException(f"La Pizza nommée '{nom} 'n'éxiste pas dans la carte")
