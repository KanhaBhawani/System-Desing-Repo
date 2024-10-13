class Database:
    def __init__(self) -> None:
        self.id_counter = 0
        self.data_array = {}
        self.Schema = []

class Post:
    def __init__(self, content) -> None:
        self.content = content

class User:
    def __init__(self, name, metadata = []) -> None:
        self.name = name
        self.metadata = metadata
        self.follower = []
        self.following = []
    
    def addFollower(self, userID):
        self.follower.append(userID)

    def addFollowing(self, userID):
        self.following.append(userID)
    
    def getFollowers(self):
        return self.follower.copy()

class PostDB(Database):
    def __init__(self) -> None:
        super().__init__()
        self.Schema = ["POST ID", "POST"]

    def addPost(self, post:Post)->int:
        _id = self.id_counter
        self.id_counter += 1
        self.data_array[_id] = post
        return _id

    def getPost(self, postID):
        if(postID not in self.data_array):
            return None
        return self.data_array[postID]

class Post_User(Database):
    def __init__(self) -> None:
        super().__init__()
        self.Schema = ["postID", "userID"]
    
    def addPost(self, postID: int, userID: int):
        self.data_array[postID] = userID
    
class UserDB(Database):
    def __init__(self) -> None:
        super().__init__()
        self.Schema = ["userID", "user"]
    
    def addUser(self, user: User) -> None:
        _id = self.id_counter
        self.id_counter += 1
        self.data_array[_id] = user
        return _id
    
    def getUser(self, userID)->User:
        if(userID not in self.data_array):
            return None
        return self.data_array[userID]
        
class FeedCache(Database):
    def __init__(self) -> None:
        super().__init__()
        self.Schema = ['UserId', "['list of PostIDs']"]
    
    def populate(self, postID, userID_List) -> None: 
        for userID in userID_List:       
            if(userID not in self.data_array):
                self.data_array[userID] = []
            
            self.data_array[userID].append(postID)
    
    def get_feed(self, userID)->list:
        if(userID not in self.data_array):
            return []
        return self.data_array[userID]
    
    def checkUserAvailable(self, userID)->bool:
        if(userID in self.data_array):
            return True
        return False