class ShoppingList(object):
    def _init_(self, list_name):
        self.list_name = list_name
        self.shopping_list = []
        def add_item(self, item):
            if  item not in self.shopping_list:
                self.shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
            else:
                print(f"'{item}' is alread in the shopping list.")
        def remove_item(self, item):
            if  item in self.shopping_list:
                self.shopping.remove(item)
                print(f"'{item}' has been removed from shopping list.")
            else:
                print(f"'{item}' is not in the shopping list.")
        def view_list(self):
            if  self.shopping_list:
                print(f"Items in '{self.list_name}':")
                for item ins self.shopping_list:
                    print(f"-{item}")
            else:
                print(f"'{self.list_name}' is empty.")

class Height:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __sub__(self, other):
        # Convert both heights to inches first
        total_inches_self = self.feet * 12 + self.inches
        total_inches_other = other.feet * 12 + other.inches
        
        # Perform the subtraction
        diff_inches = total_inches_self - total_inches_other

        # Convert back to feet and inches
        diff_feet = diff_inches // 12
        remaining_inches = diff_inches % 12
        
        # Return the new Height object
        return Height(diff_feet, remaining_inches)

    def __str__(self):
        return f"{self.feet} feet {self.inches} inches"


class Height:
    def _init_(self, feet, inches):
        self.feet = feet
        self.inches = inches
    def total_inches(self):
        return self.feet * 12 + self.inches
    def _it_(self, other):
        return self.total_inches() < other.total_inches()
    def _gt_(self, other):
        return self.total.inches() > other.total.inches() 
    def _ge_(self, other):
        return self.total.inches() >= other.total.inches()
    def _ne_(self, other):
        return self.total.inches() != other.total.inches() 
    
