
from models import User, db, Post
from app import app


with app.app_context():

# Create all tables


    db.drop_all()
    db.create_all()

# If table isn't empty, empty it
    # User.query.delete()

# Add users
    Harry = User(first_name='Harry', last_name='Potter', image_url='https://tse2.mm.bing.net/th?id=OIP.T9QOfpzhvjIzDQEAf5WE-wHaEK&pid=Api&P=0')
    Chuck = User(first_name='Chuck', last_name='Norris', image_url='https://www.adomonline.com/wp-content/uploads/2020/09/Chuck-Norris.jpg')
    Abe = User(first_name='Abraham', last_name='Lincoln', image_url='https://cdn.antiquestradegazette.com/media/8588/2256bp_shutterstock_242290726.jpg')
    Katniss = User(first_name='Katniss', last_name='Everdeen', image_url='https://i.pinimg.com/736x/07/e8/54/07e8545aa19ae769b5948c10a73a4249--katniss-everdeen-actress-katniss-braid.jpg')
    Dua = User(first_name='Dua', last_name='Lipa', image_url='https://www.hawtcelebs.com/wp-content/uploads/2018/12/dua-lipa-kiis-fm-jingle-ball-at-the-forum-11-30-2018-3.jpg')
    Michael = User(first_name='Michael', last_name='Che', image_url='https://tse3.mm.bing.net/th?id=OIP.zh4TWQlZOtVZam-1OsEkyAHaKW&pid=Api&P=0')
    Michelle = User(first_name='Michelle', last_name='Obama', image_url='https://tse3.mm.bing.net/th?id=OIP.t08Ct5wXExsaIOt3_a7NQQHaHa&pid=Api&P=0')

# Add new objects to session, so they'll persist
    db.session.add(Harry)
    db.session.add(Chuck)
    db.session.add(Abe)
    db.session.add(Katniss)
    db.session.add(Dua)
    db.session.add(Michael)
    db.session.add(Michelle)

# Commit--otherwise, this never gets saved!
    db.session.commit()

# Add posts
    hello1 = Post(title='Hello',content='Hello',user_id=1)
    hello2 = Post(title='Hello',content='Hello',user_id=2)
    hello3 = Post(title='Hello',content='Hello',user_id=3)
    hello4 = Post(title='Hello',content='Hello',user_id=4)
    hello5 = Post(title='Hello',content='Hello',user_id=5)
    hello6 = Post(title='Hello',content='Hello',user_id=6)
    hello7 = Post(title='Hello',content='Hello',user_id=7)

# Add new objects to session, so they'll persist
    db.session.add(hello1)
    db.session.add(hello2)
    db.session.add(hello3)
    db.session.add(hello4)
    db.session.add(hello5)
    db.session.add(hello6)
    db.session.add(hello7)

# Commit--otherwise, this never gets saved!
    db.session.commit()
