# Exercise 1.1: Adding Two Numbers in Python

This exercise includes:
- A Python script (`add.py`) that adds two user-inputted numbers.
- A `requirements.txt` file to install necessary packages.
- Screenshots demonstrating the steps involved in this exercise.
- A learning journal documenting the learning process.

- # Recipe Collection

## Data Structure Choice

For storing multiple recipes, I chose a **list of dictionaries** as the data structure. Each recipe is represented by a dictionary containing the following keys:
- `name`: The name of the recipe.
- `cooking_time`: The time required to cook the recipe.
- `ingredients`: A list of ingredients required for the recipe.

This approach ensures that recipes can be accessed sequentially, easily added, modified, or removed. A list maintains the order of recipes, while dictionaries allow us to label key properties of each recipe for clarity and efficient data retrieval. This structure is scalable and flexible for future modifications.
## Instructions to Run:
1. Clone the repo and navigate to the `Exercise 1.1` folder.
2. Install the required packages using `pip install -r requirements.txt`.
3. Run the script `add.py` using Python:
   ```bash
   python add.py

   
