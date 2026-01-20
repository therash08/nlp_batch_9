raw_inventory = ["Laptop:1000", "Mouse:25", "Monitor:300", "Keyboard:50"]


inventory_tuples = [(item.split(':')[0], int(item.split(':')[1]))
                    for item in raw_inventory]

print("Processed Inventory:", inventory_tuples)

prices = [item[1] for item in inventory_tuples]

most_expensive = max(prices)
cheapest = min(prices)

print(f"Most Expensive Price: ${most_expensive}")
print(f"Cheapest Price: ${cheapest}")
