from app.models import db, User, Channel, environment, SCHEMA

# Function to seed channels
def seed_channels():
    # Create sample channels
    demo_channel = Channel(
        user_id=1,
        title='Demo Channel',
        description='This is a demo channel for testing purposes.'
    )

    justin_channel = Channel(
        user_id=2,
        title='Justin\'s Gaming Channel',
        description='Welcome to my gaming channel! Watch me play some cool games.'
    )

    rajheem_channel = Channel(
        user_id=3,
        title='Bigred1\'s Channel',
        description='Gaming and more! Join me on my gaming adventures.'
    )

    chris_channel = Channel(
        user_id=4,
        title='DUNC Gaming',
        description='Gaming, reviews, and everything related to gaming!'
    )

    john_channel = Channel(
        user_id=5,
        title='Reaper4G Streams',
        description='Live streams of various games. Join me and let\'s have fun together!'
    )

    # Add the channels to the session and commit the changes
    db.session.add(demo_channel)
    db.session.add(justin_channel)
    db.session.add(rajheem_channel)
    db.session.add(chris_channel)
    db.session.add(john_channel)
    db.session.commit()


def undo_channels():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.channels RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM channels")

    db.session.commit()
