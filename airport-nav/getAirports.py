import requests, env
from assertpy import assert_that

#init header variable
BASE_URL = env.BASE_URL

#create function http request to get airport data with status 200
def test_getAirport_200():
    getAirports = requests.get(f'{BASE_URL}/airports')
    listAirports = getAirports.json()

#do assertion on http request with json data
    assert_that(getAirports.status_code).is_equal_to(200)
    assert_that(listAirports.get('data')).is_not_empty
    assert_that(listAirports.get('data')[0].get('id')).is_equal_to('GKA') #get object json with list array
    assert_that(listAirports.get('data')[0].get('attributes')).is_not_empty
    assert_that(listAirports.get('data')[0].get('attributes').get('country')).contains('Guinea')
    assert_that(listAirports.get('data')[0].get('attributes').get('altitude')).is_type_of(int)
    assert_that(listAirports.get('links')).is_not_empty
    assert_that(listAirports.get('links').get('first')).contains(BASE_URL)

#create function http request to get airport data with status 404
def test_getAirport_404():
    getAirports = requests.get(f'{BASE_URL}/airports/test')
    listAirports = getAirports.json()

#do assertion on http request with json data
    assert_that(getAirports.status_code).is_equal_to(404)
    assert_that(listAirports.get('errors')).is_not_empty
    assert_that(listAirports.get('errors')[0].get('status')).is_equal_to('404')
    assert_that(listAirports.get('errors')[0].get('title')).is_equal_to('Not Found')
    assert_that(listAirports.get('errors')[0].get('detail')).contains('not be found')

