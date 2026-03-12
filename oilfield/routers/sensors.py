from ninja import Router
from oilfield.models import Sensor
from django.shortcuts import get_object_or_404
from oilfield.schemas import SensorIn, SensorOut, SensorUpdate
sensor_router = Router(tags=["Sensors"])
@sensor_router.post('', response=SensorOut)
def create_sensor(request, data: SensorIn):
    sensor = Sensor.objects.create(
        name=data.name,
        type=data.type,
        unit=data.unit
    )
    return SensorOut.from_orm(sensor)
@sensor_router.get('', response=list[SensorOut])
def list_sensors(request, well_id: int = None):
    if well_id is not None:
        sensors = Sensor.objects.filter(well_id=well_id)
    else:
        sensors = Sensor.objects.all()
    return [SensorOut.from_orm(s) for s in sensors]
@sensor_router.get('/{id}', response=SensorOut)
def get_sensor(request, id: int):
    sensor = get_object_or_404(Sensor, id=id)
    return SensorOut.from_orm(sensor)
@sensor_router.put('/{id}', response=SensorOut)
def update_sensor(request, id: int, data: SensorUpdate):
    sensor = get_object_or_404(Sensor, id=id)
    if data.name is not None:
        sensor.name = data.name
    if data.type is not None:
        sensor.type = data.type
    if data.unit is not None:
        sensor.unit = data.unit
    sensor.save()
    return SensorOut.from_orm(sensor)
@sensor_router.delete('/{id}')
def delete_sensor(request, id: int):
    sensor = get_object_or_404(Sensor, id=id)
    sensor.delete()
    return {'message': 'Sensor deleted successfully'}    
    