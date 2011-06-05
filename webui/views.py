from django.http import HttpResponse
from django.shortcuts import render_to_response

def kit_ship(request):
	return render_to_response('kit-ship.html')
	
def kit_track(request):
	return render_to_response('kit-track.html')

def kit_history(request, kit_id):
	return render_to_response('kit-history.html')
