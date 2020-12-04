from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Fournisseur, Produit, Order, MergedOrder, OrderItems
from .forms import FournisseurForm, ProduitForm, OrderForm, MergedOrderForm, OrderItemsForm
from django.urls import reverse
# Create your views here.


def back_office(request):
    return render(request, 'stock_management/base.html')


def list_articles(request):
    current_page = 'articles'
    produits = Produit.objects.all()
    return render(request, 'stock_management/list.html', {'list_produits': produits, 'current_page': current_page})


def add_article(request):
    form = ProduitForm(request.POST, request.FILES)
    if form.is_valid():
        # form.image = form.cleaned_data['image']
        form.save()
        return HttpResponseRedirect(reverse('list_articles'))

    return render(request, 'stock_management/add_article.html', locals())


def modify_article(request, pk):
    obj = get_object_or_404(Produit, pk=pk)
    form_send = False
    if request.method == 'POST':
        form = ProduitForm(request.POST)

        if form.is_valid():
            new_name = form.cleaned_data['name']
            new_price = form.cleaned_data['selling_gross_price']
            old_name = obj.name
            obj.name = new_name
            obj.selling_gross_price = new_price
            obj.save()
            envoi = True
            form_send = True
            return HttpResponseRedirect(reverse('list_articles'))
        elif not form.is_valid():
            print(form.errors)
    else:

        form = ProduitForm(initial={'name': obj.name, 'selling_gross_price': obj.selling_gross_price})

    return render(request, 'stock_management/modify_article.html', locals())


def delete_article(request, pk):
    obj = get_object_or_404(Produit, pk=pk)
    obj.delete()
    return HttpResponseRedirect(reverse('list_articles'))
    # return render(request,'stock_management/list.html',locals())


def list_supplier(request):
    current_page = 'page_fournisseurs'
    fournisseurs = Fournisseur.objects.all()
    return render(request, 'stock_management/supplier.html',
                  {'tous_les_fournisseurs': fournisseurs, 'current_page': current_page})


def add_supplier(request):
    form = FournisseurForm(request.POST)
    form_send = False
    if form.is_valid():
        form_send = True
        form.save()
        return HttpResponseRedirect(reverse('list_supplier'))
    else:
        form = FournisseurForm()
        return render(request, 'stock_management/add_supplier.html', locals())


def modify_supplier(request, pk):
    obj = get_object_or_404(Fournisseur, pk=pk)
    form_send = False
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            old_name = obj.name
            obj.name = new_name
            obj.save()
            envoi = True
            form_send = True
            return HttpResponseRedirect(reverse('list_supplier'))
    else:
        form = FournisseurForm(initial={'name': obj.name})

    return render(request, 'stock_management/modify_supplier.html', locals())


def delete_supplier(request, pk):
    obj = get_object_or_404(Fournisseur, pk=pk)
    obj.delete()
    return HttpResponseRedirect(reverse('list_supplier'))


def list_order(request):
    current_page = 'commandes'
    orders = Order.objects.all()

    merged_orders = MergedOrder.objects.all()
    order_items = OrderItems.objects.all()
    return render(request, 'stock_management/order.html',
        {'list_orders': orders, 'list_merged_orders': merged_orders, 'list_order_items':order_items,
         'current_page': current_page})


def add_items_to_order(request, pk):
    obj = get_object_or_404(Order, pk=pk)

    form = OrderItemsForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list_order'))
    else:
        return render(request, 'stock_management/order_items.html', locals())


def create_order(request):
    form = OrderForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()
        obj = Order.objects.latest("pk")

        return HttpResponseRedirect(reverse('add_items_to_order', kwargs={'pk': obj.primary_key}))
    return render(request, 'stock_management/create_order.html', locals())


def modify_order(request, pk):
    obj = get_object_or_404(Order, pk=pk)
    products = Produit.objects.all()

    form_send = False
    # print(request.POST.get("add_item_1"))
    form = OrderForm(data=request.POST, instance=obj)
    if request.method == 'POST':
        if form.is_valid():

            for key, value in request.POST.items():
                if key.startswith('add_item'):
                    produit = Produit.objects.get(primary_key=value)
                    item = OrderItems(order=obj, product=produit)
                    item.save()
            form.save()
            form_send = True
            return HttpResponseRedirect(reverse('list_order'))
    else:
        form = OrderForm(instance=obj)

    return render(request, 'stock_management/modify_order.html', locals())


def delete_order(request, pk):
    obj = get_object_or_404(Order, pk=pk)
    obj.delete()
    return HttpResponseRedirect(reverse('list_order'))


def delete_order_items(request, pk):
    obj = get_object_or_404(OrderItems, pk=pk)
    obj.delete()
    return HttpResponseRedirect(reverse('list_order'))


def merge_order(request):
    form = MergedOrderForm(request.POST, request.FILES)
    orders = Order.objects.all()
    results = MergedOrder.objects.all()

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list_order'))

    return render(request, 'stock_management/merge_order.html', locals())


def delete_merged_order(request, pk):
    obj = get_object_or_404(MergedOrder, pk=pk)
    obj.delete()
    return HttpResponseRedirect(reverse('list_order'))


def modify_merged_order(request, pk):
    obj = get_object_or_404(MergedOrder, pk=pk)
    form_send = False
    if request.method == 'POST':
        form = MergedOrderForm(request.POST)
        if form.is_valid():
            new_id = form.cleaned_data['identifier']
            old_id = obj.identifier
            obj.identifier = new_id

            new_date = form.cleaned_data['date']
            old_date = obj.date
            obj.date = new_date

            new_order = form.cleaned_data['order']
            old_order = obj.order
            obj.order = new_order

            obj.save()
            envoi = True
            form_send = True
            return HttpResponseRedirect(reverse('list_order'))
    else:
        form = MergedOrderForm(
            initial={'identifier': obj.identifier, 'date': obj.date, 'order': obj.order})

    return render(request, 'stock_management/modify_merged_order.html', locals())
