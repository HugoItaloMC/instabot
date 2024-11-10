from src.factory.rules.abs import *
__all__ = ['Login', 'Like', 'Comment', 'Follow', 'Unfollow']

#### CONCRETS CLASS  ########################
#`run` refrência descritor da classe Handler#
                                            #
class Login(AbstractLogin):                 #
    run = ...                               #
    def __init__(self, data: tuple):        #
        super().__init__(data)              #
                                            #
                                            #
class Like(AbstractLike): run = ...         #
                                            #
class Comment(AbstractComment): run = ...   #
                                            #
class Follow(AbstractFollow): run = ...     #
                                            #
class Unfollow(AbstractUnfollow): run = ... #
#############################################