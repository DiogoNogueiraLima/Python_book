class Client:
    def __init__(self):
        print("Setting up the client...")
    
    def query(self, **kwargs):
        print(f"Performing a query: {kwargs}")

class Manager:
    @property
    def client(self):
        return Client()
    
    def perform_query(self, **kwargs):
        return self.client.query(**kwargs)
    
class ManualCacheManager:
    @property
    def client(self):
        if not hasattr(self, '_client'):
            self._client = Client()
        return self._client
    
from functools import cached_property

class CachedPropertyManager:
    @cached_property
    def client(self):
        return Client()
    
    def perform_query(self, **kwargs):
        return self.client.query(**kwargs)

manager = CachedPropertyManager()
manager.perform_query(object_id=42)
manager.perform_query(name_ilike='%Python%')
del manager.client  # Isso causará um novo Cliente na próxima chamada
manager.perform_query(age_gte=18)
