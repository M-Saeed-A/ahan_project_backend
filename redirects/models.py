from django.db import models


class Redirect(models.Model):
    REDIRECT_STATUS_CODE = (
        ('301', '301'),
        ('302', '302'),
        ('410', '410'),
    )

    request_url = models.CharField(
        max_length=350, verbose_name='آدرس مبدأ')  # from url
    destination_url = models.CharField(
        max_length=350, verbose_name='آدرس مقصد')  # to url

    status_code = models.CharField(
        max_length=250, choices=REDIRECT_STATUS_CODE, verbose_name='نوع ریدایرکت')

    created = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name='زمان ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='زمان آپدیت')

    class Meta:
        verbose_name = 'ریدایرکت'
        verbose_name_plural = 'ریدایرکت ها'
