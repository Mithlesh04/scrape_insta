
# from browser import browser

def user(obj={}):
    user = (obj or {}).get('graphql',{}).get('user',{})
    return {
        #local_unique_uid
        'username' : user.get('username'),
        "full_name" : user.get('full_name'),
        'instagram_id' : user.get('id'),
        "fbid" : user.get('fbid'),
        "biography" : user.get('biography'),
        'profile_pic_url' : user.get('profile_pic_url'),
        'profile_pic_url_hd' : user.get('profile_pic_url_hd'),
        #local_profile_pic_url
        "external_url" : user.get('external_url'),
        "external_url_linkshimmed" : user.get('external_url_linkshimmed'),
        'is_private' : user.get('is_private'),
        'is_verified' : user.get('is_verified'),
        "category_name" : user.get('category_name'),
        'is_joined_recently' : user.get('is_joined_recently'),
        'is_professional_account' : user.get('is_professional_account'),
        "connected_fb_page" : user.get('connected_fb_page'),
        'overall_category_name' : user.get('overall_category_name'),
        "blocked_by_viewer" : user.get('blocked_by_viewer'),
        'is_business_account' : user.get('is_business_account'),
        "business_address_json" : user.get('business_address_json'),
        "business_category_name" : user.get('business_category_name'),
        "business_contact_method" : user.get('business_contact_method'),
        "business_email" : user.get('business_email'),
        "business_phone_number" : user.get('business_phone_number'),
        "category_enum" : user.get('category_enum'),
        "country_block" : user.get('country_block'),
        "logging_page_id" : (obj or {}).get('logging_page_id'),
        'user_server_profile_url' : 'https://www.instagram.com/{0}/?hl=en'.format(user.get('username'))
    }

def posts(obj={}):
    pst = (obj or {}).get('graphql',{}).get('user',{}).get('edge_owner_to_timeline_media',{}).get('edges',[])
    postss = []
    for i in pst:
        p = i.get('node',{}) or {}
        lo = (p.get('location',{}) or {})
        tu = []
        for tt in p.get('media_to_tagged_user',{}).get('edges',[]) or []:
            t = tt.get('node',{}).get('user',{}) or {}
            tu.append({
                "full_name" : t.get('full_name'),
                "instagram_id" : t.get('id'),
                "is_verified" : t.get('is_verified'),
                "profile_pic_url" : t.get('profile_pic_url'),
                "username" : t.get('username')
            })
        postss.append({
            "display_url" : p.get('display_url'),
            "media_to_caption" : (p.get('edge_media_to_caption') or {}).get('edges',[])[0].get('node',{}).get('text'),
            "location_id" : lo.get('id'),
            "location_name" : lo.get('name'),
            "location_slug" : lo.get('slug'),
            "taken_at_timestamp" : p.get('taken_at_timestamp'),
            "is_video" : p.get('is_video',False),
            "has_audio" : p.get('has_audio',False),
            "video_url" : p.get('video_url'),
            "post_id" : p.get('id'),
            "thumbnail_src" : p.get('thumbnail_src'), # when is_video is true then use this insted of display_url
            "accessibility_caption" : p.get('accessibility_caption'),
            "media_to_tagged_user" : tu
        })
    return postss

def related_profiles(obj={}):
    rp = (obj or {}).get('graphql',{}).get('user',{}).get('edge_related_profiles',{}).get('edges',[])
    rpu = []
    for i in rp :
        n = i.get('node',{})
        rpu.append({
            'full_name' : n.get('full_name'),
            'instagram_id'        : n.get('id'),
            'is_private': n.get('is_private'),
            'is_verified':n.get('is_verified'),
            'profile_pic_url':n.get('profile_pic_url'),
            'username' : n.get('username')
        })
    return rpu

# u = posts(browser())
# print(u)