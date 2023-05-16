import logging

import requests
from src.main.constants.BaseConstants import BaseConstants
from src.main.constants.Endpoints import EndPoints


class TestSetUp:

    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.logger = logging.getLogger(self.__class__.__name__)

    def urlMaker(self, endPoint):
        return f"{BaseConstants.BASE_URL}{BaseConstants.version}{endPoint}"

    def getRequest(self, endPoint):
        url = self.urlMaker(endPoint)
        self.logger.info("Hitting this API: %s", url)
        return requests.get(url, params={"api_key": self.apiKey})

    def postRequest(self, endpoint, body, guestSessionId, headers):
        url = self.urlMaker(endpoint)
        self.logger.info(url)
        return requests.post(f"{url}?guest_session_id={guestSessionId}",  params={"api_key": self.apiKey},json=body, headers=headers)

    def genericRequest(self, method, url, params, data):
        return requests.request(method, url, params=params, data=data)

    def getMovieRatings(self):
        return self.getRequest(EndPoints.getTopRatedMovies)

    def postMovieRatings(self, movieId, body, guestSessionId):
        headers = {'Content-Type': 'application/json'}
        return self.postRequest(EndPoints.rateMovie.format(movieId), body, guestSessionId, headers=headers)

    def getNewGuestSessionId(self):
        return self.getRequest(EndPoints.guestSessionKey)
