from django.urls import path


app_name = "users"




from . import views


urlpatterns = [
    path('', views.index, name='profiles'),
    path(r"time", views.time),
    path(r"jump", views.jump),
    path(r"temp", views.temp),



    #path("profile/", views.PROFILE_LIstView.as_view(), name="profile_index"), #profile_info

    path("profile/"                 , views.PROFILE.as_view(),      name="profile_index"),

    path("profile/create/"          , views.PROFILE_CreateView.as_view(),    name="profile_create"),


    path("profile/<int:pk>/update/" , views.PROFILE_UpdateView.as_view(),    name="profile_update"),

    path("profile/<int:pk>/delete/" , views.PROFILE_DeleteView.as_view(),    name="profile_delete"),

   # path("profile/<int:pk>/", views.PROFILE_DetailView.as_view(), name="profile_detail"),

]

