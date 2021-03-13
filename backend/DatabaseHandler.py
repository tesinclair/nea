# External Imports

import sqlite3
from sqlite3 import Error
import os
import pygame


# Local Imports

import dependencies


# Initializations

dependencies.settings.init()


# Constants
CONN = sqlite3.connect("../nea_database.db") # Establishes connection with database
CURSOR = CONN.cursor()

def execute_command(command):
    try:
        CURSOR.execute(command)
    except Error as e: print(e) # If command cannot be executed, print why


# Creates the tables required

def create_tables():
    setup_command_users = r"""   
    CREATE TABLE IF NOT EXISTS users(
        id integer PRIMARY KEY AUTOINCREMENT, 
        f_name varchar(15) NOT NULL,
        s_name varchar(20) NOT NULL,
        pass varchar(100) NOT NULL,
        username varchar(20) NOT NULL
    ); 
    """ # SQL query to create the user table

    setup_command_message = r""" 
    CREATE TABLE IF NOT EXISTS messages(
        message_id integer PRIMARY KEY AUTOINCREMENT,
        sender_id integer,
        receiver_id integer,
        message text NOT NULL,
        message_date date,
        FOREIGN KEY (sender_id) REFERENCES users (id),
        FOREIGN KEY (receiver_id) REFERENCES users (id)
    );
    """ # SQL query to create the messages table

    # Executes query

    execute_command(setup_command_users)
    execute_command(setup_command_message)

# returns a list of messages between user and contact
# def get_messages(username, contact):
#     command = f"""
# SELECT `message` FROM `messages` JOIN users WHERE `username` = '{username}' AND 'recipient_id' = '{recipient_id}';
# """
# execute_command(CONN, command)


# def add_message(message: str, user_id: str, recipient_id: str):
#     command = f"""
#     INSERT INTO 'messages' (sender_id, receiver_id, message)
#     VALUES('{user_id}', '{recipient_id}', '{message}');"""
#     execute_command(CONN, command)


def add_account(f_name, s_name, password, username):
    password_to_add = hash_pass(password)
    command = f"""
    INSERT INTO 'users' (f_name, s_name, pass, username)
    values('{f_name}', '{s_name}', '{password_to_add}', '{username}');"""
    execute_command(command)

def get_exists(username):
    command = """
    SELECT 'username' FROM 'users' WHERE 'username' = '{username}';
    """
    result = execute_command(command)
    if result:
        return True
    else:
        return False


def check_password(pass_to_check, username):
    hashed_pass_to_check = hash_pass(pass_to_check)
    command = """
    SELECT * FROM 'users' WHERE 'username' = '{username}' AND 'pass' = '{hashed_pass_to_check}';
    """
    if execute_command(command): return True
    else: return False

# def get_id(username):
#     command = """
#     SELECT 'user_id' FROM 'users' WHERE 'username' = '{username}';
#     """
#     return execute_command(CONN, command)

def hash_pass(password: str):
    return hashlib.sha224(password.encode("UTF-8")).hexdigest()


''' Taking advantage of python being interpreted
I can invoke create_tables() when the database handler
is called which allows a neater solution than calling it in main'''
create_tables() 