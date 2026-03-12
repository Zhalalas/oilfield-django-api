from ninja import Router
from oilfield.models import ProductionReading
from django.shortcuts import get_object_or_404
from oilfield.schemas import ProductionReadingIn, ProductionReadingOut, ProductionReadingUpdate
production_reading_router = Router(tags=["Production Readings"])
@production_reading_router.post('/', response=ProductionReadingOut)
def create_production_reading(request, data: ProductionReadingIn):
    production_reading = ProductionReading.objects.create(
        sensor_id=data.sensor_id,
        timestamp=data.timestamp,
        value=data.value
    )
    return ProductionReadingOut.from_orm(production_reading)
@production_reading_router.get('/', response=list[ProductionReadingOut])
def list_production_readings(request, sensor_id: int = None, start: str = None, end: str = None):
    if sensor_id is not None:
        production_readings = ProductionReading.objects.filter(sensor_id=sensor_id)
    else:
        production_readings = ProductionReading.objects.all()
    return [ProductionReadingOut.from_orm(pr) for pr in production_readings]
@production_reading_router.get('/{id}', response=ProductionReadingOut)
def get_production_reading(request, id: int):
    production_reading = get_object_or_404(ProductionReading, id=id)
    return ProductionReadingOut.from_orm(production_reading)
@production_reading_router.put('/{id}', response=ProductionReadingOut)
def update_production_reading(request, id: int, data: ProductionReadingUpdate):
    production_reading = get_object_or_404(ProductionReading, id=id)
    if data.sensor_id is not None:
        production_reading.sensor_id = data.sensor_id
    if data.timestamp is not None:
        production_reading.timestamp = data.timestamp
    if data.value is not None:
        production_reading.value = data.value
    production_reading.save()
    return ProductionReadingOut.from_orm(production_reading)
@production_reading_router.delete('/{id}')
def delete_production_reading(request, id: int):
    production_reading = get_object_or_404(ProductionReading, id=id)
    production_reading.delete()
    return {'message': 'Production reading deleted successfully'}    
