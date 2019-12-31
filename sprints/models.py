from django.db import models

# Create your models here.
class Sprint(models.Model):
    Project_Name = models.CharField(max_length=255)
    Sprint_Name = models.CharField(max_length=100)
    Resource_Name = models.CharField(max_length=255)
    Planned_Deliverables = models.TextField()
    Delivery_date = models.DateTimeField()
    Challenges_Faced = models.TextField()