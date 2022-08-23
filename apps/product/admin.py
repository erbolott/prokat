from django.contrib import admin
from .models import Category , Product ,Images
from mptt.admin import DraggableMPTTAdmin
# Register your models here.


class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {"slug":('title',)} # момент одновременной записи название и слага
    save_on_top = True

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Сопутствующие товары (для этой конкретной категории)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Сопутствующие товары (в категории)'
#mptt


class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title' , 'create_at' , 'category' , 'image_tag']
    list_filter = ['category']
    prepopulated_fields = {"slug":('title',)}
    save_on_top = True
    inlines = [ProductImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'image_tag']
    list_filter = ['product',]
    

admin.site.register(Category , CategoryAdmin)
admin.site.register(Product , ProductAdmin)
admin.site.register(Images, ImagesAdmin)