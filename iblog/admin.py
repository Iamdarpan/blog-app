from django.contrib import admin
from .models import Category,Post

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','url','add_date')
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','post_des','url')
    list_filter = ('title',)
    list_per_page = 50

    class Media:
        js= ('https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js','js/scripts.js',)

# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)



