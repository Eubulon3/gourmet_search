from django.shortcuts import render
from django.views import generic
import requests

class IndexView(generic.TemplateView):
    template_name = "index.html"

class SearchView(generic.TemplateView):
    template_name = "search.html"

# class GourmetListView(generic.ListView):
#     template_name = "gourmet_list.html"

def gourmet_list(request):

    api_endpoint = "https://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
    api_key = "1b1c0aede467a3f4"

    keyword = request.GET.get("keyword", "")
    # search2 = request.GET.get("search2", "")

    params = {
        "key": api_key,
        "keyword": keyword,
        "format":"json",
    }

    print(params)


    response = requests.get(api_endpoint, params=params)


    if response.status_code == 200:
        data = response.json()

        context = {
            "gourmet_list": data["results"]["shop"],
        }
        return render(request, "gourmet_list.html", context)
    else:
        # エラーメッセージを表示
        pass