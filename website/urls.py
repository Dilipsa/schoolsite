"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from student.views import (
                        create_student_view, 
                        update_student_view,
                        student_list_view,
                        student_detail_view,
                        student_delete_view,
                    )

from users.views import register_user_view, login_user_view, logout_user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', create_student_view),
    path('update_student/<int:id>/', update_student_view),
    path('student_list/', student_list_view),
    path('student_detail/<int:id>/', student_detail_view),
    path('student_delete/<int:id>/', student_delete_view),
    path('register_user/', register_user_view),
    path('login_user/', login_user_view),
    path('logout_user/', logout_user_view),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
