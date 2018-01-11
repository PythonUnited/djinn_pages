
def get_urls():

    from .urls import urlpatterns

    return urlpatterns

def get_js():

    return ["djinn_pages.js"]

def get_css():

    return ["djinn_pages.css"]
