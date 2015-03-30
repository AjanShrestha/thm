

from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from django.contrib.gis.db import models

from users.models import UserProfile

import pytz
import jsonfield
import uuid
from moneyed import Money, NPR

from djmoney.models.fields import MoneyField
# Create your models here.

STATUS_SELECTION = (
    ('0', 'New'),
    ('1', 'Accepted'),
    ('2', 'Completed')
)

JOBS_SELECTION = (
    ('0', 'N/A'),
    ('1', 'Plumbing'),
    ('2', 'Electrical'),
    ('3', 'Furnishing'),
    ('4', 'Masonry'),
)


def getUniqueUUID():
    uniqueID = ''.join(str(uuid.uuid4()).split('-'))
    return uniqueID


class Jobs(models.Model):

    jobref = models.CharField(_('jobref'), max_length=100, unique=True, default=getUniqueUUID)
    customer = models.ForeignKey(UserProfile, limit_choices_to={'user_type':'2'}, related_name='jobs')
    fee = MoneyField(_('fee'), decimal_places=2,
        max_digits=8, blank=True, null=True, default_currency='NPR', default=0.00)
    status = models.CharField(_('status'),
                    max_length=1,
                    choices=STATUS_SELECTION,
                    default='0',
                    )
    creation_date = models.DateTimeField(_('creation_date'),
        default=timezone.now)
    jobtype = models.CharField(_('jobtype'),
                    max_length=250,
                    default='0',
                    )
    handyman = models.ManyToManyField(UserProfile, related_name='orders')
    # isaccepted = models.BooleanField(_('isaccepted'), default=False)
    # isnotified = models.BooleanField(_('isnotified'), default=False)
    # is_complete = models.BooleanField(_('is_complete'), default=False)
    ishidden = models.BooleanField(_('ishidden'), default=False)
    distance = models.DecimalField(_('distance'), decimal_places=2,
        max_digits=1000, default=0)
    accepted_date = models.DateTimeField(_('accepted_date'),
        blank=True, null=True, editable=False)
    completion_date = models.DateTimeField(_('completion_date'),
        blank=True, null=True, editable=False)
    available_handymen = jsonfield.JSONField(_('available_handymen'), default={})
    considered_handymen = models.TextField(_('considered_handymen'), default=[])
    remarks = models.TextField(_('remarks'), blank=False)
    destination_home =  models.BooleanField(_('destination_home'), default=True)
    location = models.PointField(srid=4326, default='POINT (85.3141498444705064 27.6942413607694782)', blank=True, null=True)
    location_landmark = models.CharField(
        _('Nearest Address'),
        max_length=100
    )
    objects = models.GeoManager()

    def __unicode__(self):
        return str(self.jobref)

        #Overriding
    def save(self, *args, **kwargs):
        if self.jobref == '':
            self.jobref=''.join(str(uuid.uuid4()).split('-'))
        super(Jobs, self).save(*args, **kwargs)

class JobEvents(models.Model):
    """Models for JobEvents"""

    job = models.ForeignKey(Jobs)
    event = models.IntegerField(_('event'), max_length=2, default=1)
    updated_on = models.DateTimeField(_('updated_on'),
        default=timezone.now)
    extrainfo = jsonfield.JSONField(_('extrainfo'), default='{}', max_length=9999)


    def save(self, *args, **kwargs):
        super(JobEvents, self).save(*args, **kwargs)
