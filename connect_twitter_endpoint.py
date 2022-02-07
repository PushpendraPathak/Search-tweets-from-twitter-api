import requests


def bearer_oauth(r):
    bearer_token = 'AAAAAAAAAAAAAAAAAAAAAJavYwEAAAAAGKWbiFL1uSh%2B2VCjuOKzHrQOECI%3DdaUX3ObHN4lhBADqcNGev0G3WIVEqb06VxBeGrTqx3rEUCA4BW'
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    #requesting data fetch from twitter recent search api through bearer token auth
    response = requests.get(url, auth=bearer_oauth, params=params)
    if response.status_code == 429:
        return None,response.status_code
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json(),response.status_code