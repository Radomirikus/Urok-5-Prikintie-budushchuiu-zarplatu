# Сравниваем вакансии программистов
Проект создан для сравнения количества и зароботной платы по вакансиям программиста на разных языках.

## Как установить
Для начала вам нужно зарегистрировать приложение в `Superjob` - [Superjob](https://api.superjob.ru/info/), потом создать .env файл где создать переменную `SUPER_SECRET_KEY` в которую надо записать полученный ключ из `Superjob`.
```
SUPER_SECRET_KEY = 'Ваш ключ приложения'
```
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

## Как запустить
Что-бы проанализировать работы по языкам программирования в терминал напишите:
```
python create_table.py
```
в консоль у вас выведет две таблицы одна по `Superjob` одна по `HeadHunter`.

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org)
