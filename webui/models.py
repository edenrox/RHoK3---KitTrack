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

class CartonType(models.model):
	type = models.ForeignKey(KitType)
	name = models.CharField(max_length=255)

class CartonContent(models.model):
	type = models.ForeignKey(CartonType)
	item = models.ForeignKey(SupplyItem)
	quantity = models.DoubleField()
	
class SupplyItem(models.model):
	name = models.CharField(max_length=255)
	type = models.ForeignKey(SupplyItemType)
	
class SupplyItemType(models.model):
	name = models.CharField(max_length=255)
