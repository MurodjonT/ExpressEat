from django.shortcuts import render
from django.views.generic import TemplateView,ListView, CreateView
from .models import Mahsulotlar, Comments
from django.core.paginator import Paginator
import requests
from django.urls import reverse_lazy


# keyingi holatlar uchun
from .models import *
from django.http import JsonResponse
import json

class HomePageView(ListView):
	model = Mahsulotlar
	template_name = 'index.html'


# 3-bosqich
# avvalgi holat
# def MenuPageView(request):
# 	obj = Mahsulotlar.objects.all()
# 	page_n = request.GET.get('page',1)
# 	p = Paginator(obj,3)
# 	try:
# 		page = p.page(page_n)
# 	except Exception:
# 		page = p.page(1)
# 	context = {
# 	'page': page
# 	}
# 	return render(request,'menu.html',context)


# keyingi holat
def menuPageView(request):
	if request.user.is_authenticated:
		customer = request.user
		print(request.user)
		order, created = Order.objects.get_or_create(customer=customer,complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items # savatdagi mahsulotlar soni
	else:
		items = []
		order = {'get_cart_total': 0, "get_cart_items": 0}
		cartItems = order['get_cart_items'] # qaysi funksiya orqali hisoblasin

	obj = Mahsulotlar.objects.all()
	page_n = request.GET.get('page',1)
	p = Paginator(obj,3)
	try:
		page = p.page(page_n)
	except Exception:
		page = p.page(1)
	context = {
	'page': page,
	'cartItems':cartItems
	}
	return render(request,'menu.html',context)
# ====> urls.py fayilimizda davom etamiz


# from django.http import JsonResponse
# import json
# Mahsulotlarni qushishni bajarish uchun funsiya yozamiz
def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	# print('Bosildi: ',action) #terminalda mahsulot ID si ko'rinishi kerak
	# print('Mahsulot IDsi: ',productId)

	# keyingi uzgarish POST create qilish
	# base.html dagi savat iconi ga  mahsulot soni korsatishimiz kerak
	customer = request.user
	product = Mahsulotlar.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer,complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)
	
	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)
	# ushbu funksiyaga url yasashimiz kerak


# cart.html uchun funksiya
def cart(request):
	if request.user.is_authenticated:
		customer = request.user
		order, created = Order.objects.get_or_create(customer=customer,complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		# reverse_lazy('login')
		items = []
		order = {'get_cart_total': 0, "get_cart_items": 0}
		cartItems = order['get_cart_items']

	context = {"items": items,"order": order,'cartItems':cartItems }
	return render(request, 'cart.html', context)
	# ushbu funksiyaga url yasashimiz kerak
	# base html dagi savat urliga cart ni belgilab quyishimiz kerak





def telegram_bot_sendtext(bot_message):
  bot_token ='5130152396:AAGiHy6qCBX9Yc8cxEyhsbn1Twzk_pdWL5E'
  bot_chatID ='1129151347'
  send_text ='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode =Markdown&text=' + bot_message 
  response =requests.get(send_text)
  return response.json()





def BookPageView(request):
    if request.method == 'POST':
        name = request.POST.get('name',None)
        phone = request.POST.get('phone',None)
        email = request.POST.get('email',None)
        message = request.POST.get('message',None)
        user = Comments.objects.create(
            userName = name,
            phone = phone,
            email = email,
            message = message
            )
        user.save()
        telegram_bot_sendtext(f"Ismi: {name} \nTelfon raqam: {phone} \nEmail: {email} \nXabar jonatdi: {message}") 

       
    return render(
    request=request,
    template_name= 'book.html'
    )
# class BookPageView(TemplateView):
# 	template_name = 'book.html'


class AboutPageView(TemplateView):
	template_name = 'about.html'


class ProductCreateView(CreateView):
    model = Mahsulotlar
    template_name = 'product_create.html'
    # fields = ('mahsulot_nomi','mahsulot_tarkibi','mahsulot_rasmi','mahsulot_narxi')
    fields = '__all__'
    success_url = reverse_lazy('index')