from django.contrib import admin
from .models import History,Contacts,Prices,Hours,Post
# Register your models here.
admin.site.register(History)
admin.site.register(Contacts)
admin.site.register(Prices)
admin.site.register(Hours)
admin.site.register(Post)