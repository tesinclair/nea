# External Imports

import sqlite3
from sqlite3 import Error
import os
import pygame
import hashlib


# Local Imports

import dependencies


# Initializations

dependencies.settings.init()


# Constants
CONN = sqlite3.connect("./nea_database.db") # Establishes connection with database
CURSOR = CONN.cursor()

# Variables
user = None

def execute_command(command, data=[]):
    try:
        result = CURSOR.execute(command, data).fetchall()
        if len(result) > 0: # If there is something returned
            return result # Return that # Else, just run the command
    except Error as e: print(e) # If command cannot be executed, print why


# Creates the tables required

def create_tables():
    setup_command_users = r"""   
    CREATE TABLE IF NOT EXISTS users(
        id integer PRIMARY KEY AUTOINCREMENT, 
        f_name varchar(15) NOT NULL,
        s_name varchar(20) NOT NULL,
        pass varchar(100) NOT NULL,
        username varchar(20) NOT NULL UNIQUE
    ); 
    """ # SQL query to create the user table

    setup_command_message = r""" 
    CREATE TABLE IF NOT EXISTS messages(
        message_id integer PRIMARY KEY AUTOINCREMENT,
        sender_username varchar(20),
        contact_username varchar(20),
        message text NOT NULL,
        message_date datetime default current_timestamp,
        FOREIGN KEY (sender_username) REFERENCES users (username),
        FOREIGN KEY (contact_username) REFERENCES users (username)
    );
    """ # SQL query to create the messages table

    # Executes query

    execute_command(setup_command_users)
    execute_command(setup_command_message)

# returns a list of messages between user and contact
def get_messages(username, contact):
    command = f"""
SELECT `message` FROM `messages` INNER JOIN `users` on  ;
"""
execute_command(command, data)


def add_message(message: str, username: str, contact: str):
    command = r"""
    INSERT INTO `messages` (`sender_username`, `contact_username`, message)
    VALUES(?, ?, ?);
    """
    execute_command(command, [username, contact, message])


def create_account(f_name, s_name, password, username):
    password_to_add = hash_pass(password)
    command = r"""
    INSERT INTO `users` (`f_name`, `s_name`, `pass`, `username`)
    VALUES(?, ?, ?, ?);
    """
    execute_command(command, [f_name, s_name, password_to_add, username])

def get_exists(username):
    command = r"""
    SELECT `username` FROM `users` WHERE `username` = ?; 
    """ # Sqlite3 variable management - question mark to be filled in by data
    result = execute_command(command, [username]) # passes through command, and the data
    if result:
        return True
    else:
        return False


def check_password(username, pass_to_check):
    hashed_pass_to_check = hash_pass(pass_to_check)
    command = r"""
    SELECT * FROM `users` WHERE `username` = ? AND `pass` = ?;
    """
    result = execute_command(command, [username, pass_to_check])
    if result: 
        return True
    else: 
        return False

def get_id(username):
    command = """
    SELECT `id` FROM `users` WHERE `username` = ?;
    """
    return execute_command(command, [username])

def get_name(username):
    command_f_name = '''
    SELECT `f_name` FROM `users` WHERE `username` = ?;
    '''
    command_s_name = '''
    SELECT `s_name` FROM `users` WHERE `username` = ?;
    '''
    f_name = execute_command(command_f_name, [username])
    s_name = execute_command(command_s_name, [username])
    return f_name, s_name

def search(text):
    command = '''
    SELECT * FROM `users` WHERE `username` LIKE ?
    '''
    return execute_command(command, ['%'+text+'%']) # using sql wildcard % to return all usernames like this

def hash_pass(password: str):
    return hashlib.sha224(password.encode("UTF-8")).hexdigest()


''' Taking advantage of python being interpreted
I can invoke create_tables() when the database handler
is called which allows a neater solution than calling it in main'''
create_tables() 
