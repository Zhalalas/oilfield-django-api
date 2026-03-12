from django.db import models

class MockItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

class OilField(models.Model):
    name = models.CharField(max_length=200, null=False)
    location = models.CharField(max_length=200)
    operator_company = models.CharField(max_length=200)
    start_date = models.DateField(auto_now=True)
    
class Well(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('shut-in', 'Shut-in'),
        ('abandoned', 'Abandoned'),
    ]
    
    oil_field = models.ForeignKey(OilField, on_delete=models.CASCADE, related_name='wells')
    name = models.CharField(max_length=200, null=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    drill_date = models.DateField()
    depth_m = models.FloatField()
    
class Sensor(models.Model):
    SENSOR_TYPE_CHOICES = [
        ('pressure', 'Pressure'),
        ('temperature', 'Temperature'),
        ('flow_rate', 'Flow Rate'),
    ]
    
    well = models.ForeignKey(Well, on_delete=models.CASCADE, related_name='sensors')
    sensor_type = models.CharField(max_length=20, choices=SENSOR_TYPE_CHOICES)
    install_date = models.DateField()
    is_active = models.BooleanField(default=True)
    
class ProductionReading(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='readings')
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()
    unit = models.CharField(max_length=50)