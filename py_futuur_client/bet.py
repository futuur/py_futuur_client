from urllib import request


class BetAPI:

    def __init__(self, client):
        self.client = client
    
    def list(self, params: dict={}):
        """
        Return a list of all your bets.
        """
        return self.client._make_request(endpoint='bets/', params=params)
    
    def purchase(self, payload: dict):
        """
        Bet on a market by purchasing an outcome position.

        Position Long: Bet in favor of a specific outcome. You win if the selected outcome occurs.

        Position Short: Bet against a specific outcome. You win if any other outcome occurs.
        """
        return self.client._make_request(method='POST' ,endpoint='bets/', payload=payload)
