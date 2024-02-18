def cookbook(*args):
    cookbook_dict = {}
    result = ""
    for recipe_name, cuisine, ingredients in args:
        if cuisine not in cookbook_dict:
            cookbook_dict[cuisine] = []
        cookbook_dict[cuisine].append((recipe_name, ingredients))
        # cookbook_dict[cuisine] += list(ingredients)

    sorted_cookbook_dict = sorted(cookbook_dict.items(), key=lambda x: (-len(x[1]), x[0]))


    for cur_cuisine, cur_recipe in sorted_cookbook_dict:
        result += f"{cur_cuisine} cuisine contains {len(cur_recipe)} recipes:\n"
        sorted_new = sorted(cur_recipe, key=lambda x: x[0])
        for name_recipe, c_ingredients in sorted_new:
            result += f"  * {name_recipe} -> Ingredients: {', '.join(c_ingredients)}\n"
    return result[:-1]


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
print()
print(cookbook(
    ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
    ))
print()
print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))

print(cookbook(
       ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
        ("Chicken Curry", "Indian", ["chicken", "curry paste", "coconut milk", "rice"]),
        ("Caesar Salad", "American", ["romaine lettuce", "croutons", "parmesan", "caesar dressing"]),
        ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
        ("Mushroom Risotto", "Italian", ["arborio rice", "mushrooms", "onion", "parmesan", "broth"]),
        ("Tacos", "Mexican", ["tortillas", "ground beef", "lettuce", "tomato", "cheese"]),
        ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"]),
        ("Chicken Alfredo", "Italian", ["fettuccine", "chicken", "alfredo sauce", "broccoli"]))
)

#        expected = """Italian cuisine contains 3 recipes:
#   * Chicken Alfredo -> Ingredients: fettuccine, chicken, alfredo sauce, broccoli
#   * Mushroom Risotto -> Ingredients: arborio rice, mushrooms, onion, parmesan, broth
#   * Spaghetti Bolognese -> Ingredients: spaghetti, tomato sauce, ground beef
# American cuisine contains 1 recipes:
#   * Caesar Salad -> Ingredients: romaine lettuce, croutons, parmesan, caesar dressing
# Indian cuisine contains 1 recipes:
#   * Chicken Curry -> Ingredients: chicken, curry paste, coconut milk, rice
# Japanese cuisine contains 1 recipes:
#   * Sushi Rolls -> Ingredients: rice, nori, fish, vegetables
# Mexican cuisine contains 1 recipes:
#   * Tacos -> Ingredients: tortillas, ground beef, lettuce, tomato, cheese
# Thai cuisine contains 1 recipes:
#   * Pad Thai -> Ingredients: rice noodles, shrimp, peanuts, bean sprouts, tamarind sauce"""
