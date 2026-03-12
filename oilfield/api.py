from ninja import Router
from django.shortcuts import get_object_or_404
from .models import MockItem
from .schemas import MockItemIn, MockItemOut
from typing import List
router = Router(tags=["Mock CRUD"])
@router.post("/mock-items", response=MockItemOut)
def create_mock_item(request, payload: MockItemIn):
    obj = MockItem.objects.create(**payload.dict())
    return obj
@router.get("/mock-items", response=List[MockItemOut])
def list_mock_items(request):
    return MockItem.objects.all()
@router.put("/mock-items/{item_id}", response=MockItemOut)
def update_mock_item(request, item_id: int, payload: MockItemIn):
    obj = get_object_or_404(MockItem, id=item_id)
    for k, v in payload.dict().items():
        setattr(obj, k, v)
    obj.save()
    return obj
@router.delete("/mock-items/{item_id}")
def delete_mock_item(request, item_id: int):
    obj = get_object_or_404(MockItem, id=item_id)
    obj.delete()
    return {"deleted": True}