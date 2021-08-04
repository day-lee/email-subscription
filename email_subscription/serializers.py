from rest_framework.serializers import ModelSerializer
from email_subscription.models import UserSubscription, EmailManager
from rest_framework import serializers
from email_subscription.models import UserSubscription, EmailManager


class UserSubscriptionSerializer(ModelSerializer):
    category = serializers.SerializerMethodField('get_category')
    class Meta:
        fields = ('id', 'email', 'name', 'category')
        model = UserSubscription

    def get_category(self, obj):
        return [category.category for category in obj.category.all()]

class EmailManagerSerializer(ModelSerializer):
    subscriber = UserSubscriptionSerializer()
    class Meta:
        fields = ('id', 'subject', 'content', 'subscriber')
        model = EmailManager

