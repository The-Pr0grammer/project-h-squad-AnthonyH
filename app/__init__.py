import os
from venv import create
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
import datetime

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),user=os.getenv("MYSQL_USER"), password=os.getenv("MYSQL_PASSWORD"), host=os.getenv("MYSQL_HOST"), port=3306)
print(mydb)

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/aboutMe')
def aboutMe():
    return render_template('about_me.html', title="MLH Fellow")

@app.route('/experience')
def experience():
    return render_template('experience.html', title="MLH Fellow")

@app.route('/travel')
def travel():
    return render_template('travel.html', title="MLH Fellow")

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="MLH Fellow")

@app.route('/education')
def education():
    return render_template('education.html', title="MLH Fellow")

class Timelinepost():
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([Timelinepost])