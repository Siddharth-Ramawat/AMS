from django.db import models
from users.models import Profile
import datetime
from django.contrib.auth.models import User

class Events(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now=True)
    event_date = models.DateField(default=datetime.date.today)
    event_subject = models.CharField(max_length=40)
    organizer_name = models.CharField(max_length=50)
    text = models.CharField(max_length=400)
    email = models.EmailField()
    venue = models.CharField(max_length=200,default=0)

    def __str__(self):
        return self.event_subject


class Poll(models.Model):
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE)
    yes_count = models.IntegerField(default=0)
    no_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.event_id)