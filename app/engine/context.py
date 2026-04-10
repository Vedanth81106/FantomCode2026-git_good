from pydantic import BaseModel
from typing import Optional

class UserContext(BaseModel):

    # location
    # if field value is unknown, its automatically considered optional

    city: Optional[str] = "unknown"
    country_code: Optional[str] = "unknown"
    
    # weather - done
    weather_temp: Optional[float] = 20.0
    weather_condition: Optional[str] = "clear"
    
    # hardware/wealth - done
    is_mobile: Optional[bool] = False
    device_brand: Optional[str] = "generic"

    # browser language - done
    browser_language: Optional[str] = "english"
    
    # time/metadata - done
    local_time: Optional[str] = "13:00"
