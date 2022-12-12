"""Dsj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from app1 import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    ###########小程序##########
    path('admin/', admin.site.urls),
    url(r'^CollectQuest/$', views.ZyyCollectQuestGeneicView.as_view()),
    url(r'^CollectQuest/(?P<pk>\d+)/$', views.ZyyCollectQuestGeneicView2.as_view()),
    url(r'^DsjPic/$', views.ZyyDsjPicQuestGeneicView.as_view()),
    url(r'^DsjPic/(?P<pk>\d+)/$', views.ZyyDsjPicQuestGeneicView2.as_view()),
    path('inedx/login2/', views.UserLogin2),
    url(r'^user/$', views.ZyyUserGeneicView.as_view()),
    url(r'^user/(?P<pk>\d+)/$', views.ZyyUserGeneicView2.as_view()),
    url(r'^leibiao/$', views.LeiBiaoGeneicView.as_view()),
    url(r'^leibiao/(?P<pk>\d+)/$', views.LeiBiaoGeneicView2.as_view()),

    url(r'^leixing/$', views.LeiXingGeneicView.as_view()),
    url(r'^leixing/(?P<pk>\d+)/$', views.LeiXingGeneicView2.as_view()),

    url(r'^zerenren/$', views.ZerenrenGeneicView.as_view()),
    url(r'^zerenren/(?P<pk>\d+)/$', views.ZerenrenGeneicView2.as_view()),
    url(r'^zj/$', views.ZjGeneicView.as_view()),
    url(r'^jxiao/$', views.JxiaoGeneicView.as_view()),
    url(r'^export/csv/$', views.export_users_csv, name='export_users_csv'),

    path('index/addPro/', views.addPro),
    #path('index/uploadPic/', views.uploadPic),
    path('index/test/', views.test),
    path('user/updateUser/', views.updateUser),
    path('jxiao/detail/', views.jxdetail),
    #path('dbx/', views.dbxdetail)
    path('plza/', views.plza),
    path('plza/detail/', views.plzadetail),#旁路系统工单
    path('plza/getclr/', views.plzagetclr),#旁路系统查询处理人
    path('plza/xgdx/', views.plzaxgdx),#旁路定性工单修改
    path('user/getusertype/', views.getusertype),  # 登录时获取用户类型。
    # path('sendmail/', views.sendmail),
    path('fqx/detail/', views.fqxdetail),



    ###########web网页##########
    path('web/userlogin/', views.MainLogin),
    path('web/exitlogin', views.exitlogin),
    path('web/index/', views.index),
    path('web/list/ztd', views.listzdt),
    path('web/list/ztd_hd', views.ztd_hd),
    path('web/list/yhd', views.listyhd),
    path('web/list/yhd_hf', views.yhd_hf),
    path('web/list/zjcs', views.zjcs),
    path('web/list/zjcsdetail', views.zjcsdetail),
    path('web/list/gdbx', views.webgdbx),
    path('web/upload/',views.upload),
    path('web/upload1',views.excel_upload),
    path('download_template/',views.download_template),

    ###########食堂#############
    path('st/styy', views.styy),
    path('st/getid', views.stgetId),
    path('st/styy/detail', views.styydetail),
    path('st/styy/delete', views.styydelete),
    path('st/styy/cp/detail', views.cpdetail),
    path('st/styy/cp/delete', views.delete),
    path('st/styy/cp/add', views.spadd)


]

