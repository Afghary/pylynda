import pymongo

class Database(object):
    # static property

    # Universal Resource Identifier
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['pylynda']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def update(collection, query, changes):
        return Database.DATABASE[collection].update(query, changes)

    @staticmethod
    def find_one(collection, query):
        # find_one method returns the first json found
        # despite find witch returns a cursor object.
        return Database.DATABASE[collection].find_one(query)
