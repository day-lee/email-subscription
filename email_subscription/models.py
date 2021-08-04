from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.category


class UserSubscription(models.Model):
    email = models.EmailField(null=False, blank=True, max_length=200, unique=True)
    name = models.CharField(max_length=20, null=True)
    category = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.email


class EmailManager(models.Model):
    subject = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)
    subscriber = models.ForeignKey(UserSubscription, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ('subject',)

    # 	"ID": "메일 ID",
    # 	"CreatedAt": "메일 생성날짜",
    # 	"UpdatedAt": "메일 수정날짜",
    # 	"DeletedAt": "메일 삭제날짜",
    # 	"Sender": "메일 발신인",
    # 	"Receiver": "메일 수신인",
    # 	"Subject": "메일 제목",
    # 	"Content": "메일 내용"