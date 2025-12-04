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
    
    def list_featured(self):
        """
        Return top 10 featured categories highest volume first.
        Endpoint: GET /api/v1/categories/featured/
        """
        return self.client._make_request(endpoint='categories/featured/')
    
    def list_main(self):
        """
        List all active categories marked as main
        Endpoint: GET /api/v1/categories/main/
        """
        return self.client._make_request(endpoint='categories/main/')