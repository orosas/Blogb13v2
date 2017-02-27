from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def Consulta(request):
	r = requests.get('https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=WErUlu6SzPVPMkfoJrpmg1sDpeejzSpHTyy8MLd1')
	dict_nasa = dict(r.json())
	# dic2 ['2015-09-08','2015-09-08']
	dic2 = dict_nasa['near_earth_objects']
	
	#return render(request,'Nasa/index.html',{'dict_nasa':})
	return HttpResponse('Pagina de nasa')
	

	pass

"""
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf8'
>>> r.encoding
'utf-8'
>>> r.text
u'{"type":"User"...'
>>> r.json()
"""