from django.urls import path
from . import views


urlpatterns = [
    # path("", views.review, name="user-review-page"),
    # path("thank-you", views.thank_you,name="thank-you-page")
    path("", views.ReviewView.as_view(), name="user-review-page"),
    path("thank-you", views.ThankYouView.as_view(),name="thank-you-page"),
    path("reviews", views.ReviewsListView.as_view(),name="review-list-page"),
    path("reviews/favorite", views.AddFavoriteView.as_view()),
    path("reviews/<int:pk>", views.SingleView.as_view(),name="detail-review-page")
]