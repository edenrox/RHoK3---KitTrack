from django.http import HttpResponse
from django.shortcuts import *
from django.core.context_processors import csrf
from webui.models import *

def kit_ship(request):
	
	if (request.method == 'POST'):
		# create the kit
		kit = Kit.create(kit_type = request.POST['kit_type'], estimated_delivery_date = request.POST['estimated_delivery_date'], destination = request.POST['destintion'])
		
		# add the kit history for the first one
		kit_history = KitHistory.create(kit = kit.pk, created = request.POST['date_shipped'], location = request.POST['start_location'], state = 1)
		
		# redirect to the kit details
		return redirect(u'/kit/%s/history' % (kit.pk)) 
	
	# load the KitTypes and Locations
	kit_types = KitType.objects.order_by('name')
	locations = Location.objects.order_by('name')
		
	# render the template
	return render_to_response('kit-ship.html', {'kit_types': kit_types, 'locations': locations})
	
def kit_track(request):
	
	if (request.method == 'POST'):
		kit_id = request.POST['kit_id']
		url = u'/kit/%s/history' % (kit_id)
		print url
		return redirect(url)
		
	c = {}
	c.update(csrf(request))
	
	return render_to_response('kit-track.html', c);

def kit_history(request, kit_id):
	
	history = KitHistory.objects.filter(kit=kit_id)
	
	return render_to_response('kit-history.html', {'kit_id': kit_id, 'kit_history': history})
