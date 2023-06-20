from src.models.ingredient import Ingredient, restriction_map


def test_ingredient():
    ingredient1 = Ingredient("carne")
    ingredient3 = Ingredient("salmão")

    assert hash(ingredient1) == hash(ingredient1)

    assert hash(ingredient1) != hash(ingredient3)

    assert ingredient1 == ingredient1

    assert ingredient1 != ingredient3

    assert ingredient1.name == "carne"

    assert ingredient1.restrictions == restriction_map().get("carne", set())

    assert repr(ingredient1) == "Ingredient('carne')"
