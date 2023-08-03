from app.models import db, User, Channel, Subscriber

def seed_subscribers():


    # Create subscriber records
    demo_subscriber = Subscriber(user_id=1, channel_id=1)
    justin_subscriber = Subscriber(user_id=2, channel_id=2)
    rajheem_subscriber = Subscriber(user_id=3, channel_id=3)
    chris_subscriber = Subscriber(user_id=4, channel_id=4)
    john_subscriber = Subscriber(user_id=5, channel_id=5)

    # Add subscribers to the session and commit to the database
    db.session.add_all([demo_subscriber, justin_subscriber, rajheem_subscriber, chris_subscriber, john_subscriber])
    db.session.commit()


def undo_subscribers():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.subscribers RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM subscribers"))

    db.session.commit()
