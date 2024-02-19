from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views import generic
import requests
import os
from datetime import datetime
from django_user_agents.utils import get_user_agent

class IndexView(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        api_endpoint = "https://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
        api_key = os.environ.get("API_KEY")

        context = super().get_context_data(**kwargs)

        params = {
            "key": api_key,
            "keyword": "インスタ映え",
            "count": 50,
            "format":"json",
        }
        response = requests.get(api_endpoint, params=params)


        if response.status_code == 200:
            data = response.json()

            gourmet_photo = data["results"]["shop"]

            context["gourmet_photo"] = gourmet_photo

            is_mobile = get_user_agent(self.request).is_mobile
            context["is_mobile"] = is_mobile

            return context
        
        else:
            # エラーメッセージを表示
            pass

        

class SearchView(generic.TemplateView):
    template_name = "search.html"


def gourmet_list(request):

    api_endpoint = "https://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
    api_key = os.environ.get("API_KEY")

    genre = request.GET.get("genre", "")
    budget = request.GET.get("budget", "")
    range = request.GET.get("range", "")
    lat = request.GET.get("lat", "")
    lng = request.GET.get("lng", "")


    params = {
        "key": api_key,
        "genre": genre,
        "budget": budget,
        "count": 60,
        "lat": lat,
        "lng": lng,
        "range": range,
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

        is_mobile = get_user_agent(request).is_mobile

        context = {
            "page_obj": page_obj,
            "is_mobile": is_mobile,
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

        current_time = datetime.now().time()
        is_mobile = get_user_agent(request).is_mobile

        print(gourmet_detail)


        context = {
            "detail": gourmet_detail,
            "current_time": current_time,
            "is_mobile": is_mobile,
        }

        return render(request, "detail.html", context)
    else:
        pass
