import time
import psycopg2
import gloabl_func
import faceDetect
import browser
import manipulate

conn = psycopg2.connect(
   database="instagram_users",
   user='postgres',
   password='2012',
   host='127.0.0.1',
   port= '5432',
   connect_timeout = 1 * 60 #for 1 minute
)

conn.autocommit = True
cursor = conn.cursor()

#return true if local_unique_uid is already exists in user table otherwise return false if not exists
def isExists_local_unique_uid(id=None):
  cursor.execute("SELECT local_unique_uid from users WHERE EXISTS (SELECT local_unique_uid from users WHERE local_unique_uid='{0}' ORDER BY local_unique_uid ASC LIMIT 1)".format(id))
  return True if cursor.fetchone() else False
  
#return true if user already exists with the same username and instagram_id
def isExists_username_and_instagram_id(username=None,instagram_id=None):
  sql = "SELECT username,instagram_id from users WHERE EXISTS (SELECT username,instagram_id from users WHERE username='{0}' AND instagram_id='{1}' ORDER BY local_unique_uid ASC LIMIT 1)".format(username,instagram_id)
  cursor.execute(sql)
  return True if cursor.fetchone() else False
  
#return 1 if successfully inserted new data in user table
def insert_new_data(obj={},table='users'):
   cursor.execute('''INSERT INTO {0} ({1}) VALUES ({2})'''.format(table,','.join(obj.keys()),','.join(['%s' for k in obj ])),[obj[k] for k in obj])
   conn.commit()
   return cursor.rowcount

def insert_multiple_rows(obj=[],tableName='userlist'):
  col = ','.join(list(obj[0].keys())) if gloabl_func.index_in_list(obj,0) else ''
  if col : 
     cursor.executemany("INSERT INTO {0} ({1}) VALUES({2})".format(tableName,col,','.join(list( '%s' for d in obj[0]))),list(list(e.values()) for e in obj))
     return cursor.rowcount
  return 0

def delete_row_from_userlist(username=None,instagram_id=None):
   cursor.execute('''DELETE FROM userlist WHERE username='{0}' instagram_id = '{1}' ORDER BY username ASC LIMIT 1; '''.format(username,instagram_id))
   conn.commit()
   return cursor.rowcount

