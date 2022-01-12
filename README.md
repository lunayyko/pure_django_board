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

1. 하는 경로에 해당 프로젝트를 깃 클론 받는다
```terminal
git clone https://github.com/lunayyko/pure_django_board.git
```

2. manage.py가 있는 디렉토리 상에 mysql 데이터베이스 내용을 포함한 my_settings.py파일을 추가한다.
```python
SECRET_KEY = '랜덤한 특정 문자열'

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

5. 서버를 실행한다(파이썬이 설치 필요)
```python
python manage.py runserver
```
## API 명세

### 1. 게시글 리스트 출력
----
 모든 게시글을 한 페이지당 3개씩 보여준다

* **URL, Method**

  /post | `GET`

* **응답 예시:**

  * **Code:** 200 <br />
    **Content:**
    ```json
    {
        "page": 1,
        "results": [
            [
                {
                    "post_id": 1,
                    "user_id": 1,
                    "text": "우린 같은걸 보면서~ 말을 건네지 않아도",
                    "created_at": "2021-10-20T04:29:43.401Z"
                },
                {
                    "post_id": 2,
                    "user_id": 1,
                    "text": "너와 걸을때면 난 내가 사랑받는걸 느껴",
                    "created_at": "2021-10-20T04:32:43.017Z"
                },
                {
                    "post_id": 3,
                    "user_id": 1,
                    "text": "너와 발을 맞출때 이렇게 기분 좋은걸",
                    "created_at": "2021-10-20T04:33:06.862Z"
                }
            ]
        ]
    }
    ```

### 2. 게시글 등록
---
 새 게시글을 등록한다 

* **URL, Method**

  /post | `POST`

* **요청 예시:**  
    **Content:**
    ```json
    {
        "text": "무궁화 꽃이 피었습니다"
    }
    ```

* **응답 예시:**

  * **Code:** 200 <br />
    **Content:**
    ```json
    {
        "message": "SUCCESS"
    }
    ```


### 3. 게시글 수정
---
본인이 쓴 게시글을 수정한다

* **URL, Method**

  /post/{post_id} | `PATCH`

* **요청 예시:**  
    **Content:**
    ```json
    {
        "text": "무궁화 꽃이 피었습니까?"
    }
    ```

* **응답 예시:**

  * **Code:** 200 <br />
    **Content:**
    ```json
    {
        "message": "SUCCESS"
    }
    ```

### 4. 게시글 삭제
---

본인이 쓴 게시글을 수정한다

* **URL, Method**

  /post/{post_id} | `DELETE`

* **응답 예시:**

  * **Code:** 200 <br />
    **Content:**
    ```json
    {
        "message": "SUCCESS"
    }
    ```
