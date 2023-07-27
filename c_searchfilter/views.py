from django.shortcuts import render
from django.views import View
from c_searchfilter.models import Info
from django.db.models import Q


class Home(View):
    def get(self,request):
        employees = Info.objects.all() 
        context = { 
        'employees': employees,
        }
        return render(request, 'c_searchfilter/home.html', context)



# def home(request):
#     employees = Info.objects.all() 

#     context = { 
#         'employees': employees,
#     }
#     return render(request, 'c_searchfilter/home.html', context)



class Search(View):
    def get(self,request):
        try:
            query = request.GET.get('q')
            search_results = Info.objects.filter(Q(name__icontains=query) | Q(address__icontains=query))
            context = {'search_results': search_results,}
            return render(request, 'c_searchfilter/home.html', context)
        except Exception as e:
            print(e)
            raise e



# def search(request):
#     query = request.GET['q']

#     search_results = Info.objects.filter(
#         Q(name__icontains=query) | Q(address__icontains=query)
#     )

#     context = {
#         'search_results': search_results,
#         'query': query,
#     }
#     return render(request, 'c_searchfilter/search.html', context)