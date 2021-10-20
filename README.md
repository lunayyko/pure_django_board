# wanted x wecode

## 구현한 방법과 이유에 대한 간략한 내용

장고와 파이썬 기술스택으로 구현했습니다.
- bcrypt로 암호화하고, JWT를 이용해 회원가입, 로그인 구현
- 게시글 리스트 출력(페이지네이터), 새 글 등록, 자신이 쓴 글 수정 및 삭제 구현 
- RESTful API
## 실행 방법(endpoint 호출방법)

```python
python manage.py runserver
```
해당 디렉토리에서 위의 명령어를 실행하면 localhost:8000에서 실행됩니다. 
## api 명세(request/response 서술 필요)

(get)   | /post           |  게시글 리스트 출력 | header에 토큰, body에 "text" : string
(post)  | /post           |  새 글 등록       | header에 토큰, body에 "text" : string
(patch) | /post/{post_id} |  글 수정  
(delete)| /post/{post_id} |  글 삭제




