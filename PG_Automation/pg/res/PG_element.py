# coding:utf-8
import os

pkg = os.getenv('PGPKG')
# Package 相關
Package = {}
Package['appPackage'] = pkg
Package['appActivity'] = pkg + '.MainPage'

# 第一次開啟的登入頁
LoginPage = {}
LoginPage['skip'] = pkg + ':id/login_skip_btn'
LoginPage['topImage'] = pkg + ':id/top_images'
LoginPage['more'] = pkg + ':id/more_login_option_btn'
LoginPage['FB'] = pkg + ':id/explore_login_btn_fb'
LoginPage['IG'] = pkg + ':id/explore_login_btn_ig'
LoginPage['G'] = pkg + ':id/explore_login_btn_g'
LoginPage['Mail'] = pkg + ':id/sign_up_email'

# 第二次開啟的蒙層
AllTool = {}
AllTool['wording'] = pkg + ':id/create_guide_text'  # 蒙層文案
AllTool['arrow_down'] = pkg + ':id/create_dialog_arrow_down'  # 下拉箭頭
AllTool['tool'] = pkg + ':id/create_guide_btn'  # +號
AllTool['tools_content'] = pkg + ':id/fast_tools_content'  # 最外層
AllTool['close'] = pkg + ':id/btn_fast_tools'  # X
AllTool['twinkle'] = pkg + ':id/twinkle_layout'
AllTool['multi'] = pkg + ':id/multi_layout'
AllTool['camera'] = pkg + ':id/camera_item'  # 最近照片的相機

# 五大頁面
FivePage = {}
FivePage['home'] = pkg + ':id/home_tab'
FivePage['feature'] = pkg + ':id/feed_tab'
FivePage['tools'] = pkg + ':id/btn_fast_tools'
FivePage['noti'] = pkg + ':id/notify_tab'
FivePage['profile'] = pkg + ':id/profile_tab'

# profile
ProfilePage = {}
ProfilePage['FB'] = pkg + ':id/explore_login_btn_fb'
ProfilePage['IG'] = pkg + ':id/explore_login_btn_ig'
ProfilePage['G'] = pkg + ':id/explore_login_btn_g'
ProfilePage['Mail'] = pkg + ':id/sign_up_email'

# profile after login
ProfilePageAfterLogin = {}
ProfilePageAfterLogin['nickName'] = pkg + ':id/profile_name'
ProfilePageAfterLogin['myPhoto'] = pkg + ':id/my_photo'
ProfilePageAfterLogin['postNum'] = pkg + ':id/post_num'
ProfilePageAfterLogin['followingNum'] = pkg + ':id/following_num'
ProfilePageAfterLogin['followerNum'] = pkg + ':id/follower_num'
ProfilePageAfterLogin['setting'] = pkg + ':id/profile_setting'
ProfilePageAfterLogin['userName'] = pkg + ':id/name'


# Email Login Page
emailLoginPage = {}
emailLoginPage['account'] = pkg + ':id/email_edit_text'
emailLoginPage['pwd'] = pkg + ':id/password_edit_text'
emailLoginPage['submit'] = pkg + ':id/login_btn'

# Home page
HomePage = {}
HomePage['Search'] = pkg + ':id/pg_search_icon_font_view'
HomePage['Comment'] = pkg + ':id/feed_comment_image'
HomePage['Like'] = pkg + ':id/feed_like_click_range'
HomePage['Follow'] = pkg + ':id/feed_follow_btn'
HomePage['CommentNumber'] = pkg + ':id/feed_comment_num'

# Search page
SearchPage = {}
SearchPage['Hashtag'] = pkg + ':id/tab_hashtags'

# Picture detail page
PicPage = {}
PicPage['back'] = pkg + ':id/backBtn'

# Xpath practice
FivePageXpath = {}
FivePageXpath['profile'] = '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[4]/android.widget.TextView[1]'
