from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, Team, Score

# Register your models here.

class UserAdmin(BaseUserAdmin):

	# The fields to be used in displaying the User model.
	# These override the definitions on the base UserAdmin
	# that reference specific fields on auth.User.
	list_display = ('email','user_name', 'is_staff', 'is_admin', 'create_date', 'update_date')
	list_filter = ()
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		('user_name', {'fields': ('user_name',)}),
		('Permissions', {'fields': ('is_admin','is_staff',)}),
		('date', {'fields': ('create_date', 'update_date')}),
	)
	search_fields = ('email',)
	ordering = ('email',)
	filter_horizontal = ()

admin.site.register(CustomUser, UserAdmin)

admin.site.register(Team)
admin.site.register(Score)