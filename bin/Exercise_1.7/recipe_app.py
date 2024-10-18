class Recipe(Base):
    __tablename__ = 'final_recipes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    ingredients = Column(String(255), nullable=False)
    cooking_time = Column(Integer, nullable=False)
    difficulty = Column(String(20), nullable=False)

    def __repr__(self):
        return f"<Recipe(id={self.id}, name={self.name}, difficulty={self.difficulty})>"

    def __str__(self):
        return (f"Recipe ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Ingredients: {self.ingredients}\n"
                f"Cooking Time: {self.cooking_time} mins\n"
                f"Difficulty: {self.difficulty}")

    def calculate_difficulty(self):
        ingredients_list = self.return_ingredients_as_list()
        num_ingredients = len(ingredients_list)
        if num_ingredients < 4 and self.cooking_time < 10:
            self.difficulty = "Easy"
        elif num_ingredients < 6 and self.cooking_time < 20:
            self.difficulty = "Medium"
        elif num_ingredients < 8 and self.cooking_time < 30:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

    def return_ingredients_as_list(self):
        if not self.ingredients:
            return []
        return self.ingredients.split(", ")

# Create the table
Base.metadata.create_all(engine)

def create_recipe():
    name = input("Enter the recipe name (max 50 characters): ")
    while len(name) > 50 or not name.isalnum():
        name = input("Invalid input. Enter a valid recipe name (max 50 characters): ")

    num_ingredients = int(input("How many ingredients? "))
    ingredients = []
    for i in range(num_ingredients):
        ingredient = input(f"Enter ingredient {i + 1}: ")
        ingredients.append(ingredient)
    ingredients_str = ", ".join(ingredients)

    cooking_time = input("Enter cooking time in minutes: ")
    while not cooking_time.isnumeric():
        cooking_time = input("Invalid input. Enter cooking time in minutes: ")

    recipe_entry = Recipe(name=name, ingredients=ingredients_str, cooking_time=int(cooking_time), difficulty="")
    recipe_entry.calculate_difficulty()
    
    try:
        session.add(recipe_entry)
        session.commit()
        print("Recipe added successfully!")
    except SQLAlchemyError as e:
        print(f"Error adding recipe: {e}")
        session.rollback()

def view_all_recipes():
    recipes = session.query(Recipe).all()
    if not recipes:
        print("No recipes found.")
        return
    for recipe in recipes:
        print(recipe)
    
def search_by_ingredients():
    if session.query(Recipe).count() == 0:
        print("No recipes found.")
        return

    results = session.query(Recipe.ingredients).all()
    all_ingredients = []
    for result in results:
        ingredients = result[0].split(", ")
        for ingredient in ingredients:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)

    for i, ingredient in enumerate(all_ingredients):
        print(f"{i + 1}. {ingredient}")

    selections = input("Select ingredients by numbers (separated by spaces): ").split()
    search_ingredients = [all_ingredients[int(i) - 1] for i in selections]
    conditions = [Recipe.ingredients.like(f"%{ingredient}%") for ingredient in search_ingredients]

    recipes = session.query(Recipe).filter(*conditions).all()
    if not recipes:
        print("No recipes found with these ingredients.")
    else:
        for recipe in recipes:
            print(recipe)
    
def edit_recipe():
    recipes = session.query(Recipe.id, Recipe.name).all()
    if not recipes:
        print("No recipes to edit.")
        return

    for recipe in recipes:
        print(f"{recipe.id}. {recipe.name}")

    recipe_id = input("Select a recipe to edit by ID: ")
    recipe_to_edit = session.query(Recipe).get(recipe_id)

    if not recipe_to_edit:
        print("Recipe not found.")
        return

    print("1. Name")
    print("2. Ingredients")
    print("3. Cooking Time")
    choice = input("What would you like to edit? ")

    if choice == "1":
        recipe_to_edit.name = input("Enter new name: ")
    elif choice == "2":
        num_ingredients = int(input("How many ingredients? "))
        ingredients = []
        for i in range(num_ingredients):
            ingredient = input(f"Enter ingredient {i + 1}: ")
            ingredients.append(ingredient)
        recipe_to_edit.ingredients = ", ".join(ingredients)
    elif choice == "3":
        recipe_to_edit.cooking_time = int(input("Enter new cooking time: "))

    recipe_to_edit.calculate_difficulty()
    session.commit()
    print("Recipe updated.")

def delete_recipe():
    recipes = session.query(Recipe.id, Recipe.name).all()
    if not recipes:
        print("No recipes to delete.")
        return

    for recipe in recipes:
        print(f"{recipe.id}. {recipe.name}")

    recipe_id = input("Enter recipe ID to delete: ")
    recipe_to_delete = session.query(Recipe).get(recipe_id)

    if recipe_to_delete:
        confirmation = input(f"Are you sure you want to delete {recipe_to_delete.name}? (yes/no): ")
        if confirmation.lower() == "yes":
            session.delete(recipe_to_delete)
            session.commit()
            print("Recipe deleted.")
        else:
            print("Deletion cancelled.")
    
def main_menu():
    while True:
        print("\nRecipe Manager")
        print("1. Create a new recipe")
        print("2. View all recipes")
        print("3. Search for recipes by ingredients")
        print("4. Edit a recipe")
        print("5. Delete a recipe")
        print("Type 'quit' to exit.")

        choice = input("Enter your choice: ").lower()

        if choice == '1':
            create_recipe()
        elif choice == '2':
            view_all_recipes()
        elif choice == '3':
            search_by_ingredients()
        elif choice == '4':
            edit_recipe()
        elif choice == '5':
            delete_recipe()
        elif choice == 'quit':
            session.close()
            engine.dispose()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()