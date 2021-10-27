# wanted x wecode 게시판 CRUD

## 구현한 방법과 이유에 대한 간략한 내용

장고와 파이썬 기술스택으로 구현했습니다.
- bcrypt로 암호화, 회원가입, 로그인에 JWT 사용
- 게시판 CRUD : 글 리스트 출력, 새 글 등록, 자신이 쓴 글 수정 및 삭제 구현 
- RESTful API
- 페이지네이션
- 유닛테스트 

## 실행 방법(endpoint 호출방법)

```python
python manage.py runserver
```
해당 디렉토리에서 위의 명령어를 실행하면 localhost:8000에서 실행됩니다. 
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
