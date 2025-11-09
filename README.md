## Проект по покупке товара в Saucedemo 
### Используемый стек 

<p  align="center">
<code><img width="5%" title="Python" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/1024px-Python.svg.png"></code>
<code><img width="5%" title="Pycharm" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/PyCharm_Icon.svg/1200px-PyCharm_Icon.svg.png"></code>
<code><img width="5%" title="Pytest" src="https://upload.wikimedia.org/wikipedia/commons/b/ba/Pytest_logo.svg"></code>
<code><img width="5%" title="Selene" src="https://fs.getcourse.ru/fileservice/file/download/a/159627/sc/264/h/e0cabcb69a2df1e6b1086292c020a4a7.png"></code>
<code><img width="5%" title="Allure Report" src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4"></code>
<code><img width="5%" title="GitHub" src="https://cdn-icons-png.flaticon.com/512/25/25231.png"></code>
</p>
<br> 

### Что проверяет тест
* Заполнение формы авторизации
* Добавление товара в корзину
* Проверка наличия товара в корзине и его количества
* Навигацию (Открытие страницы меню "О нас")
* Выход из системы 
* Подтверждение ошибки при вводе невалидных данных при авторизации
<br>

## Запуск теста  

1. Склонировать репозиторий
```bash
git clone https://github.com/tsypur/hw_qa_guru_python_lesson_14
cd hw_qa_guru_python_lesson_14
```

2. Открыть проект и установить интерпретатор
3. Создать файл с переменными окружения `.env` по образцу в корне проекта
4. Запустить тесты

```bash
pytest
```
### Allure 

Для просмотра отчета локально нужно ввести команду:

```bash
allure serve tests/allure-results
```
### Пример отчёта в Jenkins

#### Jenkins Build
![Jenkins Build](media/jenkins_1.png)

#### Allure Overview  
![Allure Report](media/jenkins_2.png)

#### Детали прохождения теста
![Test Details](media/jenkins_3.png)

#### Telegram Notification
![Telegram](media/tg_4.png)