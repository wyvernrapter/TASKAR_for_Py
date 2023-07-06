from django.db import models
from django.contrib.auth.models import User

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Em_id = models.IntegerField(null=True, blank=True)
    flag = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)
    PTO_SP = models.IntegerField(null=True, blank=True)
    PTO_flag = models.IntegerField(null=True, blank=True)
    PTO_upperhelf = models.IntegerField(null=True, blank=True)
    PTO_lowerhelf = models.IntegerField(null=True, blank=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    late_time = models.DateTimeField(default=None, null=True, blank=True)
    early_time = models.DateTimeField(default=None, null=True, blank=True)
    start_TE = models.IntegerField(null=True, blank=True)
    end_TE = models.IntegerField(null=True, blank=True)
    other_TE = models.IntegerField(null=True, blank=True)
    total_TE = models.IntegerField(null=True, blank=True)
    over_time = models.DateTimeField(null=True, blank=True)
    set_wt = models.DateTimeField(null=True, blank=True)
    set_wt_e = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.user.username, self.start_time.strftime('%Y-%m-%d %H:%M:%S'))


