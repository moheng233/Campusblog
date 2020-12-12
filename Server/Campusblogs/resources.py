from import_export import resources
from .models import Blogs

class BlogsResources(resources.ModelResource):
    class Meta:
        model = Blogs