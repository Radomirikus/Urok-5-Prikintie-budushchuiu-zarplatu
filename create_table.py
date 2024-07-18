from superjob import get_superjob_statistic
from hh import get_HH_statistic
from terminaltables import AsciiTable
from dotenv import load_dotenv
import os

def create_beautiful_table(statistics):
    vacancies_table = [
        ['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата']
    ]
    for language, statistic in statistics.items():
        vacancies_table.append([
            language,
            statistic['vacancies_found'],
            statistic['vacancies_processed'],
            statistic['average_salary']
        ])
    
    table = AsciiTable(vacancies_table)
    print(table.table)

load_dotenv()
super_secret_key = os.getenv("SUPER_SECRET_KEY")

superjob_statistic = get_superjob_statistic(super_secret_key)
hh_statistic = get_HH_statistic()
create_beautiful_table(superjob_statistic)
create_beautiful_table(hh_statistic)