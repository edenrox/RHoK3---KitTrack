from django.http import HttpResponse

def kit_ship(request):
	#return render_to_response('templates/ship.html');
	return HttpResponse("Hey")
	
def kit_track(request):
	return render_to_response('templates/track.html');
		
