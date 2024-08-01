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
    
    table = AsciiTable(vacancies_table).table
    return table



def main():
    load_dotenv()
    superjob_key = os.getenv("SUPER_SECRET_KEY")
    superjob_statistic = get_superjob_statistic(superjob_key)
    hh_statistic = get_HH_statistic()
    print(create_beautiful_table(superjob_statistic))
    print(create_beautiful_table(hh_statistic))


if __name__ == '__main__':
    main()
