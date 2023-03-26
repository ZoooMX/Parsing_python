# Parsing_python


### Lesson_1. Основы клиент-серверного взаимодействия. Работа с API
##### Задачи:
1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного 
пользователя, сохранить JSON-вывод в файле *.json
2. Изучить список открытых API (https://www.programmableweb.com/category/all/apis).
Найти среди них любое, требующее авторизацию (любого типа). Выполнить запросы к нему, пройдя авторизацию.
Ответ сервера записать в файл.
При запуске на неизвестной VK машине не выдает инфу, результат сохранил в текстовик с именем: Run_from_PyCharm_VK.txt
##### Выполнение:
[Python_script](https://github.com/ZoooMX/Parsing_python/blob/main/lesson_1/HW_lesson_1.py)
[data_git_repo](data_repo.json)
[Run_from_PyCharm_VK.txt](https://github.com/ZoooMX/Parsing_python/blob/main/lesson_1/Run_from_PyCharm_VK.txt)

### Lesson_2. BeautifulSoup
##### Задачи:
Необходимо собрать информацию о вакансиях на вводимую должность (используем input или через аргументы получаем должность) с сайтов HH(обязательно) и/или Superjob(по желанию). Приложение должно анализировать несколько страниц сайта (также вводим через input или аргументы). Получившийся список должен содержать в себе минимум:
1. Наименование вакансии.
2. Предлагаемую зарплату (разносим в три поля: минимальная и максимальная и валюта. цифры преобразуем к цифрам).
3. Ссылку на саму вакансию.
4. Сайт, откуда собрана вакансия. (можно прописать статично hh.ru или superjob.ru)
5. По желанию можно добавить ещё параметры вакансии (например, работодателя и расположение). Структура должна быть одинаковая для вакансий с обоих сайтов. Общий результат можно вывести с помощью dataFrame через pandas. Сохраните в json либо csv.
##### Выполнение:
[Python_script](https://github.com/ZoooMX/Parsing_python/blob/main/lesson_2/lesson_2.py)
[data.json](https://github.com/ZoooMX/Parsing_python/blob/main/lesson_2/data_hh.json)

### Lesson_3. BeautifulSoup + MongoDB
##### Задачи:
Связать задачу с выгрузко данных в MongoDB
##### Выполнение:
[Python_script](https://github.com/ZoooMX/Parsing_python/blob/main/lesson_3/lesson_3.py)
