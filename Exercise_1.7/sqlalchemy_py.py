class Recipe(Base):
    _tablename_="practice_recipe"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def _repr_(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"
    
    coffee = Recipe(
        name = "Coffee",
        cooking_time = 5,
        ingredients = "Coffee Powder, Sugar, Water"
    )

    cake = Recipe(
        name = "Cake",
        cooking_time = 50,
        ingredients = "Sugar, Butter, Eggs, Vanilla Essence, Flour, Baking Powder, Milk"
    )

     Smoothie = Recipe(
        name = "Banana Smoothie",
        cooking_time = 5,
        ingredients = "Bananas, Milk, Peanut Butter, Sugar, Ice Cubes"
    )
