from handlers import error_console
from handlers import user
from utils import processor


logo = """                       
          / /                 //    ) ) //   ) ) 
         / / ( )  _   __     //    / / //___/ /  
        / / / / // ) )  ) ) //    / / / __  (    
       / / / / // / /  / / //    / / //    ) )   
 ((___/ / / / // / /  / / //____/ / //____/ /   

                Database Console

"""


print(logo)

db_filename = None

while True:
    cmd = input("[>] ").split(' ')

    if cmd[0] == "exit" or cmd[0] == "quit":
        quit()
    
    elif cmd[0] == "set":
        err = error_console.Error(cmd="set")
        try:
            if cmd[1] == "db":
                db_filename = cmd[2]
                if ".jdb" in db_filename:
                    
                    with open(db_filename, 'a') as f:
                        f.write("")
                    print(f"[+] Successfully set the database to '{db_filename}'")

                else:
                    err.spit_error(id=1)
    
        except Exception as e:
            err.spit_error(id=0)
        
    elif cmd[0] == "add":

        if db_filename == None:
            print("[!] Select a database first with the command 'set'!")
        
        else:
            usr = input("[username > ] ")
            email = input("[email >] ")
            passwrd = input("[password > ] ")
            
            decision = input(f"[?] Confirm addition (y/n) > ")      

            if decision == "y":

                current = user.User(usr=usr,email=email,passwrd=passwrd, db=db_filename)
                current.add_user()
                print(f"[+] Successfully added user on '{db_filename}'!")

            else:
                print("[+] Cancelled addition")
    
    elif cmd[0] == "show":
        err = error_console.Error(cmd="show")
        if db_filename != None:
            try:
                if cmd[1] == "db":
                    print(f"[+] The current database is set to '{db_filename}'!")

                elif cmd[1] == "user":
                    
                    try:
                        try:

                            def show_by_id(user_id):
                                

                                with open(db_filename, 'r') as db:
                                    
                                    found_id = False

                                    full_id_string = str(user_id) + ":"

                                    for line in db:
                                        if full_id_string in line:
                                            found_id = True
                                            parts = line.split(":")
                                            print(f"""
ID        : {parts[0]}
Name      : {parts[1]}
Email     : {parts[2]}
Password  : {parts[3]}
""")
                                    if found_id:
                                        pass
                                    else:
                                        print(f"[!] Couldn't find a user with the ID {user_id}!")
                            show_by_id(user_id=int(cmd[2]))
                                

                            
                        except Exception as e:
                            err.spit_error(id=2)

                
                        
                    
                    except Exception as e:
                        err.spit_error(id=0)

                elif cmd[1] == "raw":
                    with open(db_filename, 'r') as db:
                        
                        content = db.read()

                        current_content = processor.TextProcesser(text=content)
                        current_content.show_raw(text=content)

                


       

                
            except Exception as e:
                err.spit_error(id=1)
                
        else:
            print("[!] You haven't selected a database, select one with the command 'set'!")


    elif cmd[0] == "search":
        

        if db_filename:
            content = cmd[1]

            found_user = False

            with open(db_filename, 'r') as db:

                for line in db:
                    if content in line:
                        if found_user:
                            pass
                        else:
                            print(" ")
                            print("[+] Found user(s)!")
                        found_user = True
                        parts = line.split(":")
                        print(f"""
-------------------------------                      
ID        : {parts[0]}
Name      : {parts[1]}
Email     : {parts[2]}
Password  : {parts[3]}
-------------------------------
""")
         


            if found_user:
                pass
            else:
                print(f"[!] Couldn't find '{content}' in the database.")
        else:
            print("[!] You haven't selected a database, select one with the command 'set'!")


    elif cmd[0] == "help":
        menu = processor.TextProcesser(text=None)
        menu.show_help()
               
            

            
               
    else:
        if cmd[0] == "":
            pass
        else:
            print(f'[!] Unrecognized command, type "help" for help')