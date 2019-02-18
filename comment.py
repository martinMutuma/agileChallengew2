import datetime

logged_in_user=[] 
comments = []
class Comment:
    def __init__(self, author=None, message=None, replied_to=None,created_at=None):
        self.id = self.generate_id()
        self.author = logged_in_user
        self.message = message
        self.replied_to = replied_to
        self.created_at  = datetime.datetime.now()

    def generate_id(self, id=0):
        """Incremental generation of list ids
        
        Arguments:
     {[list]} -- The list to generate an id for
        
        Keyword Arguments:
            id {int} 
        Returns:
            [int] -- generated id
        """

        if id == 0:
            id = len(comments)+1

        for x in comments:
            if comments[x].id== id:
                id = id+1
                return self.generate_id(id)
        return id


    
    def save_comment(self):
        comments.append(self)

    def create_comment(self):
        message = str(input("Post comment"))
        author =str(input("Enter username"))
        self.__init__(2,author,message)
        self.save_comment()

   