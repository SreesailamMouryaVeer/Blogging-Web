import os
import json
from datetime import datetime

from flaskblog import create_app, db, bcrypt
from flaskblog.models import Post, User

app = create_app()


def load_posts():
    path = os.path.join(os.path.dirname(__file__), 'posts_seed.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


if __name__ == '__main__':
    posts = load_posts()
    with app.app_context():
        user = User.query.get(1)
        if not user:
            pw = bcrypt.generate_password_hash('password').decode('utf-8')
            user = User(username='seeduser', email='seed@example.com', password=pw)
            db.session.add(user)
            db.session.commit()
            print(f'Created seed user id={user.id}')

        added = 0
        for p in posts:
            try:
                dt = datetime.fromisoformat(p.get('date_posted'))
            except Exception:
                dt = datetime.utcnow()
            post = Post(title=p.get('title'), content=p.get('content'), date_posted=dt, user_id=user.id)
            db.session.add(post)
            added += 1
        db.session.commit()
        print(f'Inserted {added} posts for user id={user.id}')
