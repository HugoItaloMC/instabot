from src.factory.abs import AbstractLike, AbstractComment, AbstractFollow, AbstractUnfollow

#### CONCRETS CLASS  ##########################
class Like(AbstractLike): flush = ...         #
                                              #
class Comment(AbstractComment): flush = ...   #
                                              #
class Follow(AbstractFollow): flush = ...     #
                                              #
class Unfollow(AbstractUnfollow): flush = ... #
###############################################

class AbstractFactory:

    def _like(self):
        return Like()

    def _comment(self):
        return Comment()
    
    def _follow(self):
        return Follow()

    def _unfollow(self):
        return Unfollow()
    
