import uuid

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

    shift_length = models.DurationField(null=True, blank=True)
    break_length = models.DurationField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.punch_out:
            self.shift_length = self.punch_out - self.punch_in
            if self.break_start and self.break_end:
                self.break_length = self.break_end - self.break_start
                self.shift_length -= self.break_length
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.punch_in.strftime('%Y-%m-%d %H:%M:%S')}"

    @property
    def duration(self):
        return self.shift_length