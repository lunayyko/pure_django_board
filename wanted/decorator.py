import jwt

from django.http            import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from my_settings            import SECRET_KEY
from .models                import User

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        #들어올 수 있는 인자를 모두 받도록 한다
        try:
            token         = request.headers.get("Authorization", None)
            #헤더에서 Authorization(헤더에 있는 속성)을 가져와서 토큰에 저장한다.
            user          = jwt.decode(token, SECRET_KEY, algorithms='HS256')
            #토큰을 시크릿키를 이용해 디코드해서 유저 아이디를 알아내서 유저에 저장한다.
            request.user  = User.objects.get(id = user['id'])
            #유저의 아이디에 해당하는 유저객체를 리퀘스트.유저에 저장한다.

            return func(self, request, *args, **kwargs)
            #받은 인자들을 모두 전달해준다(예를 들어 이미지, 텍스트 등등)

        except jwt.exceptions.DecodeError:
            return JsonResponse({"message" : "INVALID_TOKEN"}, status=400)

        except ObjectDoesNotExist:
            return JsonResponse({"message" : "INVALID_USER"}, status=400)

    return wrapper