from rest_framework import serializers

from blog.models import Article, ArticleComment, ArticleCategoryModel
from redirects.models import Redirect

# --------------------------------------------------------
SEARCH_PATTERN = 'src=\"/media/editor_images/'
SITE_DOMAIN = "https://api.saeedaminy.ir"
REPLACE_WITH = f'src=\"{SITE_DOMAIN}/media/editor_images/'

class FixAbsolutePathSerializer(serializers.Field):
    def to_representation(self, value):
        text = value.replace(SEARCH_PATTERN, REPLACE_WITH)
        return text
# --------------------------------------------------------
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategoryModel
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleComment
        fields = ['id', 'article', 'fullname', 'body', 'jpublished']


class ArticleListSerializer(serializers.ModelSerializer):
    def get_author(self, obj):
        return {
            "fname": obj.author.first_name,
            "lname": obj.author.last_name,
        }
    author = serializers.SerializerMethodField('get_author')
    category = CategorySerializer()
    body = FixAbsolutePathSerializer()

    class Meta:
        model = Article
        fields = ['id', 'tag_title', 'h1_title', 'meta_description', 'slug', 'thumbnail',
                  'body', 'status', 'jpublished', 'short_description', 'category', 'og_type', 'og_title', 'og_desc',
                  'og_image', 'og_url', 'canonical_url', 'author']


class RedirectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Redirect
        fields = ['id', 'request_url', 'destination_url', 'status_code']