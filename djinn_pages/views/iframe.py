from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView
from djinn_pages.models import AllowedIFrameURL


class IFrameView(TemplateView):

    template_name = 'djinn_pages/iframe.html'

    def get_context_data(self, **kwargs):

        ctx = super(IFrameView, self).get_context_data(**kwargs)

        ctx['view'] = self
        try:
            if 'load_url' in self.request.GET:
                # Maybe we should drop the 'load_url' variant in future, in
                # favour of 'url_name'
                ctx['validated_url'] = AllowedIFrameURL.objects.get(
                    url=self.request.GET['load_url']).url
            else:
                if 'url_name' in self.request.GET:
                    ctx['validated_url'] = AllowedIFrameURL.objects.get(
                        url_name=self.request.GET['url_name']).url
        except AllowedIFrameURL.DoesNotExist as dne:
            ctx['error_message'] = _('requested URL is not allowed')
            pass
        except Exception as exc:
            ctx['error_message'] = _('Exception finding requested URL')
            print(exc)
            pass

        return ctx
