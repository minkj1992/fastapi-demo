# fastapi-demo
> with tortoise

## setup
> Python 3.8.6 (default, Oct 23 2020, 14:00:06) 
```bash
$ pyenv virtualenv fastapi
$ pyenv activate fastapi
$ pip install --upgrade pip
$ pip install fastapi 'uvicorn[standard]'
$ mkdir project && cd project
$ cp .env-template .env
$ uvicorn project.main:app --reload --log-level=debug
```

## unit test
```bash
$ pytest
```

## todo
- [] heroku docker-compose ci/cd
- [] app structure