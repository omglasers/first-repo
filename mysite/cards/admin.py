from django.contrib import admin

# Register your models here.

from .models import Card

class CardsAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['url_field']}),
		()

	]

admin.site.register(Card)