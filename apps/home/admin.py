from django.contrib import admin
from .models import Setting , News , Slier_promotion

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title' , 'create_at']

class Slier_promotionAdmin(admin.ModelAdmin):
    list_display = ['id' , 'create_at' ]

admin.site.register(News , NewsAdmin)
admin.site.register(Setting)
admin.site.register(Slier_promotion , Slier_promotionAdmin)