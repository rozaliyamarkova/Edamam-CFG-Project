import requests
from app_id_and_key import app_id, app_key


def recipe_search(ingredient):
    result = requests.get(
    'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient,app_id,app_key))
    data = result.json()
    return data['hits']

def run():
    ingredient_choice = input("Enter one or more ingredients you want to use (separated by commas): ")
    while ingredient_choice == "":
        ingredient_choice = input("Please enter at least one ingredient: ") # Asks user repeatedly until they enter at least one ingredient
    
    ingredients = [ingredient.strip() for ingredient in ingredient_choice.split(",")]
    results = recipe_search(ingredients)

    if not results:
        print("Sorry, no recipes were found for this criteria.") # If no recipes are found, this message gets printed and the program ends
        return
    
    print("Here are your recipes: \n")
    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['url'])
        
        print()

run()