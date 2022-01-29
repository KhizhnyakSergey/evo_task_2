# evo_task_2

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/KhizhnyakSergey/evo_task_2.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv venv_evo
$ venv_evo/Scripts/activate.bat
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


