class CategoryAPI:

    def __init__(self, client):
        self.client = client
    
    def list(self, params: dict={}):
        """
        Return list of categories
        """
        return self.client._make_request(endpoint='categories/', params=params)
    
    def get(self, id):
        """
        Return category detail
        """
        return self.client._make_request(endpoint=f'categories/{id}')
    