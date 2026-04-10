import httpx
import os
from app.engine.protocols import BaseExtractor
from fastapi import Request

class WeatherExtractor(BaseExtractor):
    async def extract(self, request: Request):
        
        api_key = os.getenv("WEATHER_API_KEY", "YOUR_PLACEHOLDER_KEY")
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=auto:ip"
        

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, timeout=0.5)
                
                # raise an error if the API returns a 4xx or 5xx
                response.raise_for_status()
                
                data = response.json()
                
                return {
                    "temp": data.get("current", {}).get("temp_c", 20.0),
                    "condition": data.get("current", {}).get("condition", {}).get("text", "unknown"),
                    "time": data.get("location", {}).get("localtime", "unknown"),
                    "city": data.get("location", {}).get("name", "unknown") 
                }
                                
            except Exception as e:
                # fallback

                print(f"Weather API Error: {e}")
                return {
                    "temp": 20.0, 
                    "condition": "Clear", 
                    "time": "unknown",
                    "city": "unknown"
                }