from django.db import models
from courses.models import Videos


class User(models.Model):
    userVidSeen = models.ManyToManyField(Videos)
    usrName = models.CharField(max_length=50)
    usrLastname = models.CharField(max_length=50)
    usrPassword = models.CharField(max_length=50)
    class Meta:
        db_table = "user"
class userSeen:
    usrId = models.ForeignKey(User, on_delete=models.CASCADE)
    vidId = models.ForeignKey(Videos, on_delete=models.CASCADE)
    class Meta:
        db_table="UserSeen"
