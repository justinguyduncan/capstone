from app.models import db, User, Channel, Subscriber

def seed_subscribers():
    # Get user IDs from seed_users
    demo_user_id, justin_user_id, rajheem_user_id, chris_user_id, john_user_id = seed_users()

    # Get channel IDs from seed_channels
    demo_channel = Channel.query.filter_by(title='Demo Channel').first()
    justin_channel = Channel.query.filter_by(title='Justin\'s Gaming Channel').first()
    rajheem_channel = Channel.query.filter_by(title='Bigred1\'s Channel').first()
    chris_channel = Channel.query.filter_by(title='DUNC Gaming').first()
    john_channel = Channel.query.filter_by(title='Reaper4G Streams').first()

    # Create sample subscriptions
    demo_subscriber = Subscriber(user_id=demo_user_id, channel_id=justin_channel.id)
    justin_subscriber = Subscriber(user_id=justin_user_id, channel_id=rajheem_channel.id)
    rajheem_subscriber = Subscriber(user_id=rajheem_user_id, channel_id=chris_channel.id)
    chris_subscriber = Subscriber(user_id=chris_user_id, channel_id=john_channel.id)
    john_subscriber = Subscriber(user_id=john_user_id, channel_id=demo_channel.id)

    # Add subscribers to the session
    db.session.add(demo_subscriber)
    db.session.add(justin_subscriber)
    db.session.add(rajheem_subscriber)
    db.session.add(chris_subscriber)
    db.session.add(john_subscriber)
    db.session.commit()
