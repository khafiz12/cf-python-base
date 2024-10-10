class Recipe(object):
    def _init_(self, name):
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = 0 
        self.difficulty = None
    
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time
        self.calculate_difficulty()
    
    def get_cooking_time(self):
        return self.cooking_time
    
    def add_ingredients(self, *ingredients):
        for ingredient in ingredients:
            self.ingredients.append(ingredient)
        self.update_all_ingredients()
    
    def get_ingredients(self):
        return self.ingredients
    
    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"
    
    def get_difficulty(self):
        if self.difficulty is None:
            self.calculate_difficulty()
        return self.difficulty

    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients

    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            Recipe.all_ingredients.add(ingredient)

        # String representation to print the recipe nicely
    def __str__(self):
        return (f"Recipe: {self.name}\n"
                f"Ingredients: {', '.join(self.ingredients)}\n"
                f"Cooking Time: {self.cooking_time} minutes\n"
                f"Difficulty: {self.get_difficulty()}\n")

# Recipe search method outside of the class
def recipe_search(data, search_term):
    print(f"Searching for recipes containing '{search_term}':\n")
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)        










    



