
import datetime

def blog():

    DATA = {}
    DATA['title'] = 'AMOSOO'
    DATA['subtitle'] = 'blog SUB Title : 서브타이틀'
    DATA['blog_title'] = '아모이스'
    DATA['blog_subtitle'] = '블로그'
    DATA['blog_title_img'] = 'COLORADMIN_FRONT/img/cover/cover-2.jpg'

    DATA['companay'] = 'AMOSOO INC.'
    DATA['address'] = '경기도 의정부시 의정부1동 11-11'
    DATA['mail'] = 'contact@amoisoo.com'
    DATA['phone'] = '010-1111-1111'
    DATA['phone2'] = '+82 (10) 2222-2222'

    return DATA


def forum():

    DATA = {}
    DATA['title'] = '포럼'

    gallery = []
    gallery.append( 'COLORADMIN_ADMIN/img/user/user-1.jpg' )
    gallery.append( 'COLORADMIN_ADMIN/img/user/user-2.jpg' )
    gallery.append( 'COLORADMIN_ADMIN/img/user/user-3.jpg' )
    gallery.append( 'COLORADMIN_ADMIN/img/user/user-4.jpg' )
    gallery.append( 'COLORADMIN_ADMIN/img/user/user-5.jpg' )
    gallery.append( 'COLORADMIN_ADMIN/img/user/user-6.jpg' )
    gallery.append( 'COLORADMIN_ADMIN/img/user/user-7.jpg' )
    gallery.append( 'COLORADMIN_ADMIN/img/user/user-8.jpg' )
    gallery.append( 'COLORADMIN_ADMIN/img/user/user-9.jpg' )
    gallery.append( 'COLORADMIN_ADMIN/img/user/user-10.jpg' )


    DATA['gallery'] = gallery

    return DATA


def settings():

    DATA = {}
    DATA['title'] = 'Settings Info'
    DATA['layout'] = 'holizontal'


    return DATA


def layout():

    DATA = {}

    DATA['BOX'] = True # True , False
    DATA['NAVI_POSITION'] = 'TOP'   # TOP, LEFT
    DATA['NAVI_SIDE_CLOSE'] = True   # True , False


    DATA['THEME_USE'] = False
    DATA['KOOKIE_USE'] = False

    return DATA





def global_info( request ):
    DATA = {}

    APP = {}
    APP[ 'address' ] = 'AAA'
    APP['mail'] = 'contact@amoisoo.com'
    APP['name'] = 'lee'
    APP['right'] = '© 2020 아모이스 All Right Reserved'
    APP['company_name'] = '아모이스'

    APP['time'] = datetime.datetime.now()

    APP['domain'] =  '../'#'http://amosoo.com'

    APP['maindomain'] =  'http://localhost'
    APP['maindomain'] =  'http://amoisoo.net'

    #------------------------------------------

    APP['BLOG'] = blog()
    APP['FORUM'] = forum()

    #------------------------------------------
    DATA['APP'] = APP
    DATA['SETTINGS'] = settings()
    DATA['LAYOUT'] = layout()


    #DATA['ARBRE_URL'] = '/arbre/'

    return DATA










#
def info_support( request ):
    object_list = {}

    APP = {}
    APP[ 'address' ] = 'AAA'
    APP['mail'] = 'lee@amoisoo.com'
    APP['name'] = 'lee'
    APP['title'] = 'support'
    APP['note'] = '서포트 페이지를 표시합니다.'


    object_list['SUPPORT'] = APP

    return object_list













