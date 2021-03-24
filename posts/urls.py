from django.contrib import admin
from . import views
from django.urls import path
admin.site.site_header = "Sajid' Blog"
admin.site.index_title = "Sajid's Blog"
admin.site.site_title = "Sajid's Blog"

urlpatterns = [
    path('',views.PostList.as_view(),name = 'home'),
    path('<slug:slug>/<int:pk>',views.PostDetail.as_view(),name = 'post_detail'),
    path("search",views.search,name = "search"),
    path("<int:pk>/comment",views.post_comment,name="comment"),
    path("*/<int:pk>/",views.delete_comment,name="delete")
]