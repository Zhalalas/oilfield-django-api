from ninja import Router
from oilfield.models import OilField
from oilfield.schemas import OilFieldIn, OilFieldOut, OilFieldUpdate
from django.shortcuts import get_object_or_404
oil_field_router = Router(tags=["Oil Fields"])
@oil_field_router.post('/', response=OilFieldOut)
def create_oil_field(request, data: OilFieldIn):
    oil_field = OilField.objects.create(
        name=data.name,
        description=data.description
    )
    return OilFieldOut.from_orm(oil_field)
@oil_field_router.get('/', response=list[OilFieldOut])
def list_oil_fields(request):
    oil_fields = OilField.objects.all()
    return [OilFieldOut.from_orm(of) for of in oil_fields]
@oil_field_router.get('/{id}', response=OilFieldOut)
def get_oil_field(request, id: int):
    oil_field = get_object_or_404(OilField, id=id)
    return OilFieldOut.from_orm(oil_field)
@oil_field_router.put('/{id}', response=OilFieldOut)
def update_oil_field(request, id: int, data: OilFieldUpdate):
    oil_field = get_object_or_404(OilField, id=id)
    if data.name is not None:
        oil_field.name = data.name
    if data.description is not None:
        oil_field.description = data.description
    oil_field.save()
    return OilFieldOut.from_orm(oil_field)
@oil_field_router.delete('/{id}')
def delete_oil_field(request, id: int):
    oil_field = get_object_or_404(OilField, id=id)
    oil_field.delete()
    return {'message': 'Oil field deleted successfully'}    
