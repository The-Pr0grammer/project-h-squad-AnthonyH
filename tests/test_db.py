import unittest
from peewee import *
from app import TimelinePost

MODELS = [TimelinePost]

test_db = SqliteDatabase( ':memory:' )

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        first_post = TimelinePost.create(date='5/20/22', title='Title1', events='Hello, my name is Joe Biden and I am the president.')
        assert first_post.id == 1

        second_post = TimelinePost.create(date='6/20/22', title='Title2', events='Hello, my name is Joe and I am the president.')
        assert second_post.id == 2  