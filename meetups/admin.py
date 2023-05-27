from django.contrib import admin
from .models import Latestorder
from .models import Recentlyaddedproducts
# Register your models here.


class LatestorderAdmin(admin.ModelAdmin):
    list_display = ('title','orderId','status','popularity')
    list_filter = ('orderId','status')
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Latestorder,LatestorderAdmin)

class RecentlyaddedproductsAdmin(admin.ModelAdmin):
    list_display = ('title','rate','status')
    list_filter = ('status',)
    prepopulated_fields = {'slug':('title',)}


admin.site.register(Recentlyaddedproducts,RecentlyaddedproductsAdmin)
