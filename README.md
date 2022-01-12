# 퓨어장고로 구현한 게시판 CRUD

## 사용 기술 및 tools
> - Back-End :  Python3.8, Django3.2, MySQL 
> - ETC : Git, Github, Postman
## 구성 요소
- bcrypt로 암호화, 회원가입, 로그인에 JWT 사용
- 게시판 CRUD : 글 리스트 출력, 새 글 등록, 자신이 쓴 글 수정 및 삭제 구현 
- RESTful API 사용
- 페이지네이션
- 유닛테스트
## 실행방법

1. 원하는 경로에 해당 프로젝트를 깃 클론 받는다
```terminal
git clone https://github.com/lunayyko/pure_django_board.git
```

2. manage.py가 있는 디렉토리 상에 mysql 데이터베이스 내용을 포함한 my_settings.py파일을 추가한다.
```python
SECRET_KEY = '랜덤한특정문자열'

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cloudnineapp',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

ALGORITHM = 'HS256'
```

3. 데이터베이스를 생성한다
```bash
mysql.server start
mysql -u root -p
```
```sql
mysql > create database cloudnineapp character set utf8mb4 collate utf8mb4_general_ci;
```
4. 가상환경을 만들고 실행한다(미니콘다 설치 필요)
```bash
conda create -n cloudnine python=3.8
conda activate cloudnine
```

4. 라이브러리들을 설치한다
```python
pip install -r requirements.txt 
```

5. 마이그레이션을 실행한다.
```python
python manage.py makemigrations
python manage.py migrate
```

5. 서버를 실행한다(파이썬이 설치 필요)
```python
python manage.py runserver
```
## API 명세

[POSTMAN API 문서](https://documenter.getpostman.com/view/16843815/UVXhovkJ)
