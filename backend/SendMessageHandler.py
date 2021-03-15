import backend

def send_message(message, user, contact):
    backend.DatabaseHandler.add_message(message, user, contact)

    #TODO: 
    # - move this geezer to frontend handlers