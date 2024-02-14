from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views import generic
import requests
import os

class IndexView(generic.TemplateView):
    template_name = "index.html"

class SearchView(generic.TemplateView):
    template_name = "search.html"


def gourmet_list(request):

    api_endpoint = "https://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
    api_key = os.environ.get("API_KEY")

    keywords = request.GET.get("keywords", "")
    budget = request.GET.get("budget", "")
    range = request.GET.get("range", "")
    lat = ""
    ing = ""

    params = {
        "key": api_key,
        "keyword": keywords,
        "count": 50,
        "format":"json",
    }



    response = requests.get(api_endpoint, params=params)


    if response.status_code == 200:
        data = response.json()

        gourmet_list = data["results"]["shop"]

        per_page = 10
        page_num = request.GET.get("page", 1)
        paginator = Paginator(gourmet_list, per_page)
        page_obj = paginator.get_page(page_num)

        context = {
            "page_obj": page_obj,
        }

        return render(request, "gourmet_list.html", context)
    else:
        # エラーメッセージを表示
        pass


def detail_view(request, id):

    api_endpoint = "https://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
    api_key = "1b1c0aede467a3f4"


    params = {
        "key": api_key,
        "id": id,
        "format":"json",
    }

    response = requests.get(api_endpoint, params=params)
    if response.status_code == 200:
        data = response.json()

        gourmet_detail = data["results"]["shop"][0]

        print(gourmet_detail)

        context = {
            "detail": gourmet_detail,
        }

        return render(request, "detail.html", context)
    else:
        # エラーメッセージを表示
        pass
