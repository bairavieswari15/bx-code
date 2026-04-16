from collections import OrderedDict
supermarket_items = OrderedDict()
n = int(input())
for _ in range(n):
    data = input().rpartition(' ')
    item_name = data[0]
    net_price = int(data[2])
    if item_name in supermarket_items:
        supermarket_items[item_name] += net_price
    else:
        supermarket_items[item_name] = net_price
for item, price in supermarket_items.items():
    print(f"{item} {price}")
