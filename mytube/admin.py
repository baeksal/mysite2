from django.contrib import admin
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display  = ('id', 'category_list', 'title', 'created_at', 'updated_at', 'video_id')
    list_filter   = ('updated_at', 'created_at',)
    search_fields = ('title', 'content')


    def category_list(self, Category):
        return ', '.join(o.name for o in Category.category.all()) 


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('id','name','description')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)