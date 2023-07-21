from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='home'),
    path('resume/', views.ResumeView.as_view(), name='resumeform'),
    path('<int:pk>',views.Candidate.as_view(), name='candidate'),
    path('all/', views.AllCandidate.as_view(), name='all'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)