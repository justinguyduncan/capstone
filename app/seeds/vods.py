from app.models import db, Channel, VOD, environment, SCHEMA
from ..aws import upload_file_to_s3, remove_file_from_s3


# Function to seed VODs
def seed_vods():
    # Get channel IDs from seed_channels
    demo_channel = Channel.query.filter_by(title='Demo Channel').first()
    justin_channel = Channel.query.filter_by(title="Justin's Gaming Channel").first()
    rajheem_channel = Channel.query.filter_by(title="Bigred1's Channel").first()
    chris_channel = Channel.query.filter_by(title="DUNC Gaming").first()
    john_channel = Channel.query.filter_by(title="Reaper4G Streams").first()

    # Create sample VODs and upload them to S3
    demo_vod1 = VOD(
        channel_id=demo_channel.id,
        title='Shadow of the Tomb Raider',
        description='1st run through of the new Tomb Raider',
        video_url='s3://gamersquare/Shadow of the Tomb Raider HD Gameplay - Free To Use Gameplay (60 FPS).mp4'
    )

    demo_vod2 = VOD(
        channel_id=demo_channel.id,
        title='Forza Horizon 4',
        description='Drifting around a Supra',
        video_url='s3://gamersquare/Free To Use Gameplay _ Forza Horizon 4 _ RTX ON Ultra Graphics _ no copyright gameplay.mp4'
    )

    justin_vod1 = VOD(
        channel_id=justin_channel.id,
        title="CSGO Getting Ready For Comp",
        description='Lets start the rank up grind!',
        video_url='s3://gamersquare/Free To Use Gameplay _ CS_GO _ 4K _ No Copyright Gameplay _ Nuke.mp4'
    )

    justin_vod2 = VOD(
        channel_id=justin_channel.id,
        title="Valorant Warmup",
        description='Warming Up with a little Swiftplay',
        video_url='s3://gamersquare/Valorant Deadlock Gameplay - Free To Use  #PCGamePass.mp4'
    )

    rajheem_vod1 = VOD(
        channel_id=rajheem_channel.id,
        title="GTA V Playthrough",
        description='GTA V Playthrough',
        video_url='s3://gamersquare/Free To Use Gameplay _ GTA 5 _ RTX ON Ultra Graphics _ no copyright gameplay.mp4'
    )

    rajheem_vod2 = VOD(
        channel_id=rajheem_channel.id,
        title="Spider-Man Remastered",
        description='This new spiderman remaster is amazing. Come watch me playthrough',
        video_url='s3://gamersquare/Free To Use Gameplay _ Marvels Spider-Man Remastered _ RTX ON Ultra Graphics _ no copyright gameplay.mp4'
    )

    chris_vod1 = VOD(
        channel_id=chris_channel.id,
        title="Minecraft: Survival Series Part 1",
        description='Lets Get a new World Started',
        video_url='s3://gamersquare/Free To Use Gameplay _ Minecraft _ 4K _ No Copyright Gameplay + map.mp4'
    )

    chris_vod2 = VOD(
        channel_id=chris_channel.id,
        title="Minecraft: Survival Series Part 2",
        description='Lets Get a new World Started',
        video_url='s3://gamersquare/Free To Use Gameplay _ Minecraft _ 4K _ No Copyright Gameplay + map (1).mp4'
    )

    john_vod1 = VOD(
        channel_id=john_channel.id,
        title="Valorant Noob",
        description='First Time Playing Val. Check it out',
        video_url='s3://gamersquare/Valorant Gameplay - Free To Use.mp4'
    )

    # Add VODs to the session
    db.session.add(demo_vod1)
    db.session.add(demo_vod2)
    db.session.add(justin_vod1)
    db.session.add(justin_vod2)
    db.session.add(rajheem_vod1)
    db.session.add(rajheem_vod2)
    db.session.add(chris_vod1)
    db.session.add(chris_vod2)
    db.session.add(john_vod1)
    db.session.commit()

if __name__ == "__main__":
    seed_vods()


def undo_vods():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.vods RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM vods")

    db.session.commit()
