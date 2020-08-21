from django.db import models
from django.utils import timezone

class BoastRoast(models.Model):
    rbvote = ((True, 'Boast'), (False, 'Roast'))
    choices = models.BooleanField(choices=rbvote, default=True)
    user_input = models.CharField(max_length=280, default='')
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    time_posted = models.DateTimeField(default=timezone.now)

    @property
    def votes(self):
        return self.upvotes - self.downvotes


