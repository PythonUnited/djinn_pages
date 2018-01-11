from django.conf.urls import url
from django.urls import include

from .views.iframe import IFrameView


_urlpatterns = [
    url(r"^ipage",
        IFrameView.as_view(),
        name="djinn_pages_iframeview"),

]

urlpatterns = [
    url(r'^djinn_pages/', include(_urlpatterns)),
]
