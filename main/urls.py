from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('templates/main/style.css', TemplateView.as_view(
        template_name='style.css',
        content_type='text/css'),
    ),
    path('', views.index, name='index'),
    path('create', views.create, name="create"),
    path('<int:pk>', views.FilmDetailView.as_view(), name='film-detail'),
    path('<int:pk>/update', views.FilmUpdateView.as_view(), name='film-update'),
    path('<int:pk>/delete', views.FilmDeleteView.as_view(), name='film-delete'),
]
