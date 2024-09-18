# Оцінки адвокатів за критеріями
candidates = [
    [3, 7, 2, 9],
    [8, 3, 6, 7],
    [4, 8, 3, 5],
    [9, 6, 5, 4]
]

# Ваги критеріїв
weights = [8, 9, 6, 7]

# Обчислення загальної оцінки для кожного кандидата
total_score = [sum(score * weight for score, weight in zip(candidate, weights)) for candidate in candidates]

candidates_names = ['A1', 'A2', 'A3', 'A4']

# Вибір найкращого кандидата
best_candidate_index = total_score.index(max(total_score))
best_candidate = candidates_names[best_candidate_index]
best_candidate_score = max(total_score)

print(f"Найкращий кандидат: {best_candidate}")
print(f"Загальна оцінка: {best_candidate_score}")
