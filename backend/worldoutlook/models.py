from django.db import models

class WorldOutlook(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(blank=True, null=True, max_length=4000)

    def __str__(self):
        return self.name
