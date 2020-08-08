from django.db import models

# Create your models here.

class User_Data(models.Model):
    uid=models.CharField(max_length=50)
    real_name=models.CharField(max_length=100)
    tz=models.CharField(max_length=100)

    def __str__(self):
        return self.uid

class Activity_Mapping(models.Model):
    user_activity_id=models.ForeignKey(User_Data, to_field='id', on_delete=models.SET_NULL,null=True)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()

    def __str__(self):
        return "{} {} {}".format(self.user_activity_id,self.start_time,self.end_time)
