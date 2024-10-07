 all_ingredients = data['all_ingredients']
     ...: 
     ...: # Ask how many recipes the user wants to enter
     ...: n = int(input("How many recipes would you like to enter? "))
     ...: 
     ...: # For loop to gather recipes and ingredients
     ...: for _ in range(n):
     ...:     recipe = take_recipe()
     ...:     recipes_list.append(recipe)
     ...: 
     ...:     # Inner loop to add ingredients to all_ingredients if not already there
     ...:     for ingredient in recipe['ingredients']:
     ...:         if ingredient not in all_ingredients:
     ...:             all_ingredients.append(ingredient)
     ...: 
     ...: # Update the data dictionary with the new recipes and ingredients
     ...: data['recipes_list'] = recipes_list
     ...: data['all_ingredients'] = all_ingredients
     ...: 
     ...: # Write the updated data to the binary file
     ...: with open(filename, 'wb') as file:
     ...:     pickle.dump(data, file)
     ...: 
     ...: print(f"Data saved successfully to {filename}.")