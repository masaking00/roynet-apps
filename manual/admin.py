from django.contrib import admin
from manual.models import Category,CategoryRank,Post



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('c_order','category_name')

class CategoryRankAdmin(admin.ModelAdmin):
    list_display= ('cr_category_name','cr_rank','cr_order')

class PostAdmin(admin.ModelAdmin):
    list_display = ('p_title','p_order','p_category')


admin.site.register(Category,CategoryAdmin)
admin.site.register(CategoryRank,CategoryRankAdmin)
admin.site.register(Post,PostAdmin)