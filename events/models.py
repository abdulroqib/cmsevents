from django.db import models
from datetime import datetime as dt
from cms.models import CMSPlugin

class Events(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    datetime = models.DateTimeField(default=dt.now)
    is_featured = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Events'

class EventsPluginModel(CMSPlugin):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)

    def __str__(self):
        return self.event.title