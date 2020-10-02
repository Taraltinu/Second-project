from django.db import models

class Contact(models.Model):
    fullname = models.CharField(max_length=50)
    mobile = models.IntegerField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    on_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "ContactModel"
    def __str__(self):
        return self.fullname