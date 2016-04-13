from django.contrib import admin
from polls.models import Poll,Choice
# Register your models here.

admin.site.register(Choice)

class PollAdmin(admin.ModelAdmin):
	fields = ['question','pub_date']
admin.site.register(Poll,PollAdmin)