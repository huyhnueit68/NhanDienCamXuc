from django.db import models


# Create your models here.

class RequestClient(models.Model):
    client_name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    number_image = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now=True, blank=True)
    status = models.IntegerField(default=1)
    result_client = models.IntegerField()


class RequestImages(models.Model):
    image_path = models.ImageField(upload_to='img/%y')
    request_image_id = models.ForeignKey(RequestClient, on_delete=models.CASCADE)
    status = models.IntegerField(default=1)
    result_image = models.CharField(max_length=1000)
