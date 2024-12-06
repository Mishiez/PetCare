from django.contrib import admin
from petcareapp.models import User,Product,Contact,Member

# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Member)