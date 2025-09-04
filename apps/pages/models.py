from django.db import models

from apps.blogs.models import BaseModel


class ContactModel(BaseModel):
    email = models.EmailField()
    address = models.TextField()
    phone_number = models.CharField(
        max_length=15, null=True, blank=True
    )
    subject = models.CharField(
        max_length=255, null=True, blank=True
    )
    message = models.TextField()

    is_read = models.BooleanField(default=False)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.full_name} - {self.email}"

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


