from django.contrib import admin
from .models import Post,Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','status','created_on')
    list_filter = ('status',)
    search_field = ['title','content']
    prepoulated_field = {'slug':('title',)}
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post","author","created_date","text")
    search_field = ["author","text","post"]

admin.site.register(Post,PostAdmin)    
admin.site.register(Comment,CommentAdmin)