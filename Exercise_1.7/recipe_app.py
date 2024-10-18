class Recipe(Base):
    __tablename__ = "final_recipes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredient = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return f"<Recipe ID: {self.id} - {self.name} ({self.difficulty})>"

    def __str__(self):
        return (f"Recipe Name: {self.name}\n"
                f"Ingredients: {self.ingredients}\n"
                f"Cooking Time: {self.cooking_time} minutes\n"
                f"Difficulty: {self.difficulty}\n"
                + "-"*40)
    
    def calculate_difficulty(self):
        ingredients_list = self.return_ingredients_as_list()
        if len(ingredients_list) <= 3 and self.cooking_time < 10:
            self.difficulty = "Easy"
        elif len(ingredients_list) <= 5 and self.cooking_time < 20:
            self.difficulty = "Medium"
        elif len(ingredients_list) > 5 and self.cooking_time < 30:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"
    
    def return_ingredients_as_list(self):
        if self.ingredients == "":
            return []
        return self.ingredients.split(", ")

    Base.metadata.create_all(engine)

    def create_recipe():
    # Get recipe details from the user
    name = input("Enter the name of the recipe (max 50 characters): ")
    while len(name) > 50 or not name.isalnum():
        print("Invalid input. Recipe name must be alphanumeric and under 50 characters.")
        name = input("Enter the name of the recipe (max 50 characters): ")

    cooking_time = input("Enter the cooking time (in minutes): ")
    while not cooking_time.isnumeric():
        print("Invalid input. Cooking time must be a number.")
        cooking_time = input("Enter the cooking time (in minutes): ")

    # Collect ingredients from the user
    ingredients = []
    num_ingredients = input("How many ingredients does the recipe have? ")
    while not num_ingredients.isnumeric():
        print("Invalid input. Please enter a valid number.")
        num_ingredients = input("How many ingredients does the recipe have? ")
    
    for i in range(int(num_ingredients)):
        ingredient = input(f"Enter ingredient {i+1}: ")
        ingredients.append(ingredient)

    ingredients_str = ", ".join(ingredients)  # Convert list to comma-separated string

    # Create the recipe object
    recipe_entry = Recipe(name=name, ingredients=ingredients_str, cooking_time=int(cooking_time))
    
    # Calculate and assign the difficulty
    recipe_entry.calculate_difficulty()

    # Add the recipe to the database and commit
    session.add(recipe_entry)
    session.commit()
    print(f"Recipe '{name}' added successfully.")

 