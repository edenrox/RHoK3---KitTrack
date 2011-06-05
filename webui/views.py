from django.http import HttpResponse
from django.shortcuts import render_to_response

def kit_ship(request):
	return render_to_response('templates/ship.html');
	
def kit_track(request):
	return render_to_response('templates/track.html');
		
