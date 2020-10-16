import cv2
from django.db import models
from apipro import laplacian
# Create your models here.
class awsimage(models.Model):
    title=models.CharField(max_length=50)
    images=models.ImageField('images/')














    def valid(self):
       if laplacian.variance_of_laplacian(self.images,100)<100:


            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
