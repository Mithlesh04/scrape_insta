
# update pip version
  python -m pip install --user --upgrade pip


def delete_row_from_userlist(username=None,instagram_id=None):
   cursor.execute('''DELETE FROM userlist WHERE username='{0}' instagram_id = '{1}' ORDER BY username ASC LIMIT 1; '''.format(username,instagram_id))
   conn.commit()
   return cursor.rowcount


 def __init__(self,username=''):
      self.msg_config_['username'] = username
      # call browser and manipulte
      brow = browser.browser(username)
      if brow : 
        # self.__INPUTUSER = manipulate.user(brow)
        # self.__user_posts = manipulate.posts(brow)
        # self.__related_profiles = manipulate.related_profiles(brow)
        # also first check if this user is exists in users table then break all go to next user
        isUser = 1 # isExists_username_and_instagram_id(self.__INPUTUSER['username'],self.__INPUTUSER['instagram_id'])
        if not isUser :
          ''
          # self.__local_unique_uid = self.__check_users_in_table_userlist_and_get_uid(self.__INPUTUSER['username'],self.__INPUTUSER['instagram_id'],True)
          # self.__work_on_user_data(self.__INPUTUSER)
          # delete_row_from_userlist(self.__INPUTUSER['username'],self.__INPUTUSER['instagram_id'])
        else :
          self.msg_config_["isExcuteNext"] = False
          self.msg_config_["error"] = "User already exists with this username and instagram_id code 021"
      

# user
  
 obj = {
        #local_unique_uid
        'username' : "monikamanchanda",
        "full_name" : "Monika",
        'instagram_id' : "7181088",
        "fbid" : "17841400392640112",
        "biography" : '''#foodwriter #foodconsultant #avidreader #traveller #culinarytrainer
        Chief Culinary Officer at @livealtlife 
        Twitter : @monikamanchanda''',
        'profile_pic_url' : "https://instagram.fdel18-1.fna.fbcdn.net/v/t51.2885-19/s150x150/201183122_1196226470814700_77492436918662027_n.jpg?_nc_ht=instagram.fdel18-1.fna.fbcdn.net&_nc_ohc=Iq5wmwH2H48AX8G8v2E&edm=ABfd0MgBAAAA&ccb=7-4&oh=dafb7ce955e1f383c2894978a23a0b4f&oe=6115C2C4&_nc_sid=7bff83",
        'profile_pic_url_hd' : "https://instagram.fdel18-1.fna.fbcdn.net/v/t51.2885-19/s320x320/201183122_1196226470814700_77492436918662027_n.jpg?_nc_ht=instagram.fdel18-1.fna.fbcdn.net&_nc_ohc=Iq5wmwH2H48AX8G8v2E&edm=ABfd0MgBAAAA&ccb=7-4&oh=3243c16bd24383e50fab563f82865ff3&oe=6114E0B4&_nc_sid=7bff83",
        #local_profile_pic_url
        "external_url" : 'external_url',
        "external_url_linkshimmed" : 'external_url_linkshimmed',
        'is_private' : False,
        'is_verified' : True,
        "category_name" : 'category_name',
        'is_joined_recently' : True,
        'is_professional_account' : True,
        "connected_fb_page" : 'connected_fb_page',
        'overall_category_name' : 'overall_category_name',
        "blocked_by_viewer" : False,
        'is_business_account' : False,
        "business_address_json" : 'business_address_json',
        "business_category_name" : 'business_category_name',
        "business_contact_method" : 'business_contact_method',
        "business_email" : 'business_email',
        "business_phone_number" : 'business_phone_number',
        "category_enum" : 'category_enum',
        "country_block" : False,
     
        'local_unique_uid' : 'local_unique_uid',
        'local_profile_pic_url' : 'local_profile_pic_url',
        'datetime'    : 'datetime',
        'logging_page_id' : 'logging_page_id',
        'user_server_profile_url' : 'https://www.instagram.com/monikamanchanda/?hl=en'
  }







__userObj = # {
    #         #local_unique_uid
    #         'username' : "monikamanchanda",
    #         "full_name" : "Monika",
    #         'instagram_id' : "7181088",
    #         "fbid" : "17841400392640112",
    #         "biography" : '''#foodwriter #foodconsultant #avidreader #traveller #culinarytrainer
    #         Chief Culinary Officer at @livealtlife 
    #         Twitter : @monikamanchanda''',
    #         'profile_pic_url' : "https://instagram.fdel18-1.fna.fbcdn.net/v/t51.2885-19/s150x150/201183122_1196226470814700_77492436918662027_n.jpg?_nc_ht=instagram.fdel18-1.fna.fbcdn.net&_nc_ohc=Iq5wmwH2H48AX8G8v2E&edm=ABfd0MgBAAAA&ccb=7-4&oh=dafb7ce955e1f383c2894978a23a0b4f&oe=6115C2C4&_nc_sid=7bff83",
    #         'profile_pic_url_hd' : "https://instagram.fdel18-1.fna.fbcdn.net/v/t51.2885-19/s320x320/201183122_1196226470814700_77492436918662027_n.jpg?_nc_ht=instagram.fdel18-1.fna.fbcdn.net&_nc_ohc=Iq5wmwH2H48AX8G8v2E&edm=ABfd0MgBAAAA&ccb=7-4&oh=3243c16bd24383e50fab563f82865ff3&oe=6114E0B4&_nc_sid=7bff83",
    #         #local_profile_pic_url
    #         "external_url" : 'external_url',
    #         "external_url_linkshimmed" : 'external_url_linkshimmed',
    #         'is_private' : False,
    #         'is_verified' : True,
    #         "category_name" : 'category_name',
    #         'is_joined_recently' : True,
    #         'is_professional_account' : True,
    #         "connected_fb_page" : 'connected_fb_page',
    #         'overall_category_name' : 'overall_category_name',
    #         "blocked_by_viewer" : False,
    #         'is_business_account' : False,
    #         "business_address_json" : 'business_address_json',
    #         "business_category_name" : 'business_category_name',
    #         "business_contact_method" : 'business_contact_method',
    #         "business_email" : 'business_email',
    #         "business_phone_number" : 'business_phone_number',
    #         "category_enum" : 'category_enum',
    #         "country_block" : False,
        
    #         'local_unique_uid' : '',#ddb9102473ec43c6ac72be2a32d553de1628376816318104400
    #         'local_profile_pic_url' : 'local_profile_pic_url',
    #         'datetime'    : 'datetime',
    #         'logging_page_id' : 'logging_page_id',
    #         "user_directory" :  'users/7181088_monikamanchanda',
    #         'user_server_profile_url' : 'https://www.instagram.com/monikamanchanda/?hl=en'
    #   }




# Api to get user details

   # twitter api
    https://www.speakrj.com/audit/api?api_key=0&username=klrahul11&source=twitter

   # stackexchange
    https://dba.stackexchange.com/users/



    # Aya nagar users list
    [
      'kavyachaudhary7576',
      'sanidul__78',
      'vijaykumar_ganesh',
      'rohit_302_k_',
      'sll4087582021',
      'akash_kashyap57299',
      'jatavmohit789'
      'rinkuchaudhary3016',
      ''

    ]