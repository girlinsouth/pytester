#-*-coding:utf8-*-
from django.shortcuts import render_to_response,RequestContext,redirect
from pybug.models import pybugs
from django.db.models import Q
from django.http import HttpResponse
import json
from django.utils.datastructures import SortedDict
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger

def index(request):
    return render_to_response("index.html")

def allBugs(request):
    try:
        kwd = str(request.GET.get('kwd',''))
        status = int(request.GET.get('status',0))
        projects = int(request.GET.get('projects',0))
    except ValueError:
        kwd = ''
        status = 0
        projects = 0

    if kwd != '':
        allbugs = pybugs.objects.filter(Q(title__contains=kwd) | Q(content__contains=kwd) | Q(remarks__contains=kwd)).order_by('-updateTime')
    else:
        allbugs = pybugs.objects.order_by('-updateTime')

    if projects > 0:
        allbugs = allbugs.filter(project=projects)

    if status > 0:
        allbugs = allbugs.filter(status=status)

    result = getBug(request,allbugs)
    return HttpResponse(json.dumps(result),content_type="application/json")

def getBug(request,datas):
    try:
        pagesize = int(request.GET.get("pagesize",2))
        page = int(request.GET.get('page',1))
    except ValueError:
        pagesize = 2
        page = 1

    getpage = setPage(request,datas,pagesize,page)
    outputData = getpage["datas"]
    pages = getpage["pages"]
    result = SortedDict()
    body = SortedDict()
    head = SortedDict()
    allbugdata = []
    for allbug in outputData:
        data = SortedDict()
        data["ID"] = allbug.id
        data["project"] = allbug.project
        data["title"] = allbug.title
        data["serious"] = allbug.serious
        data["priority"] = allbug.priority
        data["assigner"] = allbug.assigner
        data["fixer"] = allbug.fixer
        data["fixWay"] = allbug.fixWay
        data["creater"] = allbug.creater
        data["updateTime"] = allbug.updateTime.strftime("%Y-%m-%d %H:%I:%S")
        allbugdata.append(data)
    body["data"] = allbugdata
    body["pages"] = pages
    head["code"] = 0
    result["body"] = body
    result["head"] = head
    return result

def setPage(request,datalist,pagesize,page):
    paginator = Paginator(datalist, pagesize)
    resultdata = {}
    pagecount = paginator.num_pages
    pagerange = paginator.page_range
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage,PageNotAnInteger):
        posts = paginator.page(paginator.num_pages)

    resultdata["datas"] = posts
    resultdata["pages"] = pagecount
    resultdata["pagerange"] = pagerange
    return resultdata

