from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.

# abstractbaseuserで作成したほうがよい
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('phone',)}),)
    list_display = ['username', 'email', 'phone']

admin.site.register(CustomUser, CustomUserAdmin)