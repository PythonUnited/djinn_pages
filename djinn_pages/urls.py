from django.conf.urls import patterns, url, include
from djinn_pages.views.iframe import IFrameView


_urlpatterns = patterns(
    "",

    url(r"^ipage/(?P<loadurl>[\w-\/:\d]*)",
        IFrameView.as_view(),
        name="djinn_pages_iframeview"),

    )

urlpatterns = patterns(
    '',

    (r'^djinn_pages/', include(_urlpatterns)),
)
