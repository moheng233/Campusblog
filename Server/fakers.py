from django_seed import Seed

seeder = Seed.seeder(locale="zh_CN");

from Campusblogs.models import Blogs, Classify, UploadImages;
from Campusauth.models import User

TestUser = User.objects.get(username="test1");
TestClassify = Classify.objects.get(title="普通的分类")
Testsubimage = UploadImages.objects.get(id="1")

seeder.add_entity(Blogs,20,{
    'user': TestUser,
    'classify': TestClassify,
    'subimage': Testsubimage
})

data = seeder.execute()