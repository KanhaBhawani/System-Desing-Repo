from databases import Post, User, UserDB, PostDB, Post_User, FeedCache
from userManagement import UserManager

from publishing_service import Publisher
from subscribing_service import Subscriber

def createPost(content)->Post:
    post = Post(content)
    return post
    

def main():
    userDB = UserDB()
    postDB = PostDB()
    post_user = Post_User()
    mainFeed = FeedCache()
    userManager = UserManager(userDB)
    publisher = Publisher(userDB, mainFeed, postDB, post_user)
    subscriber = Subscriber(mainFeed)

    kanha = userManager.createUser("Kanha")

    kanhaposts = [createPost(f'kanha_{i}') for i in range(2)]
    goluposts = [createPost(f'golu_{i}') for i in range(2)]

    userManager.follow(kanha, golu)

    for post in kanhaposts:
        publisher.publish(kanha, post)

    for post in goluposts:
        publisher.publish(golu, post)

    post1 = subscriber.subscribe(kanha)
    print("Feed of kanha")
    for post in post1:
        newPost = postDB.getPost(post)
        print(newPost.content)
    post2 = subscriber.subscribe(golu)
    print("Feed of golu")
    for post in post2:
        newPost = postDB.getPost(post)
        print(newPost.content)




    




if __name__ == "__main__":
    main()