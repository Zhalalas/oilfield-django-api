from ninja import NinjaAPI
from oilfield.api import router as mock_router
from oilfield.routers import oil_field_router, well_router, production_reading_router, sensor_router

api = NinjaAPI(title="Oilfield Operations API", version="0.1.0")

api.add_router("mock/", mock_router)
api.add_router("oil-fields/", oil_field_router)
api.add_router("wells/", well_router)
api.add_router("production-readings/", production_reading_router)
api.add_router("sensors/", sensor_router)

@api.get("/health", tags=["Health"])
def health(request):
    return {"status": "ok"}

