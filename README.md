# evo_task_2

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/KhizhnyakSergey/evo_task_2.git
$ cd evo_task_2
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv venv_evo
$ venv_evo\Scripts\activate
```

Then install the dependencies:

```sh
(venv_evo)$ pip install -r requirements.txt
```
Note the `(venv_evo)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

Once `pip` has finished downloading the dependencies:
```sh
(venv_evo)$ cd evo_task_2
(venv_evo)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

## Task

Потрібно написати веб-сервіс. На головній сторінці форма з полем введення імені та кнопкою "Привітатись". При натисканні на кнопку, якщо ім'я зустрілося вперше, виведи "Привіт, <Ім'я+Прізвище> або "Привіт, <email>" (на твій вибір). Якщо таке ім'я вже зустрічалося, виведи "Вже бачилися, ім'я".

Також на головній має бути посилання, при натисканні на яке потрібно показати список усіх, з ким уже привіталися.

Подумай, де краще зберігати стан (state). Як його краще зберігати? Чи можливо оптимізувати по пам'яті, якщо ми очікуємо, що до нас прийдуть вітатись користувачі всього Інтернету. Зроби проект на Github із репозиторієм.

Плюс, якщо є зрозумілий README, проект загорнутий у Docker, застосовані GitHub Actions, проект розгорнутий на будь-якому хостингу (heroku, digitalocean, будь-який інший)

Якщо хочеться додати щось до цього завдання - не соромся проявити творчість.
