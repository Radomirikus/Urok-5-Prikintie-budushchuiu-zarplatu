import requests
from itertools import count

def predict_rub_salary_HH(salary):
    if salary['from'] and salary['to']:
        return salary['from'] + salary['to'] / 2

    elif salary['from']:
        return salary['from'] * 1.2

    else:
        return salary['to'] * 0.8


def get_HH_statistic():
    languages_statistic = {}
    url = "https://api.hh.ru/vacancies"
    languages = ["python", "java", "javascript", "c++", "c#", "TypeScript", "Swift", "Scala"]
    
    for language in languages:
        vacancies_processed = 0
        salary_sum = 0
        for page in count(0, 1):
            payload = {
                "text" : language,
                "area" : 1,
                "page" : page,
                "per_page" : 100
            }
            response = requests.get(url, params=payload)
            response.raise_for_status()
            if page >= response.json()['pages'] - 1:
                break
            for vacancy in response.json()['items']:
                salary = vacancy['salary']
                if salary is not None and salary['currency'] == 'RUR':
                    predict_rub_salary_HH(salary)
                    vacancies_processed += 1
                    salary_sum += predict_rub_salary_HH(salary)
    
        average_salary = salary_sum / vacancies_processed
        languages_statistic[language] = {
            "vacancies_found" : response.json()['found'],
            "vacancies_processed" : vacancies_processed,
            "average_salary" : average_salary
        }
        
    return languages_statistic