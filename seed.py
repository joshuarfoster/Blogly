
from models import User, db, Post, Tag, PostTag
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

# Add tags
    intro = Tag(name='Intro')
    fun = Tag(name='Fun')
    sad = Tag(name='Sad')
    angry = Tag(name='Angry')
    inspo = Tag(name='Inspo')

# Add new objects to session, so they'll persist
    db.session.add(intro)
    db.session.add(fun)
    db.session.add(sad)
    db.session.add(angry)
    db.session.add(inspo)

# Commit--otherwise, this never gets saved!
    db.session.commit()

# Add posts
    hello1 = Post(title='Hello',content="Hello, I'm Harry and I'll defeat Voldemort for sure",user_id=1)
    hello2 = Post(title='Howdy',content="Howdy partner",user_id=2)
    hello3 = Post(title='My Goal',content="I am here to preserve the Union!!!",user_id=3)
    hello4 = Post(title='Homesick',content='I miss Prim',user_id=4)
    hello5 = Post(title='New Song',content='Check out my new single',user_id=5)
    hello6 = Post(title='Show tonight',content='Putting on a show tonight',user_id=6)
    hello7 = Post(title='Book Signing',content='Come to my book signing at the library',user_id=7)

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

# Add posts_tags
    tag1 = PostTag(post_id=1,tag_id=1)
    tag2 = PostTag(post_id=1,tag_id=5)
    tag3 = PostTag(post_id=2,tag_id=1)
    tag4 = PostTag(post_id=2,tag_id=2)
    tag5 = PostTag(post_id=3,tag_id=5)
    tag6 = PostTag(post_id=3,tag_id=4)
    tag7 = PostTag(post_id=4,tag_id=3)
    tag8 = PostTag(post_id=5,tag_id=2)
    tag9 = PostTag(post_id=6,tag_id=2)
    tag10 = PostTag(post_id=7,tag_id=5)
    tag11 = PostTag(post_id=7,tag_id=2)

# Add new objects to session, so they'll persist
    db.session.add(tag1)
    db.session.add(tag2)
    db.session.add(tag3)
    db.session.add(tag4)
    db.session.add(tag5)
    db.session.add(tag6)
    db.session.add(tag7)
    db.session.add(tag8)
    db.session.add(tag9)
    db.session.add(tag10)
    db.session.add(tag11)

# Commit--otherwise, this never gets saved!
    db.session.commit()
