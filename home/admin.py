from django.contrib import admin,auth

from .models import Department,Doctor,Booking

# Register your models here.
class DepTitle(admin.ModelAdmin):
    list_display=('id','depname','depdes')
admin.site.register(Department,DepTitle)

class DocTitle(admin.ModelAdmin):
    list_display=('id','dname','depname','ddes','dimg')
admin.site.register(Doctor,DocTitle)

class BookAdmin(admin.ModelAdmin):
    list_display=('id','pname','pemail','dname','pdate','bdate')
admin.site.register(Booking,BookAdmin)


