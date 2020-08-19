import requests

ENDPOINT = 'https://swapi.py4e.com/api'

def get_resource(url, params=None, timeout=20):
    """Initiates an HTTP GET request to the SWAPI service in order to return a
    representation of a resource.

    Parameters:
        url (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    if params:
        response = requests.get(url, params=params, timeout=timeout).json()
    else:
        response = requests.get(url, timeout=timeout).json()

    return response


def main():
    """Entry point."""

    leia = get_resource(f"{ENDPOINT}/people", {"search":"leia"})['results'][0]

    print(leia['name'])



if __name__ == '__main__':
    main()
