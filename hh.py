import requests
from itertools import count

def predict_rub_salary(salary):
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
        per_page = 100
        town = 1
        for page in count(0, 1):
            payload = {
                "text" : language,
                "area" : town,
                "page" : page,
                "per_page" : per_page
            }
            response = requests.get(url, params=payload)
            response.raise_for_status()
            platform_answer = response.json()
            if page >= platform_answer['pages'] - 1:
                break
            for vacancy in platform_answer['items']:
                salary = vacancy['salary']
                if salary and salary['currency'] == 'RUR':
                    vacancies_processed += 1
                    salary_sum += predict_rub_salary(salary)
    
        average_salary = salary_sum / vacancies_processed
        languages_statistic[language] = {
            "vacancies_found" : platform_answer['found'],
            "vacancies_processed" : vacancies_processed,
            "average_salary" : average_salary
        }
        
    return languages_statistic