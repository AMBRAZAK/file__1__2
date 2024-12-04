import os

file_name = "recipes.txt"

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, file_name)
cook_book = {}

with open("recipes.txt", 'r') as f:
    while True:
        dish_name = f.readline().strip()
        if not dish_name:
            break

        ingredients_count = int(f.readline().strip())
        ingredients = []

        for _ in range(ingredients_count):
            ingredient_line = f.readline().strip()
            ingredient_name, quantity, measure = ingredient_line.split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure
            })

        cook_book[dish_name] = ingredients
        f.readline()

print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
        else:
            print(f"Блюдо '{dish}' отсутствует в книге рецептов.")
    return shop_list

result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(result)