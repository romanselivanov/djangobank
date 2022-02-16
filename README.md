build in docker:  
docker-compose -p djangobank -f docker-compose.yml up --build  

http://localhost:8000/swagger/ - документация  
http://localhost:8000/auth/users/ - ссылки для регистрации, аутентификации etc., без фронта работать через swagger  


alternatively install for dev:
1) pip install poetry  
2) poetry install  
3) python manage.py migrate  
4) python manage.py runserver  
5) cd nextjs  
6) npm i  
7) npm run dev  
(dev фронт http://127.0.0.1:3000 (не localhost)  для работы аутентификации)  

8) celery -A conf worker -l info --pool=solo  
(--pool=solo for windows dev only)  
9) celery -A conf beat -l info  
