import uuid

from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.db import models


class Shift(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    punch_in = models.DateTimeField()
    punch_out = models.DateTimeField(null=True, blank=True)
    break_start = models.DateTimeField(null=True, blank=True)
    break_end = models.DateTimeField(null=True, blank=True)

    corrected_punch_in = models.DateTimeField(null=True, blank=True)
    corrected_punch_out = models.DateTimeField(null=True, blank=True)
    corrected_break_start = models.DateTimeField(null=True, blank=True)
    corrected_break_end = models.DateTimeField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    @property
    def duration(self):
        total_time = self.punch_out - self.punch_in
        if self.break_start and self.break_end:
            break_time = self.break_end - self.break_start
            total_time -= break_time
        return total_time
