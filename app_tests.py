from app import app
from unittest import TestCase
from models import db, User

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///sqla_intro_test'
app.config['SQLALCHEMY_ECHO'] = False


app.config['TESTING'] = True


app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class RouteTestCase(TestCase):
    """Tests for views for Pets."""

    def setUp(self):
        """Add sample pet."""

        User.query.delete()

        User = Pet(first_name="Jim", last_name="Bo", image_url='www.ddfsdf.com')
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    def test_list_pets(self):
        with app.test_client() as client:
            resp = client.get("/users")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Users', html)

    def test_show_pet(self):
        with app.test_client() as client:
            resp = client.get(f"/users/{self.user_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Jim Bo</h1>', html)

    def test_add_pet(self):
        with app.test_client() as client:
            d = {"first name": "billy", "last_name": "billy", "image_url": "www.billy.com"}
            resp = client.post("/users/new", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>Users</h1>", html)
