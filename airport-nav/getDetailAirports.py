import requests, env
from assertpy import assert_that

#init header variable
base_url = env.BASE_URL
idAirports = env.idAirports
emptyID = " "
numberID = 12334

#create function http request to get airport data with status 200
def test_getDetailAirport_200():
    getDetailAirports = requests.get(f'{base_url}/airports/{idAirports}')
    listDetailAirports = getDetailAirports.json()

#do assertion on http request with json data
    assert_that(getDetailAirports.status_code).is_equal_to(200)
    assert_that(listDetailAirports.get('data')).is_not_empty
    assert_that(listDetailAirports.get('data').get('id')).is_equal_to(idAirports)
    assert_that(listDetailAirports.get('data').get('attributes').get('iata')).is_equal_to(idAirports)
    assert_that(listDetailAirports.get('data').get('attributes').get('altitude')).is_type_of(int)
    assert_that(listDetailAirports.get('data').get('attributes').get('name')).is_type_of(str)
    assert_that(listDetailAirports.get('data').get('attributes').get('city')).is_type_of(str)
    assert_that(listDetailAirports.get('data').get('attributes').get('country')).is_type_of(str)
    assert_that(listDetailAirports.get('data').get('attributes').get('timezone')).is_type_of(str)

#create function http request to get airport data with status 404 not found (empty id)
def test_getDetailAirportEmpty_404():
    getDetailAirports = requests.get(f'{base_url}/airports/{emptyID}')
    listDetailAirports = getDetailAirports.json()

#do assertion on http request with json data
    assert_that(getDetailAirports.status_code).is_equal_to(404)
    assert_that(listDetailAirports.get('errors')).is_not_empty
    assert_that(listDetailAirports.get('errors')[0].get('status')).is_equal_to('404')
    assert_that(listDetailAirports.get('errors')[0].get('title')).is_equal_to('Not Found')
    assert_that(listDetailAirports.get('errors')[0].get('detail')).contains('not be found')

#create function http request to get airport data with status 404 not found (number type)
def test_getDetailAirportNumber_404():
    getDetailAirports = requests.get(f'{base_url}/airports/{numberID}')
    listDetailAirports = getDetailAirports.json()

#do assertion on http request with json data
    assert_that(getDetailAirports.status_code).is_equal_to(404)
    assert_that(listDetailAirports.get('errors')).is_not_empty
    assert_that(listDetailAirports.get('errors')[0].get('status')).is_equal_to('404')
    assert_that(listDetailAirports.get('errors')[0].get('title')).is_equal_to('Not Found')
    assert_that(listDetailAirports.get('errors')[0].get('detail')).contains('not be found')