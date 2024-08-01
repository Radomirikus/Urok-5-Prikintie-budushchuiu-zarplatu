import requests
from dotenv import load_dotenv
import os
from hh import predict_rub_salary
from itertools import count

def get_superjob_statistic(super_secret_key):
    url = 'https://api.superjob.ru/2.0/vacancies/'
    languages = ["python", "java", "javascript", "c++", "c#", "TypeScript", "Swift", "Scala"]
    headers = {'X-Api-App-Id' : super_secret_key}
    superjob_statistics = {}
    for language in languages:    
        vacancies_processed = 0
        sj_salary_sum = 0
        profession_id = 48
        town = 4
        max_result = 100
        for page in count(0, 1):
            params = {
                'catalogues' : profession_id,
                'town' : town,
                'page' : page,
                'count' : max_result,
                'keyword' : language
            }
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            answer = response.json()
            vacancies = answer['objects']
            if not answer['more']:
                break
            
            for vacancy in vacancies:
                if vacancy['currency'] == 'rub' and (vacancy['payment_from'] or vacancy['payment_to']):
                    vacancies_processed += 1
                    sj_salary_sum += predict_rub_salary(vacancy['payment_from'], vacancy['payment_to'])
                
        try:
            average_salary = sj_salary_sum / vacancies_processed
        except ZeroDivisionError:
            average_salary = 0
        superjob_statistics[language] = {
            'vacancies_found' : answer['total'],
            'vacancies_processed' : vacancies_processed,
            'average_salary' : average_salary
        }
    
    return superjob_statistics