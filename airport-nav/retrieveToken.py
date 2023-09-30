import requests, env
from assertpy import assert_that

#init header variable
base_url = env.BASE_URL
payload = env.PAYLOADAUTH
token = env.TOKEN

#create function http request to post retrieve token data with status 200
def test_retrieveToken_200():
    getToken = requests.post(f'{base_url}/tokens', data=payload)
    dataToken = getToken.json()

#do assertion on http request with json data
    assert_that(getToken.status_code).is_equal_to(200)
    assert_that(dataToken.get('token')).is_equal_to(token)

#create function http request to post retrieve token data with status 401
def test_retrieveToken_401():
    getToken = requests.post(f'{base_url}/tokens')
    dataToken = getToken.json()

#do assertion on http request with json data
    assert_that(getToken.status_code).is_equal_to(401)
    assert_that(dataToken.get('errors')[0].get('status')).is_equal_to("401")
    assert_that(dataToken.get('errors')[0].get('title')).is_equal_to("Unauthorized")
    assert_that(dataToken.get('errors')[0].get('detail')).contains("not authorized")
