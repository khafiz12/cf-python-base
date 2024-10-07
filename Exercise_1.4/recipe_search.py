for recipe in recipes_list:
     ...:             if ingredient_searched in recipe['ingredients']:
     ...:                 display_recipe(recipe)
     ...:                 recipes_found += 1
     ...: 
     ...:         if recipes_found == 0:
     ...:             print(f"\nNo recipes found with the ingredient: {ingredient_searched}")
     ...: 
     ...: # Main code
     ...: filename = input("Enter the filename containing your recipe data: ")
     ...: 
     ...: try:
     ...:     # Try to open the binary file and load its content
     ...:     with open(filename, 'rb') as file:
     ...:         data = pickle.load(file)
     ...: 
     ...: except FileNotFoundError:
     ...:     # Warn the user if the file is not found
     ...:     print(f"File '{filename}' not found. Please check the filename and try again.")
     ...: 
     ...: else:
     ...:     # Call the search_ingredient function with the loaded data
     ...:     search_ingredient(data)
     ...: 
