from pymongo import MongoClient

class DBStorage():
    def __init__(self, mongoClient=None):
      if (mongoClient==None):
        self._client = MongoClient()
      else:
        self._client = mongoClient
      self._db = self._client.airodb
      self.dumps = self._db.airodb_dumps

    def __del__(self): 
      self._client.close()

    def insert(self, dumps):
      self.dumps.insert_many(dumps)

    def isSessionNameAlreadyExist(self, sessionName):
      return (self.dumps.count_documents({"SessionName": sessionName}) > 0)

        
