
from django.urls import path
from . import views
app_name = "main"
urlpatterns = [
    path("", views.index, name = "ShopHome"),
    path("about/", views.about, name = "AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name = "Search"),
    path("products/<int:product_id>", views.productView, name = "productView"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login")

   ]
