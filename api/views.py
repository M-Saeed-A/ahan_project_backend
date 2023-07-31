from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from blog.models import Article, ArticleComment, ArticleCategoryModel
from redirects.models import Redirect
from .serializers import ArticleListSerializer, CommentSerializer, CategorySerializer, RedirectSerializers
from .pagination import StandardResultsSetPagination

class ArticleList(ListAPIView):
    queryset = Article.objects.all().filter(status='p')
    serializer_class = ArticleListSerializer
    pagination_class = StandardResultsSetPagination
class AllArticleList(ListAPIView):
    queryset = Article.objects.all().filter(status='p')
    serializer_class = ArticleListSerializer

class LastArticleList(ListAPIView):
    queryset = Article.objects.all().filter(status='p').order_by('-id')[:4]
    serializer_class = ArticleListSerializer

class ArticleDetail(RetrieveAPIView):
    queryset = Article.objects.all().filter(status='p')
    serializer_class = ArticleListSerializer
    lookup_field = 'slug'

class ArticleComment(ListCreateAPIView):
    queryset = ArticleComment.objects.filter(is_show = True)
    serializer_class = CommentSerializer

class ArticleCategory(ListAPIView):
    queryset = ArticleCategoryModel.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(RetrieveAPIView):
    queryset = ArticleCategoryModel.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'url_title'

class RedirectList(ListAPIView):
    queryset = Redirect.objects.all()
    serializer_class = RedirectSerializers
