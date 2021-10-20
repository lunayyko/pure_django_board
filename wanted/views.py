import json, re, bcrypt, jwt

from django.views          import View
from django.http           import JsonResponse

from django.core.paginator import Paginator

from wanted.models         import User, Post

from my_settings           import SECRET_KEY

class Post(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            Post.objects.create( #디비에 값을 추가
                user_id  = request.user.id, #요청을 수행하는 유저의 아이디 
                text     = data["text"]#입력받은 값
            )
            return JsonResponse({"message": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

    def get(self, request):
            posts = Post.objects.all() 
            #업로드모델에 따라 객체를 다 가져와서 저장

            #posts 페이징 처리
            page      = request.GET.get('page','1')
            #GET 방식으로 정보를 받아오는 데이터
            paginator = Paginator(posts, '10')
            #Paginator(분할될 객체, 페이지 당 담길 객체수)
            page_obj  = paginator.page(page)
            #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
            results = []

            for post in posts: #저장된 객체들을 한 개씩 돌면서
                results.append({
                    "user_id"    : post.user_id,#글 객체의 유저아이디
                    "text"       : post.text,
                    "created_at" : post.created_at,
                })
            return JsonResponse(({"results": results}, {'page_obj':page_obj}), status=200)

class PostModify(View):
    def patch(self,request, post_id):
        try:
            data = json.loads(request.body)
            post = Post.objects.get(id=post_id)
            
            if post.user_id == request.user.id : #요청하는 유저가 글 쓴 사람이라면
                Post.objects.update( 
                    text     = data["text"]
                )
                return JsonResponse({"message": "SUCCESS"}, status=201)
            else:
                return JsonResponse({"message": "NOT_AUTHORIZED"}, status=403)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        
    def delete(self,request, post_id):
        try:
            post = Post.objects.get(id=post_id)
            if post.user_id == request.user.id:
                post.delete()
                return JsonResponse({"message": "SUCCESS"}, status=201)
            else:
                return JsonResponse({"message": "NOT_AUTHORIZED"}, status=403)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

class SignUpView(View):
    def post(self, request):
        try:
            data            = json.loads(request.body)
            email           = data['email']
            password        = data['password']
            hashed_password = bcrypt.hashpw(password.encode('UTF-8'), bcrypt.gensalt())

            if User.objects.filter(email=email).exists():
                return JsonResponse({"MESSAGE": "EMAIL_ALREADY_EXIST"}, status=400)

            if not re.match(r"^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
                return JsonResponse({"MESSAGE": "INVALID_FORMAT"}, status=400)

            if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$", password):
                return JsonResponse({"MESSAGE": "INVALID_FORMAT"}, status=400)

            User.objects.create(
                name     =   data.get('name'), #선택적으로 입력받을 때
                email    =   email,
                password =   hashed_password.decode('UTF-8'),
            )
            return JsonResponse({"MESSAGE": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)

class SignInView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)      
            email    = data['email']
            password = data['password']        

            if not User.objects.filter(email = email).exists():
                return JsonResponse({'MESSAGE':'INVALID_VALUE'}, status = 401)

            if bcrypt.checkpw(password.encode('utf-8'),User.objects.get(email=email).password.encode('utf-8')):
                nickname = User.objects.get(email = email).nickname
                token = jwt.encode({'id':User.objects.get(email=email).id}, SECRET_KEY, algorithm=const_algorithm)
            
                return JsonResponse({'TOKEN': token, "EMAIL":email, "NICKNAME":nickname}, status = 200)

            return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status = 400)