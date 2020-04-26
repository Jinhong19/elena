import requests
import urllib
import urllib3

class eleFinder:

    def make_remote_request(self, url: str, params: dict):
        """
        Makes the remote request
        Continues making attempts until it succeeds
        """

        count = 1
        while True:
            try:
                response = requests.get((url + urllib.parse.urlencode(params)))
            except (OSError, urllib3.exceptions.ProtocolError) as error:
                print('\n')
                print('*' * 20, 'Error Occured', '*' * 20)
                print(f'Number of tries: {count}')
                print(f'URL: {url}')
                print(error)
                print('\n')
                count += 1
                continue
            break

        return response
    
    def getEle(self, lat, lon):
        url = 'https://nationalmap.gov/epqs/pqs.php?'
        params = {'x': lon,
                'y': lat,
                'units': 'Meters',
                'output': 'json'}
        result = self.make_remote_request(url, params)
        return result.json()['USGS_Elevation_Point_Query_Service']['Elevation_Query']['Elevation']

