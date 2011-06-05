from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from webui.models import *

def kit_ship(request):
	
	locations = Location.get_objects()
	
	#if (request.method == 'POST'):
		
	
	return render_to_response('kit-ship.html', )
	
def kit_track(request):
	
	if (request.method == 'POST'):
		kit_id = request.POST['kit_id']
		return redirect(u'/kit/%d/history' % (kit_id))
		
	c = {}
	c.update(csrf(request))
	
	return render_to_response('kit-track.html', c);

def kit_history(request, kit_id):
	
	history = KitHistory.objects.filter(kit=kit_id)
	
	return render_to_response('kit-history.html', {'kit_id': kit_id, 'kit_history': history})
