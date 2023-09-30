import requests, env
from assertpy import assert_that

#init header variable
base_url = env.BASE_URL
auth = env.PAYLOADAUTH
header = env.headers

#create function http req to get token
def get_token():
    return requests.post(f'{base_url}/tokens', data=auth)

#create function http request to get favorites airports data with status 200
def test_FavAirports_200():
    token = get_token()
    signIn = token.json()
    header["Authorization"] = "Bearer " + signIn.get("token")

    getFav = requests.get(f'{base_url}/favorites', headers=header)
    dataFav = getFav.json()

#do assertion on http request with json data
    assert_that(getFav.status_code).is_equal_to(200)
    assert_that(dataFav.get('data')[0]).is_not_empty
    assert_that(dataFav.get('data')[0].get('id')).is_type_of(str)
    assert_that(dataFav.get('data')[0].get('type')).is_equal_to('favorite')
    assert_that(dataFav.get('data')[0].get('attributes').get('airport')).is_not_empty
    assert_that(dataFav.get('links')).is_not_empty
    assert_that(dataFav.get('links').get('first')).contains('favorites')