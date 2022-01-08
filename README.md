how to install:

1) pip install poetry  
2) poetry install  
3) python manage.py migrate  
4) python manage.py runserver  


http://localhost:8000/swagger/ - документация  
http://localhost:8000/auth/users/ - ссылки для регистрации, аутентификации etc., без фронта работать через swagger  

как собрать фронт фронт  
cd nextjs  
npm i  
npm run dev  
dev фронт http://127.0.0.1:3000 (не localhost)  для работы аутентификации  

celery -A conf worker -l info --pool=solo  
(--pool=solo for windows dev only)  
celery -A conf beat -l info  
