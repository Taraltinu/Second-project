from django.db import models




class CategoryModel(models.Model):
    name = models.CharField(max_length=50)
    cover_pic = models.FileField(upload_to="media/%y/%m/%d")
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name