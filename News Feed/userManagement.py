from databases import UserDB, User

class UserManager:
    def __init__(self, userDB:UserDB) -> None:
        self.userDB = userDB

    def createUser(self, name) -> int:
        user = User(name)
        id = self.userDB.addUser(user)
        return id

    def follow(self, mainUserID, secUserID)->None:
        mainUser = self.userDB.getUser(mainUserID)
        secUser = self.userDB.getUser(secUserID)

        if(secUser is None):
            print(f"user with id {secUserID} doesn't exists...")
            return
        
        mainUser.addFollowing(secUserID)
        secUser.addFollower(mainUserID)

        # add n posts of sec user to the news feed of main user 
        # get latest n posts of sec uses and add them in the top of main user

