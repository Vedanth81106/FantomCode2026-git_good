from abc import ABC, abstractmethod

async def extract(self, requests: Request):

    """ This method extracts a specific signal from each HTTP request
        It must be implemented by all sub  classes
    """