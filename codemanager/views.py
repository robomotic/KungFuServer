# Views: templates for different operations 
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

from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from codemanager.models import CodeSize
from django.contrib.auth.models import User

from django.contrib.auth.models import User, Group
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from serializers import UserSerializer, GroupSerializer

#########################################################################
__author__="Paolo Di Prodi"
__version__ = "1.0"
#########################################################################

def index(request):
    latest_code_updates = CodeSize.objects.order_by('-pub_date')[:5]
    template = loader.get_template('codemanager/index.html')
    context = Context({
        'activity_list': latest_code_updates,
    })
    return HttpResponse(template.render(context))
    #output = ', '.join([chunk.user for chunk in latest_code_updates])

# ...
def detail(request, activity_id):
    codesize = get_object_or_404(CodeSize, pk=activity_id)
    return render(request, 'codemanager/detail.html', {'activity': codesize})


def updateFromClient(request):
    """ This is called by the kung fu client for an update  """
    user = get_object_or_404(User, username=request.POST['username'])
