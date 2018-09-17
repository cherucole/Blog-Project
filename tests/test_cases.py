import unittest
from app.models import User,Post, Comment, Role
from app import db



class UserTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'mypassword')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('mypassword'))



class PostTest(unittest.TestCase):
    def setUp(self):
        self.new_post = Post(id=1,
                             title="title",
                             subtitle='subtitle',
                             content="content")

    def tearDown(self):
        Post.query.delete()

    def test_init(self):
        self.assertEquals(self.new_post.id, 1)
        self.assertEquals(self.new_post.title, "title")
        self.assertEquals(self.new_post.subtitle, "subtitle")
        self.assertEquals(self.new_post.content, "content")


class CommentTest(unittest.TestCase):
    def setUp(self):
        self.new_comment = Comment(1,"comment",1,1)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))

    def test_init(self):
        self.assertEqual(self.new_comment.id, 1)
        self.assertEqual(self.new_comment.comment, "comment")
        self.assertEqual(self.new_comment.user_id, 1)
        self.assertEqual(self.new_comment.post_id, 1)

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all()) > 0)


    def test_get_comment_by_post_id(self):
        self.new_comment.save_comment()
        get_comments = Comment.get_comments(12345)
        self.assertTrue(len(get_comments) == 1)






