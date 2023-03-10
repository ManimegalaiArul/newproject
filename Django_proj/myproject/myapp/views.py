from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

from myapp import models

def index(request):
	uniqueids = models.PollingUnit.objects.values_list('uniqueid', flat=True)
	res = models.AnnouncedPuResults.objects.all()
	results = []
	for unit in uniqueids:
		temp =""
		for r in res:
			if(str(r.polling_unit_uniqueid) == str(unit)):
				temp = temp + r.party_abbreviation + ":"+ str(r.party_score) + ","
		if(temp != ""):
			results.append({'unit': unit,'txt' : temp})
	return render(request, "myapp/index.html", {"uniqueids" : uniqueids, 'results' : results})

# def index(request):
# 	return HttpResponse("Hello, world!")	
