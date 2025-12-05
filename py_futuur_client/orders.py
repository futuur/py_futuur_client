class OrdersAPI:

    def __init__(self, client):
        self.client = client
    
    def list(self, params: dict = {}):
        """
        Retrieve a list of all limit orders placed by Outcome or Question for Real Money or Play Money.
        Endpoint: GET /api/v1/orders/
        """
        return self.client._make_request(endpoint='orders/', params=params)
