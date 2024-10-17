import pandas as pd
from typing import List, Tuple

# Вхідні дані
demand_probability: List[float] = [0.3, 0.6, 0.1]
demand: List[int] = [10, 15, 20]
production_costs: int = 1500
selling_price: int = 2400
fine: int = 1400

# Обсяги виробництва
productions: List[int] = [10, 15, 20]

# Функція для розрахунку продажу, незадоволеного попиту та прибутку
def calculate_sales_and_profit(production: int) -> Tuple[List[int], List[int], List[int], List[float], List[float]]:
    sold_amount: List[int] = [min(production, d) for d in demand]
    not_sold_amount: List[int] = [production - sold for sold in sold_amount]
    unsatisfied_demand: List[int] = [max(d - production, 0) for d in demand]

    pure_profit: List[float] = [
        sold * (selling_price - production_costs) - production_costs * not_sold
        for sold, not_sold in zip(sold_amount, not_sold_amount)
    ]

    impure_profit: List[float] = [
        sold * (selling_price - production_costs) - production_costs * not_sold - unsatisfied * fine
        for sold, not_sold, unsatisfied in zip(sold_amount, not_sold_amount, unsatisfied_demand)
    ]

    return sold_amount, not_sold_amount, unsatisfied_demand, pure_profit, impure_profit

# Виведення результатів для кожного обсягу виробництва
for production in productions:
    sold_amount, not_sold_amount, unsatisfied_demand, pure_profit, impure_profit = calculate_sales_and_profit(production)

    # Створення DataFrame для відображення результатів
    data = {
        "Попит": demand,
        "Продано": sold_amount,
        "Не продано": not_sold_amount,
        "Незадов. попит": unsatisfied_demand,
    }
    
    df = pd.DataFrame(data)

    print(f'Обсяг виробництва в {production} тон:')
    print(df.to_string(index=False))  # Виводить таблицю без індексів
    print("\n" + "-" * 40 + "\n")  # Розділювач для кращої читаємості

    # Розрахунок нормованого доходу
    normalized_pure_income: float = sum(prob * profit for prob, profit in zip(demand_probability, pure_profit))
    normalized_impure_income: float = sum(prob * profit for prob, profit in zip(demand_probability, impure_profit))

    print(f'Можливий чистий прибуток: {round(normalized_pure_income, 2)}')
    print(f'Можливий дохід з урахуванням незадоволеного попиту: {round(normalized_impure_income, 2)}\n')
