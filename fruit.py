#variable fruit for user input/use .lower() to make case insensitive.
fruit = input().lower()

#define a funtion using dictionary/branching to acieve desired outcome.
def findcalorie(fruit):
    calories = {
        'apple':130,
        'avocado':50,
        'banana': 110,
        'cantaloupe': 50,
        'grapefruit': 60,
        'grapes': 90,
        'honeydew melon':50,
        'kiwi fruit': 90,
        'lemon': 15,
        'lime': 20,
        'nectarine': 60,
        'orange': 80,
        'peach': 60,
        'pear': 100,
        'pineapple': 50,
        'plums':70,
        'strawberries': 50,
        'sweet cherries': 100,
        'tangerine': 50,
        'watermelon': 80
    }

    if fruit in calories:
        print('Calories:',calories[fruit])
    else:
        print(f'calories not found for: {fruit}')

#call function
findcalorie(fruit)