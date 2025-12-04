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

    def detail(self, id):
        """
        Return information on your bet, on a given market, for an outcome and currency.
        """
        return self.client._make_request(endpoint=f'bets/{id}')
    
    def sell(self, id, payload: dict):
        """
        Sell your entire position (previously purchased) on an outcome for a given currency.
        To sell the entire position, send a PATCH request with the bet ID.
        For a partial sale, include the number of shares in the request body using the 'shares' field.
        """
        if not payload:
            payload = dict()

        return self.client._make_request(method='PATCH', endpoint=f'bets/{id}/', payload=payload)
    
    def get_partial_amount_on_sell(self, id, payload: dict):
        """
        Calculates the amount that a user will receive if they sell a portion of their shares.
        """
        if not payload:
            payload = dict()

        return self.client._make_request(endpoint=f'bets/{id}/get_partial_amount_on_sell/', payload=payload)

    