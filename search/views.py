from django.shortcuts import render_to_response, render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import View
from blog.models import Blog ,Category , add_teacher , UploadFileForm , Time_table,Documentation


class ESearchView(View):
    template_name = 'blog/search.html'

    def get(self, request, *args, **kwargs):
        context = {}
        question = request.GET.get('q')

        if question[0] == '#':
            new_question = question[1:len(question)]
            search = Category.objects.get(title=new_question)
            search_tags = search.blog_set.all()
            # формируем строку URL, которая будет содержать последний запрос
            # Это важно для корректной работы пагинации
            context['last_question'] = '?q=%s' % new_question
            context['tag'] = question
            current_page = Paginator("Search", 10)
            context['len_article'] = len(search_tags)

            context['tag_list'] = search_tags

            return render(request,'blog/search.html', context=context)

        elif question is not None:
            table_search = Time_table.objects.filter(name__search=question)
            search_articles = Blog.objects.filter(text__search=question)
            if len(search_articles)==0:
                search_articles = Blog.objects.filter(title__search=question)
            teacher_search  = add_teacher.objects.filter(name__search=question)
            doc_search = Documentation.objects.filter(title__search=question)
            files_search = UploadFileForm.objects.filter(title__search=question)
            # формируем строку URL, которая будет содержать последний запрос
            # Это важно для корректной работы пагинации
            context['last_question'] = '?q=%s' % question
            context['d_l'] = doc_search
            context['tb_l'] = table_search
            context['t_l'] = teacher_search
            context['f_l'] =  files_search
            page = request.GET.get('page')
            leng  = len(search_articles)+len(teacher_search)+len(files_search)+len(table_search)+len(doc_search)

            context['len_find'] = leng
            if (leng==0):
                context['message'] = 'Упс! Ничего не найдено :('
            current_page = Paginator(search_articles, 10)
            try:
                context['article_lists'] = current_page.page(page)
            except PageNotAnInteger:
                context['article_lists'] = current_page.page(1)
            except EmptyPage:
                context['article_lists'] = current_page.page(current_page.num_pages)

            return render_to_response(template_name=self.template_name, context=context)
