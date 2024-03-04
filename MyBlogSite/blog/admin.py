from django.contrib import admin
from .models import Post,Comment
# Register your models here.
    
   # customize the way data is displayed in the administration panel 
  
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','slug','status','today_date','created_on')
    list_filter = ("status",)
    search_fields = ['title','content']
    prepopulated_fields = {'slug':('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display=('post','author','text','created_date')
    
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
