def json_to_dict(path):
    import json
    with open(path) as json_file:
        return json.load(json_file)


def download(url, path):
    import requests
    r = requests.get(url, allow_redirects=True)
    open(path, 'wb').write(r.content)

