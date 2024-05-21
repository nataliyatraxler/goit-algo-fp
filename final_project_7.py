import random
import matplotlib.pyplot as plt

# Функція для імітації кидків двох кубиків
def simulate_dice_rolls(num_rolls):
    sum_counts = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        roll_sum = roll1 + roll2
        sum_counts[roll_sum] += 1
    
    return sum_counts

# Функція для обчислення ймовірностей
def calculate_probabilities(sum_counts, num_rolls):
    probabilities = {sum_val: count / num_rolls for sum_val, count in sum_counts.items()}
    return probabilities

# Кількість імітацій
num_rolls = 1000000

# Імітація кидків кубиків
sum_counts = simulate_dice_rolls(num_rolls)

# Обчислення ймовірностей
probabilities = calculate_probabilities(sum_counts, num_rolls)

# Аналітичні ймовірності
analytical_probabilities = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36
}

# Виведення результатів
print("Результати імітації:")
for sum_val, prob in probabilities.items():
    print(f"Сума: {sum_val}, Імовірність: {prob:.4%} ({sum_counts[sum_val]}/{num_rolls})")

print("\nАналітичні ймовірності:")
for sum_val, prob in analytical_probabilities.items():
    print(f"Сума: {sum_val}, Імовірність: {prob:.4%} ({prob * num_rolls:.0f}/{num_rolls})")

# Побудова графіку
sums = list(probabilities.keys())
simulated_probs = list(probabilities.values())
analytical_probs = [analytical_probabilities[sum_val] for sum_val in sums]

plt.figure(figsize=(10, 6))
plt.plot(sums, simulated_probs, 'o-', label='Імітаційні ймовірності')
plt.plot(sums, analytical_probs, 's-', label='Аналітичні ймовірності')
plt.xlabel('Сума')
plt.ylabel('Імовірність')
plt.title('Порівняння ймовірностей сум при киданні двох кубиків')
plt.legend()
plt.grid(True)
plt.show()
