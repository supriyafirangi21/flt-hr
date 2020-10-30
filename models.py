from django.db import models
class Activity_user(models.Model):
    id = models.IntegerField(primary_key=True)
    real_name=models.CharField( max_length=255, blank=True, null=True)
    tz=models.CharField( max_length=255, blank=True, null=True)


class Activity_periods(models.Model):
    start_time=models.DateTimeField()
    end_time = models.DateTimeField()
    pid = models.ForeignKey(Activity_user, related_name='info',on_delete=models.CASCADE,primary_key=True)

    def __str__(self):
        return self.pid







