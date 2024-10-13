from databases import FeedCache, UserDB, Post, PostDB, Post_User

class Publisher:
    def __init__(self, userDB: UserDB, feed: FeedCache, postDB: PostDB, post_user: Post_User) -> None:
        self.userDB = userDB
        self.feed = feed
        self.postDB = postDB
        self.post_user = post_user

    def publish(self, userID, post: Post) -> None:
        user = self.userDB.getUser(userID)
        postID = self.postDB.addPost(post)
        self.post_user.addPost(postID, userID)

        followers = user.getFollowers()
        followers.append(userID)
        self.feed.populate(postID, followers)

    



