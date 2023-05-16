from src.main.constants.BaseConstants import BaseConstants
from src.main.constants.HTTPsStatusCode import StatusCode
from src.main.constants.SetUp import TestSetUp


def test_GetTopRatedMovieWithInvalidApiKey():
    resp = TestSetUp(BaseConstants.inValidApiKey).getMovieRatings()

    assert resp.status_code == StatusCode.UNAUTHORIZED, \
        print(
            "StatusCode mismatch, Expected: {}, Actual: {}".format(StatusCode.UNAUTHORIZED, resp.status_code))

    assert not resp.json()['success']
    assert resp.json()['status_message'] == "Invalid API key: You must be granted a valid key."


def test_GetTopRatedMovieWithValidApiKey():
    resp = TestSetUp(BaseConstants.apiKey).getMovieRatings()

    assert resp.status_code == StatusCode.OK, print(
        "StatusCode mismatch, Expected: {}, Actual: {}".format("200", resp.status_code))

    response_data = resp.json()

    assert len(response_data['results']) > 0
    assert not (response_data["results"][0]["id"] is None) or (str(response_data["results"][0]["id"]).strip()=="")
    assert response_data['page'] == 1
