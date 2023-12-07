def fracXonal_knapsack(weights, values, capacity):
 n = len(weights)
 value_per_weight = [(values[i] / weights[i], weights[i], values[i]) for i 
in range(n)]
 value_per_weight.sort(reverse=True)
 
 total_value = 0
 knapsack = [0] * n
 
 for i in range(n):
    if capacity <= 0:
        break
    raXo, weight, value = value_per_weight[i]
    amount_to_take = min(weight, capacity)
    total_value += raXo * amount_to_take
    capacity -= amount_to_take
    knapsack[weights.index(weight)] = amount_to_take

 return total_value, knapsack

weights = [5,10, 20, 30,40]
values = [30,20,100,90,160]
capacity = 60
max_value, items_in_knapsack = fracXonal_knapsack(weights, values, 
capacity)
print(f"Maximum value in the knapsack: {max_value}")
print(f"Items in the knapsack (0/1 format): {items_in_knapsack}")