from django.contrib import admin

# Register your models here.

from .models import Card

class CardsAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['name']}),
		('Date information', {'fields': ['url_field', 'image', 'media_type', 'created_at', 'owner'], 'classes':['collapse'] })

	]
	list_display=('name', 'created_at')
	list_filter = ['name']
	search_fields = ['name']

admin.site.register(Card, CardsAdmin)