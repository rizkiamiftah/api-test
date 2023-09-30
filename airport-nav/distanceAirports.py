import requests, env
from assertpy import assert_that

#init header variable
base_url = env.BASE_URL
payload = env.PAYLOADDISTANCE
idFrom = env.idFrom
idTo = env.idTo

#create function http request to post distance airports data with status 200
def test_distanceAirports_200():
    getDistance = requests.post(f'{base_url}/airports/distance', data=payload)
    dataDistance = getDistance.json()

#do assertion on http request with json data
    assert_that(getDistance.status_code).is_equal_to(200)
    assert_that(dataDistance.get('data')).is_not_empty
    assert_that(dataDistance.get('data').get('id')).is_type_of(str)
    assert_that(dataDistance.get('data').get('attributes')).is_not_empty
    assert_that(dataDistance.get('data').get('attributes').get('from_airport').get('iata')).is_equal_to(idFrom)
    assert_that(dataDistance.get('data').get('attributes').get('to_airport').get('iata')).is_equal_to(idTo)
    assert_that(dataDistance.get('data').get('attributes').get('kilometers')).is_type_of(float)
    assert_that(dataDistance.get('data').get('attributes').get('miles')).is_type_of(float)
    assert_that(dataDistance.get('data').get('attributes').get('nautical_miles')).is_type_of(float)

#create function http request to post distance airports data with status 422
def test_distanceAirports_422():
    getDistance = requests.post(f'{base_url}/airports/distance')
    dataDistance = getDistance.json()

#do assertion on http request with json data
    assert_that(getDistance.status_code).is_equal_to(422)
    assert_that(dataDistance.get('errors')[0]).is_not_empty
    assert_that(dataDistance.get('errors')[0].get('status')).is_equal_to('422')
    assert_that(dataDistance.get('errors')[0].get('title')).contains('Unable to process')
    assert_that(dataDistance.get('errors')[0].get('detail')).contains('enter valid')