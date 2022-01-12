from django.db import models

class User(models.Model):
    name         = models.CharField(max_length=40, null=True)
    email        = models.EmailField(max_length=200, unique=True)
    password     = models.CharField(max_length=200)

    class Meta:
        db_table = 'users'
class Post(models.Model): 
    user        = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    text        = models.CharField(max_length=300)
    created_at  = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'posts'