const GLOBAL = {
    isConsoleOpen : true,
    copyFunctionName : '__copyToClipboard__',

    DOM : {
        profileImg : 'header.vtbgv div.XjzKX span img._6q-tv',
        userName : 'section.zwlfE div.nZSzR ._7UhW9',
        isVerified : 'section.zwlfE div.nZSzR div.soMvl .mTLOB',
        name : 'section.zwlfE div.-vDIg .rhpdm',
        biography : 'section.zwlfE div.-vDIg span',
        website : 'section.zwlfE div.-vDIg a.yLUwa',
        posts : 'main.SCxLW div.v9tJq div._2z6nI .ySN3v div.Nnq7C'
    },

    JSON : {
        user : [
            'biography' , 'blocked_by_viewer', 'business_address_json' , 'business_category_name' , 'business_contact_method',
            'business_email' , 'business_phone_number' , 'category_enum' , 'category_name' , 'connected_fb_page' , 'country_block',
            'external_url' , 'external_url_linkshimmed' , 'fbid' , 'followed_by_viewer' , 'follows_viewer' , 
            'full_name' , 'has_ar_effects' , 'has_blocked_viewer' , 'has_channel' , 'has_clips' , 'has_guides' , 'has_requested_viewer',
            'hide_like_and_view_counts' , 'id' , 'is_business_account' , 'is_joined_recently' , 'is_private' , 'is_professional_account' , 
            'is_verified' , 'overall_category_name' , 'profile_pic_url' ,'profile_pic_url_hd' , 'username',
            // posts
            'edge_owner_to_timeline_media'
        ],
        additional : [
            'logging_page_id'
        ],

        // posts data = readonly
        edge_owner_to_timeline_media : {
            'users.edge_owner_to_timeline_media.edges' : {
                 0 : {
                     'node' :  [
                      'display_url',
                      'id',
                      'is_video',
                      'taken_at_timestamp',
                      'accessibility_caption',
                      'edge_media_to_tagged_user', //get more
                      'coauthor_producers',
                      'location', //get more
                      'edge_media_to_caption.edges', // get more
                     ],
                    // ...
              }
           }
        }
        
    }

}
module.exports = { GLOBAL }
// entry_data.ProfilePage[0].graphql
// entry_data.ProfilePage[0].logging_page_id
// topsearch = https://www.instagram.com/web/search/topsearch/?query=therock
