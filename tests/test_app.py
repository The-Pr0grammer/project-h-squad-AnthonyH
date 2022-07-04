from operator import truediv
import os
import unittest
os.environ['TESTING'] = 'true'
from app import app
from app import TimelinePost

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<em>anthonyh202x@gmail.com</em>" in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "posts" in json
        assert len(json["posts"]) == 0
        first_post = TimelinePost.create(date='07/04/1990', title='This is a Test', events='Hello, I am Anthony')
        assert first_post.id == 1


    #date, title, events
    def test_malformed_timeline_post(self):
        #No title in post
        response = self.client.post("/api/timeline_post", data = {"date": "12/25/22", "events": "Hello world, I am Kris!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid Title" in html

        #POST has empty body
        response = self.client.post("/api/timeline_post", data = {"date": "05/22/2022", "title": "This is a Title", "events": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid Body" in html

        #POST has no date
        response = self.client.post("/api/timeline_post", data = {"title": "Luis808@example.com", "events": "Hello world, I am Luis!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid Date" in html