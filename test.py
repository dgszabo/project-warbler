from project import app,db
from project.users.models import User
from project.messages.models import Message
from flask_testing import TestCase
import unittest

class BaseTestCase(TestCase):
    def create_app(self):
        app.config['WTF_CSRF_ENABLED'] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///testing.db'
        return app

    def setUp(self):
        db.drop_all()
        db.create_all()
        user1 = User(full_name = 'Test Person 1', username = 'test_person_1', password = 'test_person_1', location = 'Berkeley, CA', bio = '1 test bio about a very interesting life', email = 'test1@test.test', image_url = 'some_picture_1.jpg', header_image_url = 'some_header_1.png')
        user2 = User(full_name = 'Test Person 2', username = 'test_person_2', password = 'test_person_2', location = 'Berkeley, CA', bio = '2 test bio about a very interesting life', email = 'test2@test.test', image_url = 'some_picture_2.jpg', header_image_url = 'some_header_2.png')
        user3 = User(full_name = 'Test Person 3', username = 'test_person_3', password = 'test_person_3', location = 'Berkeley, CA', bio = '3 test bio about a very interesting life', email = 'test3@test.test', image_url = 'some_picture_3.jpg', header_image_url = 'some_header_3.png')
        db.session.add_all([user1, user2, user3])
        message1 = Message("test message 1", 1)
        message2 = Message("test message 2", 1)
        message3 = Message("test message 3", 2)
        message4 = Message("test message 4", 3)
        db.session.add_all([message1, message2, message3,message4])
        db.session.commit()

    def tearDown(self):
        db.drop_all()

    #### USER TESTS ####

    def test_users_index(self):
        response = self.client.get('/users', content_type='html/text', follow_redirects=True)
        from IPython import embed; embed()
        self.assertLess(response.status_code, 400)
        self.assertIn(b'Elie Schoppik', response.data)
        self.assertIn(b'Tim Garcia', response.data)
        self.assertIn(b'Matt Lane', response.data)

    def test_users_show(self):
        response = self.client.get('/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Matt Lane', response.data)

    # def test_users_create(self):
    #     response = self.client.post(
    #         '/users/',
    #         data=dict(first_name="Awesome", last_name="Student"),
    #         follow_redirects=True
    #     )
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn(b'Awesome', response.data)
    #     self.assertIn(b'User Created!', response.data)

    # def test_users_edit(self):
    #     response = self.client.get(
    #         '/users/1/edit'
    #     )
    #     self.assertIn(b'Elie', response.data)
    #     self.assertIn(b'Schoppik', response.data)

    # def test_users_update(self):
    #     response = self.client.patch(
    #         '/users/1?_method=PATCH',
    #         data=dict(first_name="updated", last_name="information"),
    #         follow_redirects=True
    #     )
    #     self.assertIn(b'updated information', response.data)
    #     self.assertNotIn(b'Elie Schoppik', response.data)

    # def test_users_delete(self):
    #     response = self.client.delete(
    #         '/users/1?_method=DELETE',
    #         follow_redirects=True
    #     )
    #     self.assertNotIn(b'Elie Schoppik', response.data)

    #### TESTS FOR MESSAGES ####

    # def test_messages_index(self):
    #     response = self.client.get('/users/1/messages', content_type='html/text', follow_redirects=True)
    #     self.assertLess(response.status_code, 400)
    #     self.assertIn(b'Hello Elie!!', response.data)
    #     self.assertIn(b'Goodbye Elie!!', response.data)

    # def test_messages_show(self):
    #     response = self.client.get('/users/1/messages/1')
    #     self.assertEqual(response.status_code, 200)

    # def test_messages_create(self):
    #     response = self.client.post(
    #         '/users/1/messages/',
    #         data=dict(text="Hi Matt!!", user_id=3),
    #         follow_redirects=True
    #     )
    #     self.assertEqual(response.status_code, 200)

    # def test_messages_edit(self):
    #     response = self.client.get(
    #         '/users/1/messages/1/edit'
    #     )
    #     self.assertIn(b'Hello Elie!!', response.data)

    #     response = self.client.get(
    #         '/users/2/messages/4/edit'
    #     )
    #     self.assertIn(b'Goodbye Tim!!', response.data)

    # def test_messages_update(self):
    #     response = self.client.patch(
    #         '/users/1/messages/1?_method=PATCH',
    #         data=dict(text="Welcome Back Elie!"),
    #         follow_redirects=True
    #     )
    #     self.assertEqual(response.status_code, 200)

    # def test_messages_delete(self):
    #     response = self.client.delete(
    #         '/users/1/messages/1?_method=DELETE',
    #         follow_redirects=True
    #     )
    #     self.assertNotIn(b'Hello Elie!!', response.data)


if __name__ == '__main__':
    unittest.main()