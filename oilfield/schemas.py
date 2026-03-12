from datetime import date, datetime
from ninja import Schema
from typing import Optional

class MockItemIn(Schema):
    name: str
    description: str

class MockItemOut(Schema):
    id: int
    name: str
    description: str
    created_at: datetime

class OilFieldIn(Schema):
    name: str
    description: Optional[str] = None
class OilFieldOut(Schema):
    id: int
    name: str
    description: Optional[str] = None
class OilFieldUpdate(Schema):
    name: Optional[str] = None
    description: Optional[str] = None

class WellIn(Schema):
    name: str
    status: str
    drill_date: date
    depth_m: float
class WellOut(Schema):
    id: int
    name: str
    status: str
    drill_date: date
    depth_m: float
class WellUpdate(Schema):
    name: Optional[str] = None
    status: Optional[str] = None
    drill_date: Optional[date] = None
    depth_m: Optional[float] = None
    
class SensorIn(Schema):
    name: str
    type: str
    unit: str
class SensorOut(Schema):
    id: int
    name: str
    type: str
    unit: str
class SensorUpdate(Schema):
    name: Optional[str] = None
    type: Optional[str] = None
    unit: Optional[str] = None
    
class ProductionReadingIn(Schema):
    well_id: int
    sensor_id: int
    timestamp: datetime
    value: float
class ProductionReadingOut(Schema):
    id: int
    well_id: int
    sensor_id: int
    timestamp: datetime
    value: float
class ProductionReadingUpdate(Schema):
    well_id: Optional[int] = None
    sensor_id: Optional[int] = None
    timestamp: Optional[datetime] = None
    value: Optional[float] = None
    


