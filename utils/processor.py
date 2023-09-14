import base64

class TextProcesser:

    def __init__(self, text):
        self.text = text
    
    def encrypt(self):
        
        #return base64.b64encode(bytes(self.text, 'utf-8'))
        return self.text
    
    def show_raw(self, text):
        
        if text == "":
            print("[!] Database is empty! You can add users with the command 'add'!")
        else:
            text = text.replace(":", " - ")
    
            print(" ")
            print("ID - Name - Email - Password")
            print(" ")
            print(text)
            print(" ")
    
    def show_help(self):
        print("""
              
Available Commands:

1. set db [filename.jdb]: Set the current database file to the specified .jdb file or create a new database with the given filename.
   Example: set db my_database.jdb

2. add: Add a new user to the current database.
   Example: add
                    
3. search [content]: Searches for user records containing the specified content in the current database. It will display matching user details.
   Example: search jim

4. show db: Display the currently selected database filename.
   Example: show db

5. show user [id]: Display user details by their ID in the current database.
   Example: show user 1

6. show raw: Display the raw content of the current database.

7. help: Show this help menu.

8. exit or quit: Exit the database console.

Note: You must select a .jdb database using 'set db [filename.jdb]' to create or use an existing database.

""")

        



    
 
        