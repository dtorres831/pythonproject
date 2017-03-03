from __future__ import unicode_literals
from django.db import models
from ..loginandreg.models import User

class TravelManager(models.Manager):
    def planreview(self, postdata, user):
        errors=[]
        if not postdata['destination']:
            errors.append('destination cannot be empty')
        if not postdata['description']:
            errors.append('description cannot be empty')
        if not postdata['startdate']:
            errors.append('start date cannot be empty')
        if not postdata['enddate']:
            errors.append('end date cannot be empty')    
        if not postdata['startdate'] <= postdata['enddate']:
            errors.append('end date cannot be before start date')
        response = {}
        if errors:
            response['Status']= False
            response['errors']= errors
        else:
            travel = self.create(destination=postdata['destination'],startdate=postdata['startdate'], enddate=postdata['enddate'], user=user, description=postdata['description'])
            response['Status']= True
            response['travel'] = travel

        return response

class Travel(models.Model):
    destination = models.CharField(max_length=100)
    startdate = models.DateField()
    enddate = models.DateField()
    user = models.ForeignKey(User, related_name="travler")
    travel = models.ManyToManyField(User, related_name="travelwith")
    description = models.CharField(max_length=200)
    objects = TravelManager()
