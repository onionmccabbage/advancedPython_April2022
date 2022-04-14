import requests # needed to call end-point APIs

class DoStuff():
    def __init__(self):
        pass
    def makecall(self, cat, id):
        url='https://jsonplaceholder.typicode.com/{}/{}'.format(cat, id)
        response = requests.get(url) # make a call to the API
        data = response.json() # the API retuns JSON
        print(data)

if __name__ == '__main__':
    d = DoStuff()
    d.makecall('photos', 9)