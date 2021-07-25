from django.shortcuts import render , HttpResponse
from .models import Order

def createOrder(request):
        test = 0
        if request.method == 'POST':
                if request.POST.get('namelastname') and request.POST.get('address') and request.POST.get('phone'):
                        name = request.POST.get('namelastname') if request.POST.get('namelastname') is not None else "user"
                        address = request.POST.get('address') if request.POST.get('address') is not None else "address"
                        phone = request.POST.get('phone') if request.POST.get('phone') is not None else "phone"
                        class order:
                                name = " "
                                count = 0
                                price = 0
                                def __init__(self, name,count,price): 
                                        self.name = name
                                        self.count = count
                                        self.price = price
                        item = []
                        item.append(order("Marqarita",request.POST.get('marqarita'),13.5))
                        item.append(order("Qril Toyuq",request.POST.get('qril_toyuq'),13.2))
                        item.append(order("Bol 5li",request.POST.get('bol_5li'),12.9))
                        item.append(order("Kalipso",request.POST.get('kalipso'),14.9))
                        item.append(order("Italiano",request.POST.get('italiano'),16.5))
                        item.append(order("Hamburger",request.POST.get('hamburger'),1.6))
                        item.append(order("Chickenburger",request.POST.get('chicken_burger'),2.4))
                        item.append(order("Pepperoni",request.POST.get('pepperoni'),13.8))
                        item.append(order("Dabl Hamburger",request.POST.get('dabl_hamburger'),2.9))
                        item.append(order("McChicken",request.POST.get('mc_chicken'),3.7))
                        item.append(order("big_mac",request.POST.get('Big Mac'),3.95))
                        item.append(order("Big Tasty (chicken)",request.POST.get('big_tasty'),7.9))
                        item.append(order("Big Tasty (meat)",request.POST.get('big_tasty_meat'),8.2))
                        item.append(order("Water",request.POST.get('Water'),1.0))
                        item.append(order("Sprite",request.POST.get('sprite'),2.0))
                        item.append(order("Orange Juice",request.POST.get('orange_juice'),4.2))
                        item.append(order("Lemonade",request.POST.get('lemonade'),5.6))
                        item.append(order("Chai Chiller",request.POST.get('chai_chiller'),6.5))
                        item.append(order("Affagato Magnum",request.POST.get('affagato_magnum'),7.4))
                        item.append(order("Tonic Americano",request.POST.get('tonic_americano'),7.7))
                        item.append(order("Simple Tea",request.POST.get('simple_tea'),4.0))
                        item.append(order("Spicy Tea",request.POST.get('spicy_tea'),4.9))
                        item.append(order("Fruity Tea",request.POST.get('fruity_tea'),4.9))
                        item.append(order("Peach Tea",request.POST.get('peach_tea'),4.9))
                        item.append(order("Cherry Tea",request.POST.get('cherry_tea'),4.9))
                        item.append(order("Green Tea",request.POST.get('green_tea'),4.9))
                        item.append(order("Lilac Tea",request.POST.get('lilac_tea'),5.5))
                        item.append(order("Espresso",request.POST.get('espresso'),2.5))
                        item.append(order("Americano",request.POST.get('americano'),3.5))
                        item.append(order("Turkish Coffee",request.POST.get('turkish_coffee'),3.5))
                        item.append(order("Cappuccino",request.POST.get('cappuccino'),4.9))
                        item.append(order("Cafe Mocha",request.POST.get('cage_mocha'),5.5))
                        item.append(order("Cafe Raf",request.POST.get('cafe_raf'),5.5))
                        item.append(order("Chocolate Latte",request.POST.get('chocolate_latte'),6.0))
                        item.append(order("Honey Cake",request.POST.get('hone_cake'),5.0))
                        item.append(order("Chocolate with milk",request.POST.get('chocolate_milk'),5.5))
                        item.append(order("Tiramisu",request.POST.get('tiramisu'),5.0))
                        item.append(order("Melted Chocolate",request.POST.get('melted_chocolate'),5.5))
                        item.append(order("Profitrol",request.POST.get('profitrol'),6.0))
                        item.append(order("Lemon Cheesecake",request.POST.get('lemon_cheesecake'),6.0))
                        item.append(order("Chocolate Cheesecake",request.POST.get('chocolate_cheesecake'),7.5))
                        result = {
                                "msg" : "Please choose a product"
                        }
                        for i in item:
                                if i.count and int(i.count)>0:
                                        test = 1
                                        post=Order()
                                        post.namelastname= name
                                        post.address= address
                                        post.phone= phone
                                        post.itemname= i.name
                                        post.total_view= i.price *  int(i.count) 
                                        post.say=int(i.count)
                                        post.save() 

                                        result = {
                                                "msg" : "Your order is successful",
                                        }
                else:
                        result = {
                                "msg" : "Please enter your name, lastname, and address correctly"
                        }
                if test==1:
                        return render(request, 'success.html',result)  
                else:
                        return render(request, 'error.html',result)  