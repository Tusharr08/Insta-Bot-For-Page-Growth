from instapy import InstaPy
from instapy import smart_run

session=InstaPy(username="--your--username--", password="----your--password---").login()
session.login()
#session.like_by_tags(["metaverse","nft","cryptocurrency"],amount=5 ,media="Photo" , interact=True) 

with smart_run(session):
    """ Activity flow """
    # general settings
    
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)
                                    
    session.like_by_tags(["mensfashion","nft","crypto","metaverse","nftmoney"], amount=10 ,interact=True)
    session.set_dont_include(["friend1", "friend2", "friend3"])
    #session.set_dont_like(["pizza", "#store"])
    session.set_dont_like(["naked","nsfw"])
    session.set_do_follow(True , percentage=50)
    session.set_comments(['Really Cool',"The Future is here!","Imma buy it real quick!","Dope"])
    session.set_do_comment(True , percentage=50)

    # activity
    session.like_by_tags(["mensfashion","nft","crypto","metaverse","nftmoney"], amount=10 ,interact=True)
session.end()