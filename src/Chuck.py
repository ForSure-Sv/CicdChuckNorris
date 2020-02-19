import requests


class ChuckNorris:
    """
    @ref: https://api.icndb.com
    """

    @staticmethod
    def RandomJoke(NumOfJokes):

        api_result = requests.get('https://api.icndb.com/jokes/random/' + str(NumOfJokes))

        api_response = api_result.json()
        #print(api_response)

        return api_response['value']

    @staticmethod
    def specificJoke(numOfJoke):
        api_result = requests.get('https://api.icndb.com/jokes/' + str(numOfJoke))
        api_response = api_result.json()
        return api_response

    @staticmethod
    def ByCatagory(catagories):
        api_result = requests.get('https://api.icndb.com/jokes/random?LimitTo=' + str(catagories))
        api_response = api_result.json()
        return api_response

    @staticmethod
    def getJoke(num):
       for i in ChuckNorris.RandomJoke(num):
           print(i['joke'])

    @staticmethod
    def getSpecificJoke():
        numOfJoke = input("Enter Joke Number:")
        print(ChuckNorris.specificJoke(numOfJoke)['value']['joke'])

    @staticmethod
    def getByCatagory():
        catagories = list()
        n = int(input("Enter number of catagories :"))
        for i in range(0, n):
            ele = input()
            catagories.append(ele)
        print(ChuckNorris.ByCatagory(catagories)['value']['joke'])
