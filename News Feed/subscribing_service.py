from databases import FeedCache

class Subscriber:
    def __init__(self, feed: FeedCache) -> None:
        self.feed = feed
        self.max_feed = 10
    
    def subscribe(self, userID)-> list:
        if(not self.feed.checkUserAvailable(userID)):
            return []

        return self.feed.get_feed(userID)[-self.max_feed:]