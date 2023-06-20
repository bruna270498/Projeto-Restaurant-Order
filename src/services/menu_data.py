import csv
from src.models.ingredient import Ingredient
from src.models.dish import Dish


class MenuData:

    def __init__(self, source_path: str) -> None:
        self.load_data_from_file(source_path)

    def load_data_from_file(self, source_path: str):
        with open(source_path, 'r') as file:
            text = csv.DictReader(file)
            data = list(text)

        dict = {}
        self.dishes = set()
        for row in data:
            name = row['dish']
            price = float(row['price'])

            if name not in dict:
                dish = Dish(name, price)
                dict[name] = dish
                self.dishes.add(dish)
            else:
                dish = dict[name]

            ingredient = Ingredient(row['ingredient'])

            dish.add_ingredient_dependency(
                ingredient, int(row['recipe_amount']))
