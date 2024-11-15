import json
__all__ = ['UsersJsonUtils']
class UsersJsonUtils:

    def __init__(self, path: str):
        self.__path = path
        self.__users: set = set()
        with open(self.__path, "r+") as jsonfile:
            usersjson = json.loads(jsonfile.read())
            for _, valur in usersjson.items():
                for users in valur:
                    self.__users.add(users)
    
    def __iter__(self):
        yield self.__users
        raise StopIteration
