from django.db import models

class KitType(models.Model):
	name = models.CharField(max_length=255)
	
	def __unicode__(self):
		return u'%s' % (self.name)

class Location(models.Model):
	name = models.CharField(max_length=255)
	lat = models.FloatField()
	lng = models.FloatField()
	
	def latStr(self):
		direction = 'N'
		if (self.lat < 0):
			direction = 'S'
		return u'%.03f %s' % (math.fabs(self.lat), direction)
	
	def lngStr(self):
		direction = 'W'
		if (self.lat < 0):
			direction = 'E'
		return u'%.03f %s' % (math.fabs(self.lng), direction)
	
	def __unicode__(self):
		return u'%s (%s, %s)' % (self.name, self.latStr(), self.lngStr())

class Kit(models.Model):
	kit_type = models.ForeignKey(KitType)
	destintation = models.ForeignKey(Location)
	estimated_delivery_date = models.DateTimeField()

class KitState(models.Model):
	name = models.CharField(max_length=255)
	ordinal = models.IntegerField()

class KitHistory(models.Model):
	kit = models.ForeignKey(Kit)
	created = models.DateTimeField()
	location = models.ForeignKey(Location)
	state = models.ForeignKey(KitState)
	
class CartonType(models.Model):
	type = models.ForeignKey(KitType)
	name = models.CharField(max_length=255)

class SupplyItemType(models.Model):
	name = models.CharField(max_length=255)
	
class SupplyItem(models.Model):
	name = models.CharField(max_length=255)
	type = models.ForeignKey(SupplyItemType)

class CartonContent(models.Model):
	type = models.ForeignKey(CartonType)
	item = models.ForeignKey(SupplyItem)
	quantity = models.FloatField()


	

