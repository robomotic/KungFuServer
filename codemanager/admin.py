# Admin: admin UI for CRUDE operations over the code updates
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


import models
from django.contrib import admin
from codemanager.models import CodeSize
from codemanager.models import FileType

#########################################################################
__author__="Paolo Di Prodi"
__version__ = "1.0"
#########################################################################

class FileInfoInline(admin.TabularInline):
    """ A tabular inline view for adding file summaries one to one  """
    model = FileType
    fieldsets = [
        ('Code performance', {'fields': ['filext','lines', 'density']})
    ]    
    list_filter = ['filext']
    extra = 1
class CodeUpdatesAdmin(admin.ModelAdmin):
    """ Shows each code update individually  """
    list_display = ('user','pub_date', 'was_published_recently')

    fieldsets = [
        ('Coder',               {'fields': ['user']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('Project info',{'fields':['description'],  'classes': ['collapse']} )
        
    ]
    list_filter = ['pub_date', 'user']
    search_fields = ['user']
    date_hierarchy = 'pub_date'
    inlines = [FileInfoInline]
    
class FileInfoAdmin(admin.ModelAdmin):
    """ Shows each file individually  """
    list_display = ('update','filext', 'lines')

    fieldsets = [
        ('Code performance', {'fields': ['filext','lines', 'density']})
    ]    
    list_filter = ['filext']
    
admin.site.register(CodeSize, CodeUpdatesAdmin)
admin.site.register(FileType, FileInfoAdmin)

