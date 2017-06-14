from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = format_suffix_patterns([
    url(r'^find_avatar_key/(?P<name>.*)/$',
        views.FindAvatarKey.as_view()),
    url(r'^avatar_info/(?P<uuid>.*)/$',
        views.AvatarInfo.as_view()),
    url(r'^find_marketplace_store/(?P<name>.*)/$',
        views.FindMarketplaceStore.as_view()),
    url(r'^marketplace_product_info/(?P<url>.*)/$',
        views.MarketplaceProductInfo.as_view()),
])

