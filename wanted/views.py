import json, re, bcrypt, jwt

from django.views          import View
from django.http           import JsonResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models               import User
from .models               import Post as PostModel

from my_settings           import SECRET_KEY

from wanted.decorator      import login_decorator

class Post(View):
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = request.user

            PostModel.objects.create( #디비에 값을 추가
                user_id  = user.id, #요청을 수행하는 유저의 아이디 
                text     = data["text"]#입력받은 값
            )
            return JsonResponse({"message": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

    def get(self, request):
            post_list = PostModel.objects.all().order_by('id')
            paginator = Paginator(post_list, 3)
            # 한 페이지당 오브젝트 3개씩 나오게 설정
            page      = int(request.GET.get('page',1))
            # page라는 값으로 받을거고, 없으면 첫번째 페이지로

            try:
                posts = paginator.page(page)
            except PageNotAnInteger:
                posts = paginator.page(1)
            except EmptyPage:
                posts = paginator.page(paginator.num_pages)

            results = []

            results.append([{
                        "post_id"    : post.id,
                        "user_id"    : post.user_id,#글 객체의 유저아이디
                        "text"       : post.text,
                        "created_at" : post.created_at,
                    } for post in posts ])
            return JsonResponse({"page" : page, "results": results}, status=200)

class PostModify(View):
    @login_decorator
    def patch(self,request, post_id):
        try:
            data = json.loads(request.body)
            post = PostModel.objects.get(id=post_id)
            
            if post.user_id == request.user.id : #요청하는 유저가 글 쓴 사람이라면
                PostModel.objects.filter(id=post_id).update( 
                    text     = data["text"]
                )
                return JsonResponse({"message": "SUCCESS"}, status=201)
            else:
                return JsonResponse({"message": "NOT_AUTHORIZED"}, status=403)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
    
    @login_decorator
    def delete(self,request, post_id):
        try:
            post = PostModel.objects.get(id=post_id)
            if post.user_id == request.user.id:
                post.delete()
                return JsonResponse({"message": "SUCCESS"}, status=201)
            else:
                return JsonResponse({"message": "NOT_AUTHORIZED"}, status=403)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

class SignUp(View):
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

class SignIn(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)      
            email    = data['email']
            password = data['password']        

            if not User.objects.filter(email = email).exists():
                return JsonResponse({'MESSAGE':'INVALID_VALUE'}, status = 401)

            if bcrypt.checkpw(password.encode('utf-8'),User.objects.get(email=email).password.encode('utf-8')):
                token = jwt.encode({'id':User.objects.get(email=email).id}, SECRET_KEY)
            
                return JsonResponse({'TOKEN': token}, status = 200)

            return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status = 400)