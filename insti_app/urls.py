from django.urls import path
from .views import * 


urlpatterns = [
    path("", insti_page,name='insti_name'),
    path("submitted",submitted_insti,name='submit_insti'),
    path("submit",submit_view,name='submit_view'),

#    path("goggle",views.google,name='google_name'),
#   path('', TemplateView.as_view(template_name="google.html")),
#   path('accounts/', include('allauth.urls')),
#   path('logout', LogoutView.as_view()),
]