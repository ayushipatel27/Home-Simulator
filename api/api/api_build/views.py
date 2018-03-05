from django.shortcuts import render
from django.template.response import TemplateResponse
from api_build.models import Rooms
from django.db.models import Max

# Create your views here.
def test(request):
	data = Rooms.objects.all()

	return TemplateResponse(request, 'api/index.html', {"data": data})