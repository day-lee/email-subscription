from email_subscription.models import UserSubscription, EmailManager
from email_subscription.serializers import UserSubscriptionSerializer, EmailManagerSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.core.mail import send_mail
from django.http import JsonResponse

#구독자 리스트
class SubscriptionList(APIView):
    """
    Show all subscribers
    """
    def get(self, request, format=None):
        subscribers = UserSubscription.objects.all()
        serializer = UserSubscriptionSerializer(subscribers, many=True)
        return Response(serializer.data)


#구독추가
class SubscriptionAdd(APIView):
    """
    Add a new subscriber
    """
    def post(self, request, format=None):
        serializer = UserSubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#구독해지
class Unsubscribe(APIView):
    """
    Delete a unsubscribed user using pk
    """
    def get_object(self, pk):
        try:
            return UserSubscription.objects.get(pk=pk)
        except UserSubscription.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        subscriber = self.get_object(pk)
        subscriber.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#카테고리 필터
class CategorySearch(generics.ListAPIView):
    """
    Search by category filter
    e.g. /subscription/search/?category=여행
    """
    serializer_class = UserSubscriptionSerializer
    def get_queryset(self):
        queryset = UserSubscription.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category__category=category)
        return queryset


#이메일 전송과 저장
class SendEmail(APIView):
    """
    Create, Save and Send Email
    """
    def post(self, request, format=None):
        serializer = EmailManagerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def send_mail(self, request):
        data = SendEmail.post(self, request, format=None)
        items = data['subscriber']
        items = list(items.items()) #('email', 'value@email.com')
        to_email = items[0][1]
        try:
            send_mail(
                data['subject'],
                data['content'],
                'testpythondy@gmail.com',
                [to_email],
                fail_silently=False
            )
            return JsonResponse({"status": "success"})
        except:
            return JsonResponse({"status": "fail"})


#이메일 필터
class EmailSearch(generics.ListAPIView):
    """
    Search by email subject filter, return a list
    e.g. email/search/?subject=hello
    """
    serializer_class = EmailManagerSerializer
    def get_queryset(self):
        queryset = EmailManager.objects.all()
        subject = self.request.query_params.get('subject', None)
        if subject is not None:
            queryset = queryset.filter(subject=subject)
        return queryset


