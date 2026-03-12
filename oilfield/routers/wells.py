from ninja import Router
from oilfield.models import Well
from django.shortcuts import get_object_or_404
from oilfield.schemas import WellIn, WellOut, WellUpdate
well_router = Router(tags=["Wells"])
@well_router.post('', response=WellOut)
def create_well(request, data: WellIn):
    well = Well.objects.create(
        name=data.name,
        description=data.description
    )
    return WellOut.from_orm(well)
@well_router.get('', response=list[WellOut])
def list_wells(request):
    wells = Well.objects.all()
    return [WellOut.from_orm(w) for w in wells]
@well_router.get('/{id}', response=WellOut)
def get_well(request, id: int):
    well = get_object_or_404(Well, id=id)
    return WellOut.from_orm(well)
@well_router.put('/{id}', response=WellOut)
def update_well(request, id: int, data: WellUpdate):
    well = get_object_or_404(Well, id=id)
    if data.name is not None:
        well.name = data.name
    if data.description is not None:
        well.description = data.description
    well.save()
    return WellOut.from_orm(well)
@well_router.delete('/{id}')
def delete_well(request, id: int):
    well = get_object_or_404(Well, id=id)
    well.delete()
    return {'message': 'Well deleted successfully'}    
