# Django deployment

## Структура проекта (ориентируйтесь, пожалуйста)
```bash
- /var/
  - www/ (это основная директория)
    - run/ (тут лежат .pid и .sock файлы)
    - logs/ (тут лежат логи)
    - demo/ (тут лежит проект)
      - .conf/ (тут лежат конфиги)
      - .meta/ (тут лежит метка для виртуального окружения python)
      - src/ (тут лежит код)
      - venv/ (тут лежит виртуальное окружение)
```

## Устанавливаем важные и нужные штуки
```bash
apt-get -y install wget htop git
```

### Устанавливаем Python3.9
```bash
apt-get -y install build-essential libsqlite3-dev zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
wget https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tgz
tar -xzvf Python-3.9.5.tgz
cd Python-3.9.5
./configure --enable-optimizations
make
make altinstall
cd ..
rm Python-3.9.5.tgz
rm -rf Python-3.9.5
```

## Устанавливаем пакетики для Python
```bash
apt-get install python-dev python3-dev python-setuptools python-virtualenv python-pip python3-pip
```

## Устанавливаем NGINX
```bash
apt-get install nginx
```

## Устанавливаем PostgreSQL
```bash
sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
sudo apt install wget ca-certificates
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
apt-get update
apt-get install postgresql
```
После этого нужно подправить hostbase authorization конфиг:
```bash
nano /etc/postgresql/13/main/pg_hba.conf
```
Находим строку:
```
# "local" is for Unix domain socket connections only
local   all             all                                     peer
```
Заменяем на:
```
# "local" is for Unix domain socket connections only
local   all             all                                     md5
```
Для сохранения изименений в редакторе nano используем комбинацию клавиш **Ctrl+O**, для выхода из редактора - **Ctrl+X**.
Выполняем команду:
```bash
service postgresql restart
```

## Создаем пользователя и базейку
```bash
sudo -u postgres psql
```
Выполняем пару команд:
```SQL
CREATE ROLE demo LOGIN CREATEDB PASSWORD 'demo';
CREATE DATABASE demo WITH OWNER='demo' ENCODING='UTF8';
\q
```

## Устанавливаем supervisor
```bash
pip install supervisor
```

## Качаем проект
```bash
cd /var/www
git clone https://github.com/codemeetspeople/demo.git
```

## Создаем папки для сокетов и логов
```bash
cd /var/www
mkdir logs
mkdir run
chmod 777 -R logs
chmod 777 -R run
```

## Коннектим Django и PostgreSQL
```bash
cd /var/www/demo/src/core
touch settings_local.py
nano settings_local.py
```
Пишем туда (туда - это в файл settings_local.py):
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'demo',
        'NAME': 'demo',
        'PASSWORD': 'demo'
    }
}
```

## Готовим Django к запуску
### Создаем виртуальное окружение
```bash
cd /var/www/demo
virtualenv venv --python=/usr/local/bin/python3.9
source venv/bin/activate
pip install -r .meta/packages
```

### Устанавливаем uWSGI
```bash
cd /var/www/demo
source venv/bin/activate
pip install uwsgi
```
Если насыпало over9000 ошибок и не установилось, ТО ТОЛЬКО В ЭТОМ СЛУЧАЕ выполняем следующие действия:
Зайти в файл /var/www/demo/.meta/packages и закомментить ipython
Файл должен выглядеть так:
```
Django==3.2.2
django-tinymce==3.3.0
ipdb==0.13.7
#ipython==7.23.1
psycopg2-binary==2.8.6
django-jinja==2.7.0
django-bootstrap4==3.0.1
```
После этого:
```bash
cd /var/www/demo
deactivate
rm -rf venv
virtualenv venv --python=/usr/bin/python3.6
source venv/bin/activate
pip install -r .meta/packages
pip install uwsgi
```

### Накатываем миграции и статику
```bash
cd /var/www/demo
source venv/bin/activate
cd /var/www/demo/src
chmod +x manage.py
./manage.py migrate
./manage.py createsuperuser
./manage.py collectstatic
```

## Конфижим NGINX
```bash
rm /etc/nginx/sites-enabled/default
ln -s /var/www/demo/.conf/nginx.conf /etc/nginx/sites-available/demo.conf
ln -s /etc/nginx/sites-available/demo.conf /etc/nginx/sites-enabled/demo.conf
```
Проверяем:
```bash
nginx -t
```
Должно быть что-то типа
```bash
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

## Стартуем supervisor
```bash
supervisord -c /var/www/demo/.conf/supervisor.ini
```

Ура!
