class User(object):
    def __init__(self, username, user_id, f_name, s_name):
        self.username = username
        self.user_id = user_id
        self.f_name = f_name
        self.s_name = s_name
    
    def get_username(self): return self.username
    def get_user_id(self): return self.user_id
    def get_f_name(self): return self.f_name
    def get_s_name(self): return self.s_name