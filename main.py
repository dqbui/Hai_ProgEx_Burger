import asyncio
from unicodedata import category
from inventory import Inventory
# from time import sleep


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
    display_catalogue(await new_inventory.get_catalogue())

    while True:
        answer = input('Would you like to place an order? ')
        if answer.lower() in POSSIBLE_YES_ANSWER:  # repeat indefinitely until the customer says no
            # print('Taking order...')
            print('List of item IDs:', list(new_inventory.stock.keys()))
            print('Please enter the number of items that you would like to add to your order. Enter q to complete your order.')
            order_list = []
            while True:  # validates customer input is within catalog keys
                order_item = input('Enter an item number: ')
                if order_item.lower() == 'q':
                    break
                else:
                    try:
                        order_item = int(order_item)
                        if order_item not in new_inventory.stock.keys():
                            print('Please enter a valid choice!!!')

                        else:
                            order_list.append(order_item)
                    except ValueError:
                        print('Please enter a valide choice!!!')

            # print(f'Final list of order: {order_list}')
            print(f'Total item count: {len(order_list)}')
            print('Placing order...')

            # attempt to decrement stock; if successful, add to final order; if unsuccessful, remove item from order
            task_list = []
            for item in order_list:
                new_task = new_inventory.decrement_stock(item)
                task_list.append(new_task)

            item_status = await asyncio.gather(*task_list)

            final_order = []

            for idx, avail_bool in enumerate(item_status):
                if avail_bool == True:
                    print('Item added successfully!')
                    final_order.append(order_list[idx])

                else:
                    print(
                        f'Unfortunately item number {order_list[idx]} is out of stock and has been removed from your order. Sorry!')

            # create combo
            print(f'The order so far: {final_order}')

            # boogey final order for debugging
            final_order = [1, 2, 3, 9, 10, 12, 17, 18, 19]

            burgers_list = []
            sides_list = []
            drinks_list = []

            for item_id in final_order:
                if new_inventory.items[item_id]['category'] == 'Burgers':
                    burgers_list.append(item_id)
                elif new_inventory.items[item_id]['category'] == 'Sides':
                    sides_list.append(item_id)
                elif new_inventory.items[item_id]['category'] == 'Drinks':
                    drinks_list.append(item_id)

            print('Burgers init:', burgers_list)
            print('Sides init:', sides_list)
            print('Drinks init:', drinks_list)

            burgers_list.sort(
                key=lambda item_id: new_inventory.items[item_id]['price'])

            sides_list.sort(
                key=lambda item_id: new_inventory.items[item_id]['price'])

            drinks_list.sort(
                key=lambda item_id: new_inventory.items[item_id]['price'])

            print('Burgers sorted:', burgers_list)
            print('Sides sorted:', sides_list)
            print('Drinks sorted:', drinks_list)

            combo_count = min(len(burgers_list),
                              len(sides_list),
                              len(drinks_list))

            order_summary = []

            # first add combo as lists
            for combo in range(combo_count):
                combo_burger = burgers_list.pop()
                combo_side = sides_list.pop()
                combo_drink = drinks_list.pop()

                combo = [combo_burger, combo_side, combo_drink]
                print('Combo', combo)
                order_summary.append(combo)

            # add remaining as individual items
            order_summary.extend(burgers_list)
            order_summary.extend(sides_list)
            order_summary.extend(drinks_list)

            print(order_summary)

            # calculate net price, total price

            # display order details and get final comfirmation

        else:
            print('Okay! Have a nice day!')
            # print('Program terminating in 5 seconds...')
            # for _ in range(5):
            #     print('.')
            #     await asyncio.sleep(1)
            break


if __name__ == "__main__":
    asyncio.run(main())
