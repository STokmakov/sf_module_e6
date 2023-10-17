# sf_module_e6
ИНСТРУКЦИЯ:
# скачиваем периложение с githab
git clone https://github.com/STokmakov/sf_module_e6.git

# создать настроить окружение
python -m venv venv && source venv/bin/activate

# устанавливаем зависимости
pip install -r requirements.txt

# запускаем Redis
docker run -p 6379:6379 -d redis:5

# запускаем приложение на daphne 
daphne -b localhost -p 8001 ChatApp.asgi:application

superuser: admin
password: qwerty123

user: test
password: !Qwerty23