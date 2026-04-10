from user_agents import parse
from app.engine.protocols import BaseExtractor
from fastapi import Request

class LanguageExtractor(BaseExtractor):

    async def extract(self, request: Request):

        # get the raw header, default to empty string if missing
        language_response = request.headers.get("accept-language", "en-US")
        
        # en-US,en;q=0.9,hi;q=0.8,te;q=0.7
        language = language.split(",")[0]
        
        return {
            "browser_language": language
        }