import requests
from dotenv import load_dotenv
import os


def predict_rub_salary_sj(payment_from, payment_to):
    if payment_from and payment_to:
        return payment_from + payment_to / 2

    elif payment_from:
        return payment_from * 1.2

    else:
        return payment_to * 0.8


def get_superjob_statistic(super_secret_key):
    secret_key = super_secret_key
    url = 'https://api.superjob.ru/2.0/vacancies/'
    languages = ["python", "java", "javascript", "c++", "c#", "TypeScript", "Swift", "Scala"]
    headers = {'X-Api-App-Id' : secret_key}
    superjob_statistics = {}
    for language in languages:    
        vacancies_processed = 0
        sj_salary_sum = 0
        for page in range(5):
            params = {
                'catalogues' : 48,
                'town' : 4,
                'page' : page,
                'count' : 100,
                'keyword' : language
            }
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            vacancies = response.json()['objects']
            
            for vacancy in vacancies:
                if vacancy['currency'] == 'rub' and (vacancy['payment_from'] or vacancy['payment_to']):
                    vacancies_processed += 1
                    sj_salary_sum += predict_rub_salary_sj(vacancy['payment_from'], vacancy['payment_to'])
                
        try:
            average_salary = sj_salary_sum / vacancies_processed
        except ZeroDivisionError:
            average_salary = 0
        superjob_statistics[language] = {
            'vacancies_found' : response.json()['total'],
            'vacancies_processed' : vacancies_processed,
            'average_salary' : average_salary
        }
    
    return superjob_statistics