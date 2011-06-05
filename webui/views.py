from django.http import HttpResponse
from django.shortcuts import *
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from webui.models import *

def kit_ship(request):
	
	if (request.method == 'POST'):
		# create the kit
		the_kit_type = KitType.objects.get(pk = request.POST['kit_type'])
		dest_location = Location.objects.get(pk = request.POST['destination'])
		the_kit = Kit(kit_type = the_kit_type, destination = dest_location, estimated_delivery_date = request.POST['estimated_delivery_date'])
		the_kit.save()
		
		# add the kit history for the first one
		start_location = Location.objects.get(pk = request.POST['start_location'])
		start_state = KitState.objects.get(pk = 1)
		kit_history = KitHistory.objects.create(kit = the_kit, created = request.POST['date_shipped'], location = start_location, state = start_state)
		kit_history.save()
		
		# redirect to the kit details
		return redirect(u'/kit/%s/history' % (the_kit.pk)) 
	
	# load the KitTypes and Locations
	kit_types = KitType.objects.order_by('name')
	locations = Location.objects.order_by('name')
	
	# Setup the dictionary and CSRF Key
	c = {'kit_types': kit_types, 'locations': locations}
	c.update(csrf(request))
		
	# render the template
	return render_to_response('kit-ship.html', c)
	
def kit_track(request):
	
	if (request.method == 'POST'):
		kit_id = request.POST['kit_id']
		url = get_kit_url(kit_id)
		return redirect(url)
		
	c = {}
	c.update(csrf(request))
	
	return render_to_response('kit-track.html', c);

def kit_history(request, kit_id):
	
	history = KitHistory.objects.filter(kit=kit_id)
	
	return render_to_response('kit-history.html', {'kit_id': kit_id, 'kit_history': history})


def get_kit_url(kit_id):
	return u'/kit/%s/history' % (kit_id)

def kit_progress(request, kit_id):
	
	if (request.method == 'POST'):
		the_kit = Kit.objects.get(pk = kit_id)
		location = Location.objects.get(pk = request.POST['location'])
		state = KitState.objects.get(pk = request.POST['state'])
		history = KitHistory.objects.create(kit = the_kit, created = request.POST['date'], location = location, state = state)
		
		url = get_kit_url(kit_id)
		return redirect(url)
	
	locations = Location.objects.order_by('name')
	kit_states = KitState.objects.order_by('ordinal')
	
	c = {'kit_id': kit_id, 'locations': locations, 'kit_states': kit_states}
	c.update(csrf(request))
	
	return render_to_response('kit-progress.html', c)


@csrf_exempt
def sms(request):
	tijuana_id = 14
	
	# Get the message body
	#message = request.POST['Body']
	message = "kit intransit"
	
	# parse what command
	parts = message.strip().split(' ')
	print "parts", parts
	
	# the response
	response_text = ''
	
	if (parts[0] == 'kit'):
		if (parts[1] == 'intransit'):
			# ok, what packages are in trasit
			location = Location.objects.get(pk=tijuana_id)
			kits = Kit.objects.get(destination=location.pk)
			response_text = u'Kits on the way to %s:\n' % (location) #, ','.join(kits))
		elif (len(parts)):
			# load the kit
			kit_id = parts[1]
			the_kit = Kit.objects.get(pk=kit_id)
			if (parts[2] == 'where'):
				# ok, where is the kit
				kit_history = KitHistory.objects.filter(kit=the_kit).order_by('-date')[0]
				response_text = 'On %s, kit %s was in %s' % (kit_history.created, kit_id, kit_history.location)
			if (parts[2] == 'arrived'):
				# ok, the kit has arrived
				state = KitState.objects.get(pk=3)
				kit_history = KitHistory.objects.create(kit=the_kit, location=kit.destination, created=datetime.today())
				response_text = u'Kit %s arrived at %s' % (kit_history.created, kit_id, location)
				
	response = HttpResponse(mimetype='text/xml')
	real_response = u'<Response><Sms>%s</Sms></Response>' % (response_text)
	response.write(real_response)
	return response

