def predict_rub_salary(salary):
    if salary['from'] and salary['to']:
        return salary['from'] + salary['to'] / 2

    elif salary['from']:
        return salary['from'] * 1.2

    else:
        return salary['to'] * 0.8