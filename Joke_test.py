import unittest
from unittest.mock import Mock, patch
from src.Chuck import ChuckNorris


class ChuckTestCase(unittest.TestCase):
    @patch('src.Chuck.requests.get')
    def test_specific_joke_and_id(self, mock_get):
        # mock initialization part
        joke_information = { "type": "success", "value": { "id": 100, "joke": "Chuck Norris grinds his coffee with his teeth and boils the water with his own rage.", "categories": [] } }
        joke_information1 = { "type": "success", "value": { "id": 37, "joke": "If you spell Chuck Norris in Scrabble, you win. Forever.", "categories": [] } }
        joke_information2 = { "type": "success", "value": { "id": 52, "joke": "When Chuck Norris sends in his taxes, he sends blank forms and includes only a picture of himself, crouched and ready to attack. Chuck Norris has not had to pay taxes, ever.", "categories": [] } }
        joke_information3 = { "type": "success", "value": { "id": 17, "joke": "Chuck Norris does not teabag the ladies. He potato-sacks them.", "categories": ["explicit"] } }
        joke_information4 = { "type": "success", "value": { "id": 19, "joke": "In an average living room there are 1,242 objects Chuck Norris could use to kill you, including the room itself.", "categories": [] } }


        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        #1
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = joke_information
        # assume
        stub = 100
        # expected
        expected = 'Chuck Norris grinds his coffee with his teeth and boils the water with his own rage.'
        # action
        joke_result = ChuckNorris.specificJoke(stub)
        # assert
        self.assertEqual(joke_result['value']['id'], stub)
        self.assertEqual(joke_result['value']['joke'], expected)

        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        #2
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = joke_information1
        # assume
        stub = 37
        # expected
        expected = 'If you spell Chuck Norris in Scrabble, you win. Forever.'
        # action
        joke_result = ChuckNorris.specificJoke(stub)
        # assert
        self.assertEqual(joke_result['value']['id'], stub)
        self.assertEqual(joke_result['value']['joke'], expected)

        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        #3
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = joke_information2
        # assume
        stub = 52
        # expected
        expected = "When Chuck Norris sends in his taxes, he sends blank forms and includes only a picture of himself, crouched and ready to attack. Chuck Norris has not had to pay taxes, ever."
        # action
        joke_result = ChuckNorris.specificJoke(stub)
        # assert
        self.assertEqual(joke_result['value']['id'], stub)
        self.assertEqual(joke_result['value']['joke'], expected)

        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        #4
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = joke_information3
        # assume
        stub = 17
        # expected
        expected = 'Chuck Norris does not teabag the ladies. He potato-sacks them.'
        # action
        joke_result = ChuckNorris.specificJoke(stub)
        # assert
        self.assertEqual(joke_result['value']['id'], stub)
        self.assertEqual(joke_result['value']['joke'], expected)

        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        #5
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = joke_information4
        # assume
        stub = 19
        # expected
        expected = 'In an average living room there are 1,242 objects Chuck Norris could use to kill you, including the room itself.'
        # action
        joke_result = ChuckNorris.specificJoke(stub)
        # assert
        self.assertEqual(joke_result['value']['id'], stub)
        self.assertEqual(joke_result['value']['joke'], expected)

    @patch('src.Chuck.requests.get')
    def test_joke_by_catagories(self, mock_get):
        # mock initialization part
        joke_information = { "type": "success", "value": { "id": 529, "joke": "Chuck Norris doesn't use Oracle, he is the Oracle.", "categories": ["nerdy"] } }
        joke_information1 = { "type": "success", "value": { "id": 450, "joke": "Chuck Norris doesn't have disk latency because the hard drive knows to hurry the hell up.", "categories": ["nerdy"] } }
        joke_information2 = { "type": "success", "value": { "id": 448, "joke": "When Chuck Norris throws exceptions, it's across the room.", "categories": ["nerdy"] } }
        joke_information3 = { "type": "success", "value": { "id": 379, "joke": "Chuck Norris' penis is a third degree blackbelt, and an honorable 32nd-degree mason.", "categories": ["explicit"] } }
        joke_information4 = { "type": "success", "value": { "id": 293, "joke": "70% of a human's weight is water. 70% of Chuck Norris' weight is his dick.", "categories": ["explicit"] } }

        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        # 1
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = joke_information
        # assume
        stub = list('nerdy')
        # expected
        expected = ['nerdy']
        # action
        joke_result = ChuckNorris.ByCatagory(stub)
        # assert
        self.assertEqual(joke_result['value']['categories'], expected)


        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        # 2
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = joke_information1
        # assume
        stub = list('nerdy')
        # expected
        expected = ['nerdy']
        # action
        joke_result = ChuckNorris.ByCatagory(stub)
        # assert
        self.assertEqual(joke_result['value']['categories'], expected)


        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        # 3
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = joke_information2
        # assume
        stub = list('nerdy')
        # expected
        expected = ['nerdy']
        # action
        joke_result = ChuckNorris.ByCatagory(stub)
        # assert
        self.assertEqual(joke_result['value']['categories'], expected)

        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        # 4
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = joke_information3
        stub = list('explicit')
        # expected
        expected = ['explicit']
        # action
        joke_result = ChuckNorris.ByCatagory(stub)
        # assert
        self.assertEqual(joke_result['value']['categories'], expected)


        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        # 5
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = joke_information4
        # assume
        stub = list('explicit')
        # expected
        expected = ['explicit']
        # action
        joke_result = ChuckNorris.ByCatagory(stub)
        # assert
        self.assertEqual(joke_result['value']['categories'], expected)


if __name__ == '__main__':
    unittest.main()
