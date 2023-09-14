class Error:
    def __init__(self, cmd):
        self.cmd = cmd

    def spit_error(self, id):
        if self.cmd == "set":
            if id == 0:
                print("[!] Invalid arguments. Use 'set db [database.jdb]'")
            elif id == 1:
                print("[!] Invalid arguments. File extension must be '.jdb'!")
        
        if self.cmd == "show":
            if id == 0:
                print("[!] Invalid arguments, please specify the user ID. Use 'show user [id]'")
            elif id == 1:
                print("[!] Missing arguments! The command 'show' takes either a 'db', 'user' or 'raw' argument!")
            elif id == 2:
                print("[!] An error occured, make sure to include the ID number!")
        
        