# Step 1: Initialize two empty lists
recipes_list = []
ingredients_list = []

# Step 2: Define a function to take recipe input from the user
def take_recipe():
    name = input("Enter the recipe name: ")  # Input recipe name
    cooking_time = int(input("Enter the cooking time (in minutes): "))  # Input cooking time
    ingredients = input("Enter the ingredients (comma-separated): ").split(',')  # Input ingredients list
    ingredients = [ingredient.strip() for ingredient in ingredients]  # Strip extra spaces

    # Create the recipe dictionary
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }

    return recipe

# Step 3: Ask the user how many recipes they want to enter
n = int(input("How many recipes would you like to enter? "))

# Step 4: Run a loop to take multiple recipes from the user
for _ in range(n):
    recipe = take_recipe()  # Call the take_recipe function

    # Step 5: Add new ingredients to ingredients_list if they don't already exist
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)

    # Append the recipe to recipes_list
    recipes_list.append(recipe)

# Step 6: Define the logic to determine recipe difficulty and display recipes
for recipe in recipes_list:
    cooking_time = recipe['cooking_time']
    num_ingredients = len(recipe['ingredients'])

    # Determine difficulty based on the logic provided
    if cooking_time < 10 and num_ingredients < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = "Intermediate"
    else:
        difficulty = "Hard"

    # Display the recipe details
    print(f"\nRecipe: {recipe['name']}")
    print(f"Cooking time: {cooking_time} minutes")
    print(f"Ingredients: {', '.join(recipe['ingredients'])}")
    print(f"Difficulty level: {difficulty}")

# Step 7: Display all ingredients in alphabetical order
print("\nAll ingredients across all recipes (sorted alphabetically):")
for ingredient in sorted(set(ingredients_list)):
    print(f"- {ingredient}")