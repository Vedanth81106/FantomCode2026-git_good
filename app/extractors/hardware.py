from user_agents import parse
from app.engine.protocols import BaseExtractor
from fastapi import Request

class UserAgentExtractor(BaseExtractor):
    async def extract(self, request: Request):

        # get the raw header, default to empty string if missing
        ua_string = request.headers.get("user-agent", "")
        
        ua = parse(ua_string)
        
        # extract the brand and model, defaulting to "unknown" if None
        brand = ua.device.brand if ua.device.brand else "unknown"
        model = ua.device.model if ua.device.model else "unknown"
        os_family = ua.os.family if ua.os.family else "unknown"

        return {
            "is_mobile": ua.is_mobile,
            "device_brand": brand,
            "device_model": model,
            "os_family": os_family
        }