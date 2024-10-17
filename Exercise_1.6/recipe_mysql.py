import mysql.connector

# Step 1: Establish connection to MySQL
try:
    conn = mysql.connector.connect(
        host="localhost",      # Hostname (usually localhost)
        user="cf-python",      # Username you created earlier
        password="password"    # Password you set for the user
    )
    print("Connected to MySQL server successfully!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit()

# Step 2: Initialize cursor
cursor = conn.cursor()

# Step 3: Create the database (if not exists)
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

# Step 4: Access the database
cursor.execute("USE task_database")

# Step 5: Create the Recipes table (if not exists)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Recipes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        ingredients VARCHAR(255),
        cooking_time INT,
        difficulty VARCHAR(20)
    )
""")


# Function to create a new recipe
def create_recipe(conn, cursor):
    # Get input from the user for the recipe details
    name = input("Enter the recipe name: ")
    ingredients = input("Enter the ingredients (comma-separated): ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    difficulty = input("Enter the difficulty level (Easy, Medium, Intermediate, Hard): ")

    # SQL query to insert a new recipe into the Recipes table
    query = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
    values = (name, ingredients, cooking_time, difficulty)
    cursor.execute(query, values)
    conn.commit()
    print("Recipe added successfully!\n")

# Function to search for a recipe by ingredient
def search_recipe(conn, cursor):
    ingredient = input("Enter the ingredient to search for: ")
    query = "SELECT * FROM Recipes WHERE ingredients LIKE %s"
    cursor.execute(query, ('%' + ingredient + '%',))
    results = cursor.fetchall()

    if results:
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Ingredients: {row[2]}, Cooking Time: {row[3]} minutes, Difficulty: {row[4]}")
    else:
        print("No recipes found with that ingredient.\n")

# Function to update an existing recipe
def update_recipe(conn, cursor):
    recipe_id = int(input("Enter the ID of the recipe you want to update: "))
    new_name = input("Enter the new recipe name (leave blank to keep the same): ")
    new_ingredients = input("Enter the new ingredients (leave blank to keep the same): ")
    new_cooking_time = input("Enter the new cooking time (leave blank to keep the same): ")
    new_difficulty = input("Enter the new difficulty level (leave blank to keep the same): ")

    # Build the update query dynamically based on the fields the user wants to update
    updates = []
    if new_name:
        updates.append(f"name = '{new_name}'")
    if new_ingredients:
        updates.append(f"ingredients = '{new_ingredients}'")
    if new_cooking_time:
        updates.append(f"cooking_time = {new_cooking_time}")
    if new_difficulty:
        updates.append(f"difficulty = '{new_difficulty}'")

    if updates:
        query = f"UPDATE Recipes SET {', '.join(updates)} WHERE id = {recipe_id}"
        cursor.execute(query)
        conn.commit()
        print("Recipe updated successfully!\n")
    else:
        print("No changes made.\n")

# Function to delete a recipe
def delete_recipe(conn, cursor):
    recipe_id = int(input("Enter the ID of the recipe you want to delete: "))
    cursor.execute("DELETE FROM Recipes WHERE id = %s", (recipe_id,))
    conn.commit()
    print("Recipe deleted successfully!\n")

# Main menu function
def main_menu(conn, cursor):
    while True:
        print("Main Menu:")
        print("1. Add a new recipe")
        print("2. Search for a recipe by ingredient")
        print("3. Update an existing recipe")
        print("4. Delete a recipe")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            create_recipe(conn, cursor)
        elif choice == '2':
            search_recipe(conn, cursor)
        elif choice == '3':
            update_recipe(conn, cursor)
        elif choice == '4':
            delete_recipe(conn, cursor)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Main code block to connect to the database and start the menu
if __name__ == "__main__":
    try:
        conn = mysql.connector.connect(
            host="localhost",     # Hostname
            user="cf-python",     # Username you created earlier
            password="password",  # Password
            database="task_database"  # The database you created earlier
        )
        cursor = conn.cursor()

        # Call the main menu function
        main_menu(conn, cursor)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close the connection when the program exits
        cursor.close()
        conn.close()
        print("Database connection closed.")

def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        return "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        return "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        return "Intermediate"
    elif cooking_time >= 10 and len(ingredients) >= 4:
        return "Hard"

def create_recipe(conn, cursor):
    # Collect recipe details
    name = input("Enter the recipe name: ")
    cooking_time = int(input("Enter the cooking time in minutes: "))
    ingredients = input("Enter the ingredients (comma-separated): ").split(", ")

    # Calculate difficulty
    difficulty = calculate_difficulty(cooking_time, ingredients)

    # Convert ingredients list to a comma-separated string
    ingredients_str = ", ".join(ingredients)

    # Insert into database
    cursor.execute("""
        INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) 
        VALUES (%s, %s, %s, %s)
    """, (name, ingredients_str, cooking_time, difficulty))
    
    conn.commit()
    print("Recipe added successfully!")

def search_recipe(conn, cursor):
    # Fetch all ingredients
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()
    
    # Extract unique ingredients
    all_ingredients = set()
    for row in results:
        ingredients_list = row[0].split(", ")
        all_ingredients.update(ingredients_list)
    
    # Display ingredients
    all_ingredients = list(all_ingredients)
    print("Available ingredients:")
    for i, ingredient in enumerate(all_ingredients, 1):
        print(f"{i}. {ingredient}")
    
    # User selects an ingredient
    choice = int(input("Select an ingredient number to search: ")) - 1
    search_ingredient = all_ingredients[choice]
    
    # Search for recipes with that ingredient
    query = "SELECT * FROM Recipes WHERE ingredients LIKE %s"
    cursor.execute(query, ("%" + search_ingredient + "%",))
    results = cursor.fetchall()
    
    # Display results
    if results:
        for recipe in results:
            print(f"ID: {recipe[0]}, Name: {recipe[1]}, Ingredients: {recipe[2]}, Cooking Time: {recipe[3]} mins, Difficulty: {recipe[4]}")
    else:
        print("No recipes found with that ingredient.")
    
def update_recipe(conn, cursor):
    # Fetch and display all recipes
    cursor.execute("SELECT * FROM Recipes")
    recipes = cursor.fetchall()
    for recipe in recipes:
        print(f"ID: {recipe[0]}, Name: {recipe[1]}, Cooking Time: {recipe[3]} mins, Difficulty: {recipe[4]}")
    
    # Select recipe to update
    recipe_id = int(input("Enter the ID of the recipe to update: "))
    
    # Select column to update
    column = input("Which column would you like to update? (name/cooking_time/ingredients): ").lower()
    
    # Update the chosen column
    if column == "name":
        new_value = input("Enter the new name: ")
        cursor.execute("UPDATE Recipes SET name = %s WHERE id = %s", (new_value, recipe_id))
    elif column == "cooking_time":
        new_value = int(input("Enter the new cooking time in minutes: "))
        cursor.execute("UPDATE Recipes SET cooking_time = %s WHERE id = %s", (new_value, recipe_id))
        
        # Recalculate difficulty
        cursor.execute("SELECT ingredients FROM Recipes WHERE id = %s", (recipe_id,))
        ingredients = cursor.fetchone()[0].split(", ")
        difficulty = calculate_difficulty(new_value, ingredients)
        cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (difficulty, recipe_id))
    elif column == "ingredients":
        new_value = input("Enter the new ingredients (comma-separated): ").split(", ")
        ingredients_str = ", ".join(new_value)
        cursor.execute("UPDATE Recipes SET ingredients = %s WHERE id = %s", (ingredients_str, recipe_id))
        
        # Recalculate difficulty
        cursor.execute("SELECT cooking_time FROM Recipes WHERE id = %s", (recipe_id,))
        cooking_time = cursor.fetchone()[0]
        difficulty = calculate_difficulty(cooking_time, new_value)
        cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (difficulty, recipe_id))
    
    conn.commit()
    print("Recipe updated successfully!")

def delete_recipe(conn, cursor):
    # Fetch and display all recipes
    cursor.execute("SELECT * FROM Recipes")
    recipes = cursor.fetchall()
    for recipe in recipes:
        print(f"ID: {recipe[0]}, Name: {recipe[1]}")
    
    # Select recipe to delete
    recipe_id = int(input("Enter the ID of the recipe to delete: "))
    
    # Delete the selected recipe
    cursor.execute("DELETE FROM Recipes WHERE id = %s", (recipe_id,))
    conn.commit()
    print("Recipe deleted successfully!")

def main_menu(conn, cursor):
    while True:
        print("\nMain Menu:")
        print("1. Add a new recipe")
        print("2. Search for a recipe by ingredient")
        print("3. Update an existing recipe")
        print("4. Delete a recipe")
        print("5. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(conn, cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
    
    # Close the connection after exiting
    conn.close()

conn = mysql.connector.connect(host="localhost", user="root", password="password", database="recipes_db")
cursor = conn.cursor()
