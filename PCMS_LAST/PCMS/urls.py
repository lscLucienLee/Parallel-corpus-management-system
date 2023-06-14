"""
URL configuration for PCMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app1.views import Login
from app1.views import Register
from app1.views import Browse
from app1.views import Update
from app1.views import Correct
from app1.views import Manage
from app1.views import Add
from app1.views import Divide
from app1.views import Merge
from app1.views import Create
from app1.views import Operate
from app1.views import Filter
from app1.views import Remove
from app1.views import Normalize
from app1.views import Analyse
from app1.views import Grade
from app1.views import Align
from app1.views import File

from app1.views import Index

urlpatterns = [

    # path('admin/', admin.site.urls),

    path('index/', Index.index),
    path('indexx/', Index.indexx),
    path('indexxxx/', Index.indexxxx),
    path('iindex/', Index.iindex),
    path('iiindex/', Index.iiindex),
    path('iiiindex/', Index.iiiindex),
    path('outo/', Index.outo),
    path('ana/', Index.ana),

    # Login
    path('login/', Login.login),

    # Register
    path('register/', Register.register),

    # Manage
    path('manage/', Manage.manage),
    path('manage/data/', Manage.manage_data),
    path('delete_corpuses/', Manage.delete_corpuses),
    path('correct/', Correct.correct),
    path('create/', Create.manual_create),
    path('create/manual/', Create.input_add),
    path('last_or_next/', Create.last_or_next),
    path('create/file/', Create.file_create),

    # Browse
    path('browse/', Browse.browse),
    path('browse/data/', Browse.browse_data),
    path('browse/search/', Browse.browse_search),
    path('delete_corpus/', Browse.delete_corpus),
    path('update/', Update.update),
    path('add/', Add.add),

    # Divide
    path('divide/', Divide.divide),
    path('divide/corpus_name/', Divide.divide_corpus_name),
    path('divide/data/', Divide.divide_data),

    # Merge
    path('merge/', Merge.merge),
    path('merge/corpus_name/', Merge.merge_corpus_name),
    path('merge/data/', Merge.merge_data),

    # operate
    path('operate/', Operate.operate),
    path('filter/', Filter.filter),
    path('normalize/', Normalize.normalize),
    path('remove/', Remove.remove),
    path('analyse/', Analyse.analyse),
    path('analyse/data/', Analyse.analyse_data),
    path('analyse/search/', Analyse.analyse_search),
    path('manual_eval/', Grade.manual_eval),
    path('grade/', Grade.grade),
    path('grade/data/', Grade.grade_data),
    path('auto/', Grade.auto_eval),
    path('auto/data/', Grade.auto_data),
    path('align/', Align.align),
    path('align/data/', Align.align_data),
    path('align/next/', Align.align_next),

    # path('merge/', views.merge),
    # path('divide/', views.divide),

    # path('translate/', views.translate),
    # path('align/', views.align)
    path('upload/', File.upload_file),
    path('upload/manual/', Grade.upload_manual_file),
    path('upload/import/', Create.upload_import_file),
    path('upload/auto/', Grade.upload_auto_file),
    path('download/align/<str:file_name>/', Align.download_align_file),
]
