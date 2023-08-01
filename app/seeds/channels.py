from app.models import db, User, Channel

# Function to seed channels
def seed_channels():
    # Get user objects for the channel owners
    demo_user = User.query.filter_by(username='Demo').first()
    justin_user = User.query.filter_by(username='TruePr0tege').first()
    rajheem_user = User.query.filter_by(username='DV Bigred1').first()
    chris_user = User.query.filter_by(username='DUNC').first()
    john_user = User.query.filter_by(username='Reaper4G').first()

    # Create sample channels
    demo_channel = Channel(
        user=demo_user,
        title='Demo Channel',
        description='This is a demo channel for testing purposes.'
    )

    justin_channel = Channel(
        user=justin_user,
        title='Justin\'s Gaming Channel',
        description='Welcome to my gaming channel! Watch me play some cool games.'
    )

    rajheem_channel = Channel(
        user=rajheem_user,
        title='Bigred1\'s Channel',
        description='Gaming and more! Join me on my gaming adventures.'
    )

    chris_channel = Channel(
        user=chris_user,
        title='DUNC Gaming',
        description='Gaming, reviews, and everything related to gaming!'
    )

    john_channel = Channel(
        user=john_user,
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
