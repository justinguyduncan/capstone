from app.models import db, Comment, VOD, User, environment, SCHEMA
import random
import datetime

def seed_comments():
    # Get all VODs from the database
    vods = VOD.query.all()

    # Get all users from the database
    users = User.query.all()

    # List of sample comments
    comments = [
        "Awesome gameplay!",
        "I love this!",
        "Keep it up!",
        "Can't wait for the next stream!",
        "Great quality video!",
        "You're so skilled!",
        "This is my favorite VOD!",
        "You're the best!",
        "Incredible!",
        "I learned a lot from this!",
    ]

    for vod in vods:
        # Determine how many comments to add for each VOD (random number between 0 and 5)
        num_comments = random.randint(0, 5)

        for _ in range(num_comments):
            # Randomly select a user and a comment from the list
            user = random.choice(users)
            comment_text = random.choice(comments)

            # Create a new comment object and add it to the VOD's comments list
            comment = Comment(
                vod_id=vod.id,
                user_id=user.id,
                content=comment_text,
                created_at=datetime.datetime.utcnow()
            )
            db.session.add(comment)

    db.session.commit()


def undo_comments():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.comments RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM comments"))

    db.session.commit()
