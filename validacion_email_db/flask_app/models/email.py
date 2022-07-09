
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self,data):
        self.data = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
        return connectToMySQL("esquema_email_db").query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails ORDER BY emails.id;"
        results = connectToMySQL("esquema_email_db").query_db(query)
        emails = []
        for row in results:
            emails.append( cls(row) )
        return emails


    @staticmethod
    def validate_email(email):
        is_valid = True
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL("esquema_email_db").query_db(query,email)
        if len(results) >= 1:
            flash("Email already taken.")
            is_valid=False
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid Email!!!")
            is_valid=False
        if  EMAIL_REGEX.match(email['email']):
            flash("Your email is correct")
        return is_valid