# Оцінки адвокатів за критеріями
lawyers = [
    [85, 30, 22, 0.65, 6],
    [60, 20, 10, 0.6, 7],
    [30, 12, 5, 0.45, 5],
    [75, 24, 13, 0.7, 8],
    [40, 15, 7, 0.55, 7]
]

# Ваги критеріїв
weights = [7, 5, 6, 8, 6]

# Знаходження мінімальних та максимальних значень по кожному стовпцю
mins = [min(col) for col in zip(*lawyers)]
maxs = [max(col) for col in zip (*lawyers)]

# Нормалізація оцінок за кожним критерієм
normalized_lawyers = []
for lawyer in lawyers:
    normalized_lawyer = [(x - min_val) / (max_val - min_val) for x, min_val, max_val in zip(lawyer, mins, maxs)]
    normalized_lawyers.append(normalized_lawyer)

# Нормалізація значень стовпця 1 по спеціальній формулі
for i in range(len(lawyers)):
    normalized_lawyers[i][1] = (maxs[1] - lawyers[i][1]) / (maxs[1] - mins[1])

# Обчислення загальної оцінки для кожного адвоката
total_score = [sum(value * weight for value, weight in zip(lawyer, weights)) for lawyer in normalized_lawyers]

candidates_names = ['A1', 'A2', 'A3', 'A4', 'A5']

# Визначення найкращого адвоката
best_lawyer_index = total_score.index(max(total_score)) 
best_lawyer_score = max(total_score)
best_lawyer = candidates_names [best_lawyer_index]

print(f"Найкращий адвокат: {best_lawyer}")
print(f"Загальна оцінка: {best_lawyer_score}")