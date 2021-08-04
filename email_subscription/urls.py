from django.urls import path, re_path
from email_subscription import views
from .views import CategorySearch, SendEmail, EmailSearch

app_name = 'email_subscription'

urlpatterns = [
    path('', views.SubscriptionList.as_view()),
    path('subscription/add', views.SubscriptionAdd.as_view()),
    path('subscription/cancel/<int:pk>', views.Unsubscribe.as_view()),
    path('subscription/search/', CategorySearch.as_view()),
    path('email/send/', SendEmail.as_view()),
    path('email/search/', EmailSearch.as_view()),
]
