from django.db import models

class KitType(models.model):
	name = models.CharField(max_length=255)

class Location(models.model):
	name = models.CharField(max_length=255)
	lat = models.DoubleField()
	lng = models.DoubleField()

class Kit(models.model):
	kit_type = models.ForeignKey(KitType)
	destintation = models.ForeignKey(Location)
	estimated_delivery_date = models.DateTimeField()

class KitHistory(models.model):
	kit = models.ForeignKey(Kit)
	created = models.DateTimeField()
	location = models.ForeignKey(Location)
	state = models.ForeignKey(KitState)
	
class KitState(models.model):
	name = models.CharField(max_length=255)
	ordinal = models.IntegerField()