class Store_data:
    # output status msg of current user
    msg_config_ = {
        "isExcuteNext"  : True,
        "msg" : '',
        "username" : ''
      }
    
        
    # user post input by manipulate posts method
    __user_posts = []

    # user related_profiles input by manipulate related_profiles method
    __related_profiles = [] 

    #user input by manipulate user method
    __INPUTUSER = {}
 
    __userObj =  {} # user data that will insert in users table

    __local_unique_uid = {'local_unique_uid' : ''}

    __posts_where_human_face = []

    __USER_LIST = []

    __Media_to_tagged_user_LIST = []
   
    def __init__(self,username=''):
      self.msg_config_['username'] = username
      # call browser and manipulte
      brow = browser.browser(username)
      if not brow.get("__error__") : 
        self.__INPUTUSER = manipulate.user(brow)
        self.__user_posts = manipulate.posts(brow)
        self.__related_profiles = manipulate.related_profiles(brow)
        # also first check if this user is exists in users table then break all go to next user
        isUser = 0 #isExists_username_and_instagram_id(self.__INPUTUSER['username'],self.__INPUTUSER['instagram_id'])
        if not isUser :
          self.__local_unique_uid = self.__check_users_in_table_userlist_and_get_uid(self.__INPUTUSER['username'],self.__INPUTUSER['instagram_id'],True)
          self.__work_on_user_data(self.__INPUTUSER)
          delete_row_from_userlist(self.__INPUTUSER['username'],self.__INPUTUSER['instagram_id'])
        else :
          self.msg_config_["isExcuteNext"] = False
          self.msg_config_["error"] = "User already exists with this username and instagram_id code 021"
      

    ################################################################################
    #users
    def __work_on_user_data(self,obj={},face_detect=True):
      if not obj : 
        obj = {}

      #get unique user id after verifying from user table
      def get_unique_uid_after_verifying() : 
        def _crId_():
            return gloabl_func.unique_id()
        id = self.__local_unique_uid['local_unique_uid']
        for i in range(10):
          if isExists_local_unique_uid(id):
            id = _crId_()
            if i==9 : 
              self.msg_config_['isExcuteNext'] = False
              self.msg_config_['msg'] = 'local_user_unique_id is not created. id is = {0}'.format(id)
          else : break
        return id if self.msg_config_['isExcuteNext'] else False

      local_user_unique_id = get_unique_uid_after_verifying()
      if local_user_unique_id : 
        self.__local_unique_uid['local_unique_uid'] = local_user_unique_id
        obj['local_unique_uid'] = local_user_unique_id
        obj['datetime'] = gloabl_func.date_time()
        isExistsUser = isExists_username_and_instagram_id(obj["username"],obj["instagram_id"])
        if not isExistsUser: 
            userPicURL = obj['profile_pic_url_hd'] or obj['profile_pic_url']
            if userPicURL : 
              userDirectory = "users/"+(obj['instagram_id'] or "unknown")+ ("_{0}".format(time.time_ns()))+"/instagram"
              userImgDirectory = userDirectory + "/" + "profile"
              createDir = gloabl_func.create_directory(userImgDirectory)
              downlodUimgInDirectory = gloabl_func.downloadImg(userPicURL,"./"+createDir+"/")
              obj['local_profile_pic_url'] = createDir+"/"+downlodUimgInDirectory
              obj['user_directory'] = userDirectory
              self.__userObj = obj

              humanFace = len(self.__posts_where_human_face)
              self.__work_on_user_post()

              if face_detect or not humanFace : 
                 humanFace = faceDetect.faceDetect(obj['local_profile_pic_url'])
              if humanFace or not face_detect: 
                insert = insert_new_data(obj)
                if insert : 
                    insert_multiple_rows(self.__posts_where_human_face,'posts')
                    insert_multiple_rows(self.__USER_LIST,'userlist')
                    insert_multiple_rows(self.__Media_to_tagged_user_LIST,'media_to_tagged_user')     
                    self.msg_config_['isExcuteNext'] = True
                    self.msg_config_['msg'] = "user data successfully inserted"
                    return obj
                else : 
                  self.msg_config_['isExcuteNext'] = False
                  self.msg_config_['msg'] = "user Data not inserted"
                  return obj
              else : 
                self.msg_config_['isExcuteNext'] = False
                self.msg_config_['msg'] = "human face not detect in profile pic"
                return obj
            else : 
              self.msg_config_['isExcuteNext'] = False
              self.msg_config_['msg'] = "Profile pic url not found"
              return obj
        else : 
          self.msg_config_['isExcuteNext'] = False
          self.msg_config_['msg'] = 'User already exists in user table with USERNAME = {0} and instagram_id = {1}'.format(obj["username"],obj['instagram_id'])
          return obj
      else : return obj

    ################################################################################

    #post
        
    def __check_users_in_table_userlist_and_get_uid(self,userName='',instgram_id='',getJson = False,table='userlist'):
      responses = {
        'local_unique_uid' : gloabl_func.unique_id(),
        'isUserExistInDB' : False
      }
      cursor.execute('''SELECT username , instagram_id , local_unique_uid FROM {0} WHERE username='{1}' AND instagram_id='{2}' ORDER BY username ASC LIMIT 1'''.format(table,userName,instgram_id))
      fetch = cursor.fetchall() or []
      conn.commit()
      for f in fetch : 
        if f[0]==userName and f[1]==instgram_id :
          responses['local_unique_uid'] = f[2] or gloabl_func.unique_id()
          responses['isUserExistInDB'] = True
      return responses if getJson else responses['local_unique_uid']
          
    # check_users_in_table_user_userlist_and_get_uid('monikamanchand','7181088')

    def __work_on_user_list(self,arr={}):
        userGetId = {}
        if type(arr) is dict : 
          userGetId = self.__check_users_in_table_userlist_and_get_uid(arr.get("username"),arr.get("instagram_id"),True)
          if not userGetId.get('isUserExistInDB') :
            userGetId = self.__check_users_in_table_userlist_and_get_uid(arr.get("username"),arr.get("instagram_id"),True,'users')
            if not userGetId.get('isUserExistInDB') : 
              self.__USER_LIST.append({
                "username" : arr.get("username"),
                "full_name" : arr.get('full_name'),
                "instagram_id" : arr.get("instagram_id"),
                "profile_pic_url" : arr.get("profile_pic_url"),
                "local_unique_pid" : arr.get("local_unique_pid"),
                "local_unique_uid" : userGetId.get('local_unique_uid') or arr.get("local_unique_uid") or gloabl_func.unique_id(),
                "datetime" : gloabl_func.date_time()
              })
        return userGetId.get('local_unique_uid')


    def _work_on_generate_post_id(self,length=0):
        genid = []
        try : 
            for i in range(length) :
              genid.append("post{0}{1}".format(i,gloabl_func.unique_id())) 
            cursor.execute('''SELECT local_unique_pid FROM posts WHERE local_unique_pid IN ('{0}') ORDER BY local_unique_pid;'''.format("','".join(genid)))
            if cursor.rowcount :
              f = cursor.fetchall()
              genid = [ '{0}{1}'.format(e,gloabl_func.time.time_ns()) if (e,) in f else e for e in genid ]
        except : ''
        return genid

    def __media_to_tagged_user(self,arr={}):
        self.__Media_to_tagged_user_LIST.append({
            "to_username" : arr.get("username"),
            "to_full_name" : arr.get('full_name'),
            "to_instagram_id" : arr.get("instagram_id"),
            "to_profile_pic_url" : arr.get("profile_pic_url"),
            "local_unique_pid" : arr.get("local_unique_pid"),
            "from_local_unique_uid" : self.__userObj.get('local_unique_uid'),
            "from_username" : self.__userObj.get('username'),
            "from_instagram_id" : self.__userObj.get('instagram_id'),
            "datetime" : gloabl_func.date_time()
          })

    def __work_on_user_post(self):
        user_post_dir = gloabl_func.create_directory("./"+self.__userObj['user_directory']+"/post/")
        unique_pids = self._work_on_generate_post_id(len(self.__user_posts)) or []
        
        def downloadAndCheckHumanFace(url):
            isHumanFaceExists = 0
            local_img_path = ''
            try :
              imgN = gloabl_func.downloadImg(url,user_post_dir)
              if imgN:
                local_img_path = user_post_dir+imgN
                isHumanFaceExists = faceDetect.faceDetect(local_img_path)
            except : ''
            return {"isHumanFaceExists" : True if isHumanFaceExists else False , "local_img_path" : local_img_path }
        
        i = 0
        for p in self.__user_posts:
          if type(p) is dict : 
              url = p.get('display_url') or p.get('thumbnail_srcs')
              isHFace = downloadAndCheckHumanFace(url)              
              if isHFace['isHumanFaceExists'] :
                p['local_unique_pid'] = unique_pids[i] if gloabl_func.index_in_list(unique_pids,i) else ''
                p['local_unique_uid'] = self.__userObj.get('local_unique_uid')
                p["datetime"]  = gloabl_func.date_time()
                pe = {}
                for e in p or {}:
                    if e == 'media_to_tagged_user':
                        if type(p.get(e)) is list : 
                            for el in p[e] : 
                              if type (el) is dict : 
                                self.__media_to_tagged_user(el)
                    else :
                        pe[e] = p.get(e)
                i += 1
                self.__posts_where_human_face.append(pe)
                if len(self.__posts_where_human_face) >= 5 : #only 5 post that's contain human face
                   break
              else : 
                gloabl_func.delete_local_file(isHFace['local_img_path'])
        return self.__work_on_related_profiles()
    ################################################################################

    # related_profiles
    def __work_on_related_profiles(self):
        for e in self.__related_profiles or [] :
          if type(e) is dict :
            self.__work_on_user_list(e)
        self.__USER_LIST = list({ e.get('username') : e for e in self.__USER_LIST }.values())
        return True

FIRST_TIME_USER_LIST = [
    ("virat.kohli",),
    ("vijaykumar_ganesh",),
    ("monikamanchanda",),
    ("ashmishra_",),
    ("madhubala_000",),
    ("nishukumari06517",)
  ]

def Main() :
  cursor.execute("SELECT username FROM userlist")
  fetchAll = cursor.fetchall()
  fetchUsersList = fetchAll if bool(fetchAll) else FIRST_TIME_USER_LIST or [()]
  for u in fetchUsersList :
      usr = u[0] if len(u) else ''
      try :
         if usr : 
            Store_data_fun = Store_data(usr)
            print("completed = ",Store_data_fun)

         if browser.isEndButtonPressed:
             print("code has been stoped. Last excute UserName =  {0}".format(usr))
             break  
      except : 
         print("something wrong during fetch users list. code = 3010")


if __name__ == '__main__' : 
    Main()
    # print(cursor)


