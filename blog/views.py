from django.shortcuts import render

# Create your views here.
# -*-coding:utf-8-*-

from django.views import View



from sfedu import settings

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.core.mail import send_mail

from .forms import ContactForm

from django.conf import settings


from django.template.context_processors import csrf

from django.shortcuts import render, get_object_or_404, render_to_response

# Create your views here.
# from blog.forms import CommentForm
from blog.forms import NameForm
from blog.models import Blog, add_teacher, Category, CategoryFile , Time_table , Documentation







def home(request):
    search_articles = Blog.objects.all()


    context = {}
    search_articles = list(reversed(search_articles))
    context['article_add'] = search_articles[0:2]
    category = Category.objects.all()
    context['category'] = category

    # if request.method == 'POST':
    #
    #     context = {}
    #     context.update(csrf(request))
    #     # create a form instance and populate it with data from the request:
    #     form = NameForm(request.POST)
    #     Blog.pages = form.data['your_name']
    #
    #     context['article_add'] = search_articles[0:2]
    #     category = Category.objects.all()
    #     context['category'] = category
    current_page = Paginator(search_articles, Blog.pages)

    page = request.GET.get('page')

    try:
        context['article_lists'] = current_page.page(page)
    except PageNotAnInteger:
        context['article_lists'] = current_page.page(1)
    except EmptyPage:
        context['article_lists'] = current_page.page(current_page.num_pages)

    # if Blog.image == None:
    #     search_articles.delete(search_articles.image)

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')


def show_article(request, article_id):
    article = get_object_or_404(Blog, id=article_id)
    return render(request, 'blog/article.html', {'article': article})

def contacts(request):
    return render(request, 'blog/contacts.html')


def information(request):
    return render(request, 'blog/information.html')


def faculty(request):
    teacher = add_teacher.objects.all()
    return render(request, 'blog/information/faculty.html', {'teachers': teacher})


def schedule(request):
    timetable = {}
    timetable['tables'] = Time_table.objects.all()
    return render(request, 'blog/information/timetable.html', timetable)

def documentation(request):
    documentation = {}
    documentation['document'] = Documentation.objects.all()
    return render(request, 'blog/information/documentation.html',documentation)

def NewsList(request, slug):
    category = Category.objects.select_related().get(slug=slug)
    news = category.blog_set.all()
    return render(request, 'blog/category_article.html', {'news': news,
                                                   'category': category})

class EContactsView(View):
    template_name = 'blog/contacts.html'

    # В случае get запроса, мы будем отправлять просто страницу с контактной формой
    def get(self, request, *args, **kwargs):
        context = {}
        context.update(csrf(request))    # Обязательно добавьте в шаблон защитный токен
        context['contact_form'] = ContactForm()

        return render_to_response(template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        context = {}

        form = ContactForm(request.POST)

        # Если не выполнить проверку на правильность ввода данных,
        # то не сможем забрать эти данные из формы... хотя что здесь проверять?
        if form.is_valid():
            email_subject = 'EVILEG :: Сообщение через контактную форму '
            email_body = "С сайта отправлено новое сообщение\n\n" \
                         "Имя отправителя: %s \n" \
                         "E-mail отправителя: %s \n\n" \
                         "Сообщение: \n" \
                         "%s " % \
                         (form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message'])

            # и отправляем сообщение
            send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, ['target_email@example.com'], fail_silently=False)

        return render_to_response(template_name=self.template_name, context=context)

def library(request):
    return render(request, 'blog/library.html')

def libraries(request, slug):
    category = CategoryFile.objects.select_related().get(slug=slug)
    library = category.uploadfileform_set.all()
    return render(request, 'blog/library_files.html', dict(library=library, category=category))
