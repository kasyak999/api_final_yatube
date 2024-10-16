# api_final

[Ссылка на описание](#описание)

### Установка

1. создать виртуальное окружение
    ```bash 
    python -m venv venv
    ```
    ```bash 
    source venv/bin/activate
    ```
2. Установить зависимости
    ``` bash
    pip install -r requirements.txt
    ```
3. Установить миграции
    ```bash
    python manage.py makemigrations
    ```
    ```bash
    python manage.py migrate
    ```
4.  Запустить
    ```bash
    python manage.py runserver
    ```

### Документация API
После запуска сервера будет доступна документация к api по адресу: http://127.0.0.1:8000/redoc/ 

## Описание

Есть распространённый способ проектирования, согласно которому сначала составляют документацию, а потом, основываясь на ней как на техническом задании, пишут программную часть API. Это задание вам предстоит выполнить именно по такой схеме.

### Задание проекта
Ваша задача — дописать код и привести его в соответствие с документацией: добавить недостающие модели в приложении posts, создать адреса и представления для обработки запросов в приложении api. Документация — это ваше техническое задание.

Например, в проекте должна быть описана модель Follow, в ней должно быть два поля — user (кто подписан) и following (на кого подписан). Для этой модели в документации уже описан эндпоинт /follow/ и два метода:

- GET — возвращает все подписки пользователя, сделавшего запрос. Возможен поиск по подпискам по параметру search
- POST — подписать пользователя, сделавшего запрос на пользователя, переданного в теле запроса. При попытке подписаться на самого себя, пользователь должен получить информативное сообщение об ошибке. Проверка должна осуществляться на уровне API.

Анонимный пользователь на запросы к этому эндпоинту должен получать ответ с кодом 401 Unauthorized. 

Сейчас ни самой модели Follow, ни обработчиков запросов в коде нет. Надо их написать.