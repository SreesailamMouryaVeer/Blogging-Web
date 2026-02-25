from flask import render_template, request, Blueprint
from flaskblog.models import Post, User

main = Blueprint('main', __name__) 

@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc(), Post.id.desc()).paginate(
        page=page, per_page=5, error_out=False)
    latest_posts = Post.query.order_by(Post.date_posted.desc()).limit(5).all()
    total_users = User.query.count()
    total_posts = Post.query.count()
    return render_template('home.html', posts=posts, latest_posts=latest_posts, 
                         total_users=total_users, total_posts=total_posts)


@main.route('/about')
def about():
    latest_posts = Post.query.order_by(Post.date_posted.desc()).limit(5).all()
    total_users = User.query.count()
    total_posts = Post.query.count()
    return render_template('about.html', title='About', latest_posts=latest_posts,
                         total_users=total_users, total_posts=total_posts)

