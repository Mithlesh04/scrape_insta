import psycopg2

# first create database instagram_user

conn = psycopg2.connect(
   database="instagram_users",
   user='postgres',
   password='2012',
   host='127.0.0.1',
   port= '5432'
)

conn.autocommit = True

cursor = conn.cursor()

# cursor.execute("CREATE database instagram_users IF NOT EXISTS")


userTable = '''
    CREATE TABLE IF NOT EXISTS users(
      id serial PRIMARY KEY,
      local_unique_uid VARCHAR(999),
      datetime VARCHAR(255),
      username VARCHAR(999),
      full_name VARCHAR(999),
      instagram_id VARCHAR(999),
      fbid VARCHAR(999),
      biography text,
      profile_pic_url VARCHAR(999),
      profile_pic_url_hd VARCHAR(999),
      local_profile_pic_url VARCHAR(999),
      external_url VARCHAR(999),
      external_url_linkshimmed VARCHAR(999),
      is_private boolean,
      is_verified boolean,
      category_name VARCHAR(999),
      is_joined_recently boolean,
      is_professional_account boolean,
      connected_fb_page VARCHAR(999),
      overall_category_name VARCHAR(999),
      blocked_by_viewer boolean,
      is_business_account boolean,
      business_address_json text,
      business_category_name VARCHAR(999),
      business_contact_method VARCHAR(999),
      business_email VARCHAR(999),
      business_phone_number VARCHAR(999),
      category_enum VARCHAR(999),
      country_block boolean,
      user_directory text,
      logging_page_id VARCHAR(999),
      user_server_profile_url text
    );
    comment on column users.datetime is 'Date time when data store in database';
    comment on column users.local_unique_uid is 'unique user id create by local machine';
    comment on column users.user_directory is 'user directory in local machine';
    comment on column users.user_server_profile_url is 'user original server url where user data comes from';
  '''


userPosts = '''
    CREATE TABLE IF NOT EXISTS posts(
      id serial PRIMARY KEY,
      local_unique_pid VARCHAR(999),
      local_unique_uid VARCHAR(999),
      datetime VARCHAR(255),
      display_url VARCHAR(999),
      media_to_caption text,
      location_id VARCHAR(999),
      location_name VARCHAR(999),
      location_slug VARCHAR(999),
      taken_at_timestamp VARCHAR(999),
      is_video boolean,
      has_audio boolean,
      video_url VARCHAR(999),
      post_id VARCHAR(999),
      thumbnail_src VARCHAR(999),
      accessibility_caption text
    );
    comment on column posts.local_unique_pid is 'unique post id create by local machine';
    comment on column posts.local_unique_uid is 'unique user id store in user table';
    comment on column posts.display_url is 'posted image or if video then thumbnail_src';
    comment on column posts.media_to_caption is 'posted description with posted image';
    comment on column posts.accessibility_caption is 'few more text with posted image for info more review instagram';
    comment on column posts.datetime IS 'Date time when data store in database';

  '''


userList = '''
    CREATE TABLE IF NOT EXISTS userlist(
      id serial PRIMARY KEY,
      local_unique_uid VARCHAR(999),
      local_unique_pid VARCHAR(999),
      username VARCHAR(999),
      full_name VARCHAR(999),
      instagram_id VARCHAR(999),
      profile_pic_url VARCHAR(999),
      datetime VARCHAR(255)
    );
    comment on COLUMN userlist.local_unique_pid IS 'User mention or taged with the post.';
    comment on TABLE userlist IS 'list of temp users. In this users list like related_profiles, shared post with user. When each users data collected then that user will deleted from this table and insert into users table.';
    comment on COLUMN userlist.datetime IS 'Date time when data store in database';
  '''


media_to_tagged_user = '''
    CREATE TABLE IF NOT EXISTS media_to_tagged_user(
      id serial PRIMARY KEY,
      to_username VARCHAR(999),
      to_full_name VARCHAR(999),
      to_instagram_id VARCHAR(999),
      to_profile_pic_url VARCHAR(999),
      local_unique_pid VARCHAR(999),
      from_local_unique_uid VARCHAR(999),
      from_username VARCHAR(999),
      from_instagram_id VARCHAR(999),
      datetime VARCHAR(255)
    );
    comment on COLUMN media_to_tagged_user.to_username IS 'post that tag to specific user or users';
    comment on COLUMN media_to_tagged_user.from_username IS 'post that tag from specific user or users';
    comment on COLUMN media_to_tagged_user.local_unique_pid IS 'post unique id generated by local machine';
    comment on TABLE media_to_tagged_user IS 'posts tag to users';
    comment on COLUMN media_to_tagged_user.datetime IS 'Date time when data store in database';
 '''



cursor.execute(userTable)
cursor.execute(userPosts)
cursor.execute(userList)
cursor.execute(media_to_tagged_user)

conn.commit()