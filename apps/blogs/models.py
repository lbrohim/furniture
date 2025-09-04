from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class BlogCategoryModel(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog category'
        verbose_name_plural = 'Blog categories'


class BlogTagModel(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog tag'
        verbose_name_plural = 'Blog tags'


class BlogAuthorModel(BaseModel):
    full_name = models.CharField(max_length=64)
    avatar = models.ImageField(
        upload_to='blog-author/'
    )
    bio = models.CharField(max_length=256)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Blog author'
        verbose_name_plural = 'Blog authors'


class BlogModel(BaseModel):
    class BlogStatus(models.TextChoices):
        DRAFT = 'DRAFT'
        PUBLISHED = 'PUBLISHED'
        DELETED = 'DELETED'

    image = models.ImageField(upload_to='blog-post/')
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()

    status = models.CharField(
        max_length=20,
        choices=BlogStatus,
        default=BlogStatus.DRAFT
    )

    author = models.ForeignKey(
        BlogAuthorModel,
        on_delete=models.CASCADE,
        related_name='blogs'
    )
    category = models.ManyToManyField(
        BlogCategoryModel,
        related_name='blogs'
    )
    tag = models.ManyToManyField(
        BlogTagModel,
        related_name='blogs'
    )

    def views_count(self):
        return self.views.distinct().count()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'



