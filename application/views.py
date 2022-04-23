from django.shortcuts import render, redirect
from .models import *

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages


# Web Scapping Packages
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')

    elif request.method == 'POST':
        searchName = request.POST.get('search', '')

        my_url = f'https://www.amazon.ca/s?k={searchName}&ref=nb_sb_ss_recent_1_0_recent'

        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")

        productNameList = []
        productPriceList = []

        
        try:
            for item in page_soup.findAll("div",{"class":"a-section a-spacing-small s-padding-left-small s-padding-right-small"}):
            #     print(item.span.text)
                productNameList.append(item.span.text)
                
            for item in page_soup.findAll("a",{"class":"a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"}):
                price = item.find('span', attrs={'class':'a-offscreen'}).text
            #     print(price1)
                productPriceList.append(price)
                
            try:
                for i in range(0,len(productNameList)+1):
                    print(f'The price of the product {productNameList[i]} is {productPriceList[i]}.')
            except:
                pass
        except:
            pass

        productDict = dict(zip(productNameList, productPriceList))

        var = {
            'productNameList': productNameList,
            'productPriceList': productPriceList,
            'productName': searchName,
            'productDict': productDict,
        }

        return render(request, 'productlist_search.html', var)


def product(request,category,name):
    productName = name
    productCategory = category

    # print("->",productName)

    my_url = f'https://www.amazon.ca/s?k={productName}&ref=nb_sb_ss_recent_1_0_recent'

    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")

    productNameList = []
    productPriceList = []

    

    for item in page_soup.findAll("div",{"class":"a-section a-spacing-small s-padding-left-small s-padding-right-small"}):
    #     print(item.span.text)
        productNameList.append(item.span.text)
        
    for item in page_soup.findAll("a",{"class":"a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"}):
        price = item.find('span', attrs={'class':'a-offscreen'}).text
    #     print(price1)
        productPriceList.append(price)
        
    try:
        for i in range(0,len(productNameList)+1):
            print(f'The price of the product {productNameList[i]} is {productPriceList[i]}.')
    except:
        pass

    productDict = dict(zip(productNameList, productPriceList))

    var = {
        'productNameList': productNameList,
        'productPriceList': productPriceList,
        'productName': productName,
        'productDict': productDict,
        'productCategory': productCategory,
    }

    # print(productDict)
    return render(request, 'productlist.html', var)





