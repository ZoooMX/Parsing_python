import requests
from bs4 import BeautifulSoup
import json

headers = {'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
job_name = input('Введите должность')
url = 'https://hh.ru/'
session = requests.Session() #работа в режиме 1 сессии
response = session.get('https://hh.ru/search/vacancy?text=' + job_name, headers=headers) #переход на страницу с должностью с исп. User-Agent
dom_hh = BeautifulSoup(response.text, 'html.parser') #парсиг страницы с помощью html.parser
print(response)

count_1 = 0 # счетчик вакансий
count_2 = 0 # счетчик страниц
articles_list = []
articles_data_hh = {}
while True:
    dom = BeautifulSoup(response.text, 'html.parser')  #парсиг страницы с помощью html.parser
    url_next_page = dom.find('a', {'data-qa': ['pager-next']}) #ссылка на сл.строку
    articles = dom.find_all('div', {'class': 'vacancy-serp-item-body__main-info'})  #все заголовки страницы
    count_2 += 1
    for article in articles:
        articles_data = {}
        name_vacancy = article.find('a', {'data-qa': ['vacancy-serp__vacancy-title']}).text #поиск по тэгу с заданным ключем и значением
        url_vacancy = article.find('a', {'data-qa': ['vacancy-serp__vacancy-title']}).attrs['href']  #ссылка на вакансию
        url = 'https://hh.ru'
        articles_data['name_vacancy'] = name_vacancy
        articles_data['url_vacancy'] = url_vacancy
        pay_txt = article.find('span', {'data-qa': ['vacancy-serp__vacancy-compensation']})
        if pay_txt is None: #если ЗП не указана
            pass
        else:
            pay_txt = pay_txt.text.replace('\u202f', '')  #приведение в str без юникода
            pay_list = pay_txt.split()  #привожу в список для будущего условия по выборке цены
            cur_pay_vacancy = pay_list[-1] #валюта
            articles_data['cur_pay_vacancy'] = cur_pay_vacancy
            if 'от' == pay_list[0]:
                min_pay_vacancy = int(pay_list[1])
                articles_data['min_pay_vacancy'] = min_pay_vacancy
            elif 'до' == pay_list[0]:
                max_pay_vacancy = int(pay_list[1])
                articles_data['max_pay_vacancy'] = max_pay_vacancy
            else:
                min_pay_vacancy = int(pay_list[0])
                max_pay_vacancy = int(pay_list[2])
                articles_data['min_pay_vacancy'] = min_pay_vacancy
                articles_data['max_pay_vacancy'] = max_pay_vacancy

            count_1 += 1
            articles_data['url'] = url
            articles_list.append(articles_data)
            articles_data_hh['hh.ru'] = articles_list
    if url_next_page is None:
        break
    else:
        response = session.get(url + url_next_page.attrs['href'], headers=headers) #переход на сл.страницу

print(f'{count_1} - вакансий найдено')
print(f'{count_2} - страниц с вакансиями обработано')


with open('data_hh.json', 'w', encoding='utf-8') as file_json:
    json.dump(articles_data_hh, file_json)

name = 'data_hh.json'
with open(name) as file_json:
    data_hh = json.load(file_json)

print(data_hh)