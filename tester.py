from inventory import Inventory
import asyncio


# new_inventory = Inventory()

# print(new_inventory.items)


# ID_list = list(new_inventory.stock.keys())

# print('List of item IDs:', ID_list)

# print(new_inventory.items)

# for item_ID in ID_list:
#     print('Item ID:', item_ID)
#     print(new_inventory.items[item_ID])
#     print(f'Stock: {new_inventory.stock[item_ID]}')
#     print('---')


# async def main():
#     # print(await new_inventory.get_catalogue())
#     #
#     # for item_ID in ID_list:
#     #     print(await new_inventory.get_item(item_ID))

#     task_list = []
#     for item_ID in ID_list:
#         task_list.append(new_inventory.get_item(item_ID))
#     stock_list = await asyncio.gather(*task_list)
#     for item in stock_list:
#         print(item)

#     # for item_ID in ID_list:
#     #     print(f'Item {item_ID} stock: {stock_list[item_ID-1]}')

#     # await asyncio.sleep(1)
#     # print('Taking stuff out')

#     # task_list = []
#     # for item_ID in range(1, 6):
#     #     task_list.append(new_inventory.decrement_stock(item_ID))
#     # final_stock = await asyncio.gather(*task_list)

#     # print(final_stock)
#     # print('Rechecking stock')

#     # task_list = []
#     # for item_ID in ID_list:
#     #     task_list.append(new_inventory.get_stock(item_ID))
#     # stock_list = await asyncio.gather(*task_list)

#     # for item_ID in ID_list:
#     #     print(f'Item {item_ID} stock: {stock_list[item_ID-1]}')


# asyncio.run(main())


list1 = [1, 2, 3]
list2 = []

list1.extend(list1)

print(list1)
