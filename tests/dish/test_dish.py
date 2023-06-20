from src.models.dish import Dish  # noqa: F401, E261, E501
from models.ingredient import Ingredient
import pytest


def test_dish():
    dish_name = "Brigadeiro"
    dish_price = 2.99

    dish = Dish(dish_name, dish_price)

    assert dish.name == dish_name

    assert repr(dish) == f"Dish('{dish_name}', R${dish_price:.2f})"

    dish2 = Dish(dish_name, dish_price)
    assert dish == dish2
    assert hash(dish) == hash(dish2)

    ingredient1 = Ingredient("manteiga")

    dish.add_ingredient_dependency(ingredient1, 300)

    assert ingredient1 in dish.get_ingredients()

    restrictions = dish.get_restrictions()
    assert len(restrictions) == 2

    dish3 = Dish("Lasanha de Presunto", 15.00)
    assert hash(dish) != hash(dish3)

    with pytest.raises(ValueError):
        Dish("Lasanha de Presunto", -15.55)
