import asyncio
from inventory import Inventory
from time import sleep


def display_catalogue(catalogue):
    burgers = catalogue["Burgers"]
    sides = catalogue["Sides"]
    drinks = catalogue["Drinks"]

    print("--------- Burgers -----------\n")
    for burger in burgers:
        item_id = burger["id"]
        name = burger["name"]
        price = burger["price"]
        print(f"{item_id}. {name} ${price}")

    print("\n---------- Sides ------------")
    for side in sides:
        sizes = sides[side]

        print(f"\n{side}")
        for size in sizes:
            item_id = size["id"]
            size_name = size["size"]
            price = size["price"]
            print(f"{item_id}. {size_name} ${price}")

    print("\n---------- Drinks ------------")
    for beverage in drinks:
        sizes = drinks[beverage]

        print(f"\n{beverage}")
        for size in sizes:
            item_id = size["id"]
            size_name = size["size"]
            price = size["price"]
            print(f"{item_id}. {size_name} ${price}")

    print("\n------------------------------\n")


async def main():
    POSSIBLE_YES_ANSWER = ['yes', 'y', 'ok', 'sure']
    new_inventory = Inventory()
    print('Welcome to the ProgrammingExpert Burger Bar!')
    print('Loading catalogue...')
    display_catalogue(new_inventory.catalogue)

    while True:
        answer = input('Would you like to place an order? ')
        if answer.lower() in POSSIBLE_YES_ANSWER:
            print('Taking order...')
        else:
            print('Okay! Have a nice day!')
            # print('Program terminating in 5 seconds...')
            # for _ in range(5):
            #     print('.')
            #     sleep(1)
            break


if __name__ == "__main__":
    asyncio.run(main())
