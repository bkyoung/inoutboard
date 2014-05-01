from django.db import models

class Employee(models.Model):
    phone = models.PositiveIntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    status = models.CharField(max_length=100, blank=True)
    comment = models.CharField(max_length=100, blank=True)
    estimated_return = models.CharField(max_length=100, blank=True)
    last_changed = models.DateTimeField(auto_now=True, blank=True)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def _get_full_name(self):
        "Returns person's full name."
        return "%s %s" % (self.first_name, self.last_name)

    full_name = property(_get_full_name)
