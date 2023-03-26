import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
from pymongo import MongoClient
from pymongo import errors

client = MongoClient('127.0.0.1', 27017)
db_hh = client['user0509']
vacancies = db_hh.vacancies
# vacancies.delete_many({})

headers = {'User-Agent':
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
               '(KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
job_name = input('Введите должность')
url = 'https://hh.ru/'
session = requests.Session()  # работа в режиме 1 сессии
response = session.get('https://hh.ru/search/vacancy?text=' + job_name,
                       headers=headers)  # переход на страницу с должностью с исп. User-Agent
dom_hh = BeautifulSoup(response.text, 'html.parser')  # парсиг страницы с помощью html.parser
print(response)

# count_1 = 0  # счетчик вакансий
# count_2 = 0  # счетчик страниц
articles_list = []
articles_data_hh = {}
while True:
    dom = BeautifulSoup(response.text, 'html.parser')  # парсиг страницы с помощью html.parser
    url_next_page = dom.find('a', {'data-qa': ['pager-next']})  # ссылка на сл.строку
    articles = dom.find_all('div', {'class': 'vacancy-serp-item-body__main-info'})  # все заголовки страницы
    # count_2 += 1
    for article in articles:
        articles_data = {}
        name_vacancy = article.find('a', {
            'data-qa': ['vacancy-serp__vacancy-title']}).text  # поиск по тэгу с заданным ключем и значением
        url_vacancy = article.find('a', {'data-qa': ['vacancy-serp__vacancy-title']}).attrs[
            'href']  # ссылка на вакансию
        pay_txt = article.find('span', {'data-qa': ['vacancy-serp__vacancy-compensation']})
        # count_1 += 1
        if pay_txt is None:  # если ЗП не указана
            pass
        else:
            pay_txt = pay_txt.text.replace('\u202f', '')  # приведение в str без юникода
            pay_list = pay_txt.split()  # привожу в список для будущего условия по выборке цены
            cur_pay_vacancy = pay_list[-1]  # валюта
            articles_data['cur_pay_vacancy'] = cur_pay_vacancy
            if 'от' == pay_list[0]:
                min_pay_vacancy = int(pay_list[1])
                articles_data['max_pay_vacancy'] = None
                articles_data['min_pay_vacancy'] = min_pay_vacancy
            elif 'до' == pay_list[0]:
                max_pay_vacancy = int(pay_list[1])
                articles_data['min_pay_vacancy'] = None
                articles_data['max_pay_vacancy'] = max_pay_vacancy
            else:
                min_pay_vacancy = int(pay_list[0])
                max_pay_vacancy = int(pay_list[2])
                articles_data['min_pay_vacancy'] = min_pay_vacancy
                articles_data['max_pay_vacancy'] = max_pay_vacancy

            # count_1 += 1
            articles_data['name_vacancy'] = name_vacancy
            articles_data['url_vacancy'] = url_vacancy
            articles_data['url'] = url
            articles_list.append(articles_data)
            # articles_data_hh['hh.ru'] = articles_list

            if bool(vacancies.find_one({'url_vacancy': url_vacancy})) == True:
                pass
            else:
                vacancies.insert_one(articles_data)
    if url_next_page is None:
        break
    else:
        response = session.get(url + url_next_page.attrs['href'], headers=headers)  # переход на сл.страницу

# print(f'{count_1} - вакансий найдено')
# print(f'{count_2} - страниц с вакансиями обработано')

for item in vacancies.find({}):

    pprint(item)
    print('')




"""
2. Написать функцию, которая производит поиск и выводит на
экран вакансии с заработной платой больше введённой суммы
(необходимо анализировать оба поля зарплаты). То есть цифра
вводится одна, а запрос проверяет оба поля
"""

# pay_v = int(input('Введите сумму ЗП'))
#
#
# def pay_vacantion(pay):
#     '''Возвращает коллецию содержащую уникальную сумму ЗП
#      из мин и макс показателей коллекции vacancies'''
#
#     pay_search_min = db_hh.pay_search_min  # создание коллекции для фильтра цены
#     pay_search_min.delete_many({})
#     for item_min in vacancies.find({'max_pay_vacancy': {'$gte': pay}}):  # фильтр цен
#         pay_search_min.insert_one(item_min)
#     for item_max in vacancies.find({'min_pay_vacancy': {'$gte': pay}}):
#         try:
#             pay_search_min.insert_one(item_max)
#         except errors.DuplicateKeyError:
#             pass
#     return pay_search_min
#
#
# for item_ps in (pay_vacantion(pay_v)).find({}):
#     pprint(item_ps)
