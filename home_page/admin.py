from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('email', 'created')
    fields  = ('email', 'created')
    readonly_fields = ('created',)
