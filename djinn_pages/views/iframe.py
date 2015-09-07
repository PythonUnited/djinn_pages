from django.views.generic import TemplateView


class IFrameView(TemplateView):

    template_name = 'djinn_pages/iframe.html'

    def get_context_data(self, **kwargs):

        ctx = super(IFrameView, self).get_context_data(**kwargs)

        ctx['view'] = self

        return ctx
