from django.contrib import admin

from user.models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email', 'is_active', 'is_staff')
    search_fields = ('username', 'pk', 'email')
    list_filter = ('username', 'email', )
    list_editable = ('username', )


admin.site.register(User, UserAdmin)