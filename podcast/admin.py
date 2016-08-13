from django.contrib import admin
from models import Episode

# Register your models here.

class EpisodeAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Episode, EpisodeAdmin)