# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.

def helloWorld(request):
    '''start point test path function'''
    template = loader.get_template('helloworld.html')
    # return HttpResponse("Hello World!!!")
    return HttpResponse(template.render())


def members(request):
    '''displays members of the app'''
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members_block.html')
    context = {
        'mymembers' : mymembers
    }
    # print('mymembers===>>>', mymembers)
    return HttpResponse(template.render(context, request))


def details(request, id):
    member = Member.objects.get(id=id)
    template = loader.get_template('member_detail_block.html')
    context = {
        'member' : member
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def test(request):
    template = loader.get_template('template.html')
    context = {
        'fruits' : ['Banana', 'Apple', 'Orange']
    }
    return HttpResponse(template.render(context, request))
