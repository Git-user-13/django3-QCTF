from django.contrib import admin

# Register your models here.

from . models import Product
from . models import Flag
from . models import complete
from . models import Board

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'created_at','hint_1','flag_1','hint_2','flag_2','hint_3','flag_3','hint_4','flag_4','hint_5','flag_5')

class FlagAdmin(admin.ModelAdmin):
    list_display = ('id','q1','h1','f1','score','h2','f2','h3','f3','h4','f4','h5','f5')

class completeAdmin(admin.ModelAdmin):
    list_display = ('id','user','hint','completed','finished_at')

class BoardAdmin(admin.ModelAdmin):
    list_display = ('id','user','score')

admin.site.register(Product,ProductAdmin)
admin.site.register(Flag,FlagAdmin)
admin.site.register(complete,completeAdmin)
admin.site.register(Board,BoardAdmin)