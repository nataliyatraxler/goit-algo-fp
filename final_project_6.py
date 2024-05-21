def greedy_algorithm(items, budget):
    # Сортування страв за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    
    total_calories = 0
    total_cost = 0
    selected_items = []
    
    for item, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            selected_items.append(item)
            total_cost += info["cost"]
            total_calories += info["calories"]
    
    return selected_items, total_calories, total_cost

def dynamic_programming(items, budget):
    n = len(items)
    item_list = list(items.items())
    
    # Створення таблиці для динамічного програмування
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        name, info = item_list[i - 1]
        cost, calories = info["cost"], info["calories"]
        
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Визначення обраних страв
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name, info = item_list[i - 1]
            selected_items.append(name)
            w -= info["cost"]
    
    total_calories = dp[n][budget]
    total_cost = budget - w
    
    return selected_items, total_calories, total_cost

# Дані про страви
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

# Жадібний алгоритм
greedy_selected_items, greedy_total_calories, greedy_total_cost = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Обрані страви:", greedy_selected_items)
print("Загальна калорійність:", greedy_total_calories)
print("Загальна вартість:", greedy_total_cost)

# Динамічне програмування
dp_selected_items, dp_total_calories, dp_total_cost = dynamic_programming(items, budget)
print("\nДинамічне програмування:")
print("Обрані страви:", dp_selected_items)
print("Загальна калорійність:", dp_total_calories)
print("Загальна вартість:", dp_total_cost)
