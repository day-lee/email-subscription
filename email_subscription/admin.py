from django.contrib import admin
from .models import Category, UserSubscription, EmailManager

admin.site.register(Category)
admin.site.register(UserSubscription)
admin.site.register(EmailManager)