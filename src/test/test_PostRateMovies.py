from src.main.constants.BaseConstants import BaseConstants
from src.main.constants.HTTPsStatusCode import StatusCode
from src.main.constants.SetUp import TestSetUp


def test_PostMovieRatings():
    setUp = TestSetUp(BaseConstants.apiKey)
    resp = setUp.getMovieRatings()
    movieId = resp.json()["results"][0]["id"]
    resp = setUp.getNewGuestSessionId()

    assert resp.status_code == StatusCode.OK, "Failed to fetch new session"
    guestSessionId = resp.json()['guest_session_id']
    payload = {
        "value": 5.5}
    res = setUp.postMovieRatings(movieId, payload, guestSessionId)

    assert res.status_code == StatusCode.CREATED, "Failed to post rating"
    assert res.json()['status_message'] == 'Success.'



def test_PostRatingWithoutGuestSession():
    setUp = TestSetUp(BaseConstants.apiKey)
    resp = setUp.getMovieRatings()
    movieId = resp.json()["results"][0]["id"]
    payload = {
        "value": 7.5}
    res = setUp.postMovieRatings(movieId, payload, 'test')

    assert res.status_code == StatusCode.UNAUTHORIZED, "Failed to post rating"
    assert res.json()['status_message'] == 'Authentication failed: You do not have permissions to access the service.'
