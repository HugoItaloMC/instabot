from src.factory.rules.abs import *
__all__ = ['Login', 'Like', 'Comment', 'Follow', 'Unfollow']

############# CONCRETS CLASS  #################
# Attr `run` apontado na meta-class          ##
# refrênciando descritor da classe Handler   ##
                                             ##
class Login(AbstractLogin): run = ...        ##
                                             ##
class Like(AbstractLike): run = ...          ##
                                             ##
class Comment(AbstractComment): run = ...    ##
                                             ##
class Follow(AbstractFollow): run = ...      ##
                                             ##
class Unfollow(AbstractUnfollow): run = ...  ##
###############################################