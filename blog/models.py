from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.utils.html import format_html
from extensions.utils import jalali_converter

from accounts.models import CustomUser


class ArticleComment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name="blog_comment", null=True, blank=True, verbose_name='مقاله مرتبط')
    fullname = models.CharField(max_length=250, verbose_name='نام')
    body = models.TextField(verbose_name="متن")
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='زمان ایجاد شده')
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name='زمان آپدیت شده')

    is_show = models.BooleanField(default=True, verbose_name='وضعیت نمایش')


    def __str__(self):
        return self.fullname


    def jpublished(self):
        return jalali_converter(self.created)
    jpublished.short_description = 'زمان انتشار'

    class Meta:
        verbose_name = 'کامنت ها'
        verbose_name_plural = 'کامنت'


class ArticleCategoryModel(models.Model):
    title = models.CharField(max_length=350, db_index=True, verbose_name='عنوان')
    url_title = models.CharField(
        max_length=350, verbose_name='عنوان در url', null=True)
    meta_description = models.TextField(
        verbose_name='متا description', null=True)

    created = models.DateTimeField(auto_now_add=True, null=True,verbose_name='زمان ایجاد')
    updated = models.DateTimeField(auto_now=True, null=True,verbose_name='زمان آپدیت')


    def __str__(self):
        return self.title
    
    def jpublished(self):
        return jalali_converter(self.created)
    jpublished.short_description = 'زمان انتشار'


    class Meta:
        verbose_name = 'دسته بندی مقاله'
        verbose_name_plural = 'دسته بندی مقالات'

class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش نویس'),
        ('p', 'منتشر شده')
    )
    # comment = models.ForeignKey('ArticleComment', on_delete=models.CASCADE, related_name='relate_comment', verbose_name='کامنت', blank=True, null=True)

    tag_title = models.CharField(max_length=350, verbose_name='عنوان (در tag title)', db_index=True, null=True)
    h1_title = models.CharField(max_length=350, verbose_name='عنوان (در tag h1)', db_index=True, null=True)
    meta_description = models.TextField(verbose_name='متا description', null=True)
    slug = models.SlugField(max_length=255, verbose_name='ادرس url', unique=True, db_index=True, allow_unicode=True)
    body = RichTextUploadingField(verbose_name='متن')
    short_description = models.TextField(verbose_name='توضیحات کوتاه', null=True)

    thumbnail = models.ImageField(upload_to='thumbnails', verbose_name='عکس بند انگشتی')


    category = models.ForeignKey(ArticleCategoryModel, on_delete=models.CASCADE, related_name='article_category', verbose_name='دسته بندی', null=True)

    og_type = models.CharField(max_length=300, null=True, blank=True)
    og_title = models.CharField(max_length=300, null=True, blank=True)
    og_desc = models.CharField(max_length=300, null=True, blank=True)
    og_image = models.ImageField(upload_to='thumbnails', null=True, blank=True)
    og_url = models.CharField(max_length=300, null=True, blank=True)
    canonical_url = models.CharField(max_length=300,  blank=True, null=True)
    published = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار', null=True)

    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت', null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='نویسنده')


    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='زمان ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='زمان آپدیت')
    def __str__(self):
        return self.tag_title

    def jpublished(self):
        return jalali_converter(self.published)
    jpublished.short_description = 'زمان انتشار'

    def thumbnail_tag(self):
        return format_html("<img width=100 height=75 style='border-radius: 5px' src='{}'>".format(self.thumbnail.url))
    thumbnail_tag.short_description = 'عکس'

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

