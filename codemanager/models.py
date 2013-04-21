# Models: this is the model component that contains the code updates
# Author: Paolo Di Prodi
# Copyright 2012 Robomotic ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

#########################################################################
__author__="Paolo Di Prodi"
__version__ = "1.0"
#########################################################################

"""@package Models
This is the class that is responsible for pushing/pulling data from the RESTful database

"""
def convertDatetimeToString(o):
    """ Utility function to convert a Django DateTime field to string  """
    DATE_FORMAT = "%Y-%m-%d" 
    TIME_FORMAT = "%H:%M:%S"
    
    if isinstance(o, datetime.datetime):
        return o.strftime("%s %s" % (TIME_FORMAT,  DATE_FORMAT))
    if isinstance(o, datetime.date):
        return o.strftime(DATE_FORMAT)
    elif isinstance(o, datetime.time):
        return o.strftime(TIME_FORMAT)
        
class CodeSize(models.Model):
    """
    This contains an update from the programmer: a list of file types with the total stats
    """
    ## the user from where the update is originated
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    ## the date when the update was sent
    pub_date = models.DateTimeField('date updated')
    ## a description of the update
    description = models.TextField(max_length=140)

    def was_published_recently(self):
        """check if the update was published within 1 day"""
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    ## in the admin panel order the entries by publication date
    was_published_recently.admin_order_field = 'pub_date'
    ## a checkmark to show if it was published recently
    was_published_recently.boolean = True
    ## short description
    was_published_recently.short_description = 'Synced recently?'
    
    def __unicode__(self):
        """unicode method when printing """
        title= self. description +" -> "+ convertDatetimeToString(self.pub_date)
        return title


class FileType(models.Model):    
    """
    This contains the total amount of lines and density for a file type like *.cpp
    The density is calculated as total size / total lines
    """
    filext = models.CharField(max_length=3)
    lines=models.IntegerField()
    density=models.FloatField()
    update=models.ForeignKey(CodeSize)
    def __unicode__(self):
        """unicode method when printing """
        return self.filext
        
