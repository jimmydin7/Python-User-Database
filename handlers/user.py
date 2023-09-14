from utils import processor

class User:
    def __init__(self, usr, email, passwrd, db):
        self.usr = usr
        self.email = email
        self.passwrd = passwrd
        self.db = db

    def add_user(self):

        with open(self.db, 'r') as db:
            lines = db.readlines()
            line_count = len(lines)
            id = line_count + 1

        full_string = str(id)+":"+self.usr+":"+self.email+":"+self.passwrd
        text = processor.TextProcesser(full_string)
        encoded = str(text.encrypt())


        
            
        
        db.close()

        with open(self.db, 'a') as db:  # mode 'w' overwrites, I want to append so I right 'a'
            if id == 1:
                db.write(encoded)
            else:
                db.write('\n' + encoded)
        
        db.close()

    
       
