class BetAPI:

    def __init__(self, client):
        self.client = client
    
    def list(self, params: dict={}):
        """
        Return a list of all your bets.
        """
        return self.client._make_request(endpoint='bets/', params=params)