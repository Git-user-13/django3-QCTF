from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from . models import Product
from . forms import ProductForm
from . forms import FlagForm
from . models import Flag
from . models import Board
from . forms import BoardForm
from datetime import datetime
from . models import complete
from . forms import completeForm
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.cache import cache_control, never_cache
from django.urls import reverse
from django.utils.decorators import method_decorator

@cache_control(no_cache=True, must_revalidate=True)
def func(request):
  #some code
  return

@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')

        if pass1!=pass2:
            return render(request,'signup.html',{'error':'Passwords did not match'})
        else:
            my_user=User.objects.create_user(
                uname,
                email=email,
                password=pass1,
                first_name=first_name,
                last_name=last_name)
            my_user.save()
            return redirect('login')


    return render(request,'signup.html')

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        boards = Board.objects.all()
        value = 0
        if user is not None:
            login(request,user)
            for board in boards:
                if board.user.id == user.id:
                    value = 1
            if value == 0:
                order = Board.objects.create(
                user = request.user,
                score = 0
                )
            return redirect('index')
        else:
            return render(request,'login.html',{'error':'Username or password is wrong'})
        
    return render(request,'login.html')    

def LogoutPage(request):
    logout(request)
    return redirect('index')

def IndexPage(request):
    products = Product.objects.all()[:3]

    context = {
        "products" : products
    }
    return render(request,'index.html',context)

@staff_member_required
# @cache_control(no_cache=True, must_revalidate=True,no_store=True)
def addProduct(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showProducts')
            # return redirect('addhint form.id')

        else:
            form = ProductForm()

    context = {
        "form":form
    }

    return render(request, 'addProduct.html', context)

@staff_member_required
def ShowAllProducts(request):
    products = Product.objects.all()

    context = {
        "products": products
    }

    return render(request,'showProducts.html',context)

@staff_member_required
def productDetail(request,pk):
    eachProduct = Product.objects.get(id=pk)
    hints = Flag.objects.all()


    context = {
        # "hints" : hints
        # "eachProduct" : eachProduct
    }

    contest = {
        "hints" : hints
    }

    return render(request, 'productDetail.html',{'eachProduct':Product.objects.get(id=pk),'hints':Flag.objects.all()})

@staff_member_required
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def updateProduct(request,pk):
    product = Product.objects.get(id=pk)
    
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            
            return redirect('showProducts')

    context = {
        "form":form
    }

    return render(request, 'updateProduct.html', context)

@staff_member_required
# @cache_control(no_cache=True, must_revalidate=True,no_store=True)
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('showProducts')

@staff_member_required
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def addhint(request,pk):
    from django import forms
    form = FlagForm()
    if request.method == 'POST':
        form = FlagForm(request.POST)
        if form.is_valid():
            # form.q1 = pk
            # form.save()
            # # return redirect('showProducts')
            q1 = int(pk)
            h1 = form.cleaned_data['h1']
            f1 = form.cleaned_data['f1']
            score = form.cleaned_data['score']

            order = Flag.objects.create(
                q1 = q1,
                h1 = h1,
                f1 = f1,
                score = score
            )
            return redirect('product', pk = q1)

        else:
            form = FlagForm()

    context = {
        "form":form
    }

    return render(request, 'addhint.html', context)

@staff_member_required
# @cache_control(no_cache=True, must_revalidate=True,no_store=True)
# @method_decorator(never_cache())
# @cache_control(no_store=True)
def updateHint(request,pk):
    hint = Flag.objects.get(id=pk)
    form = FlagForm(instance=hint)

    if request.method == 'POST':
        form = FlagForm(request.POST,instance=hint)
        if form.is_valid():
            form.save()
            # rendered_html = render(request, 'showProducts.html')
            # response = HttpResponse(rendered_html, content_type='text/html')
            # response['Cache-Control'] = 'no-store'
            # return response
            # response = HttpResponse( '''
            #     <script>
            #     if (window.history.replaceState) {
            #         window.history.replaceState({},document.title,"/showProducts/");
            #         }else{
            #             window.location.href = "/showProducts/";
            #         }
            #     window.location.replace("/showProducts/");
            #     </script>
            # ''')
            # return response
            # return HttpResponseRedirect('/showProducts/')
            return redirect('product', pk = hint.q1)
            # return redirect('updateHint',pk = hint.id)
            # return reverse('product', pk = hint.q1)
            # named_redirect = reverse('Welcome_page')
            # return redirect(named_redirect)

    context = {
        "form":form
    }

    return render(request, 'updateHint.html', context)

@staff_member_required
# @cache_control(no_cache=True, must_revalidate=True,no_store=True)
def deleteHint(request, pk):
    hint = Flag.objects.get(id=pk)
    var = hint.q1
    hint.delete()
    return redirect('product',pk = var)

@login_required(login_url='login')
def ShowAllQuests(request):
    products = Product.objects.all()

    context = {
        "products": products
    }

    return render(request,'showQuests.html',context)

@login_required(login_url='login')
# @cache_control(no_cache=True, must_revalidate=True,no_store=True)
def questDetail(request,pk):
    eachProduct = Product.objects.get(id=pk)
    hints = Flag.objects.all()
    completeds = complete.objects.all()


    context = {
        # "hints" : hints
        # "eachProduct" : eachProduct
    }

    contest = {
        "hints" : hints
    }

    return render(request, 'questDetail.html',{'eachProduct':Product.objects.get(id=pk),'hints':Flag.objects.all(),'completeds':complete.objects.all()})

@login_required(login_url='login')
@cache_control(no_store=True)
def addFlag(request,pk):
    hints = Flag.objects.get(id=pk)
    completeds = complete.objects.all()
    user= request.user
    boards = Board.objects.get(user=user)
    var = hints.q1
    value = '0'
    for completed in completeds:
        if hints.id == completed.hint.id:
            user = request.user
            if user.id == completed.user.id:
                value = '1'
    if request.method=='POST':
        flag=request.POST.get('flag')
        if (hints.f1 == flag):
            order = complete.objects.create(
            user = request.user,
            hint = hints,
            completed = True
            )
            mark = boards.score
            per = hints.score
            new_mark = mark + per
            Board.objects.filter(user=user).update(score=new_mark)
            return redirect('quest',pk = var)
        else:
            error = 'Flag is not correct'
            token = int(hints.q1)
            # return redirect('addFlag',pk = hints.id)
            return render(request, 'addFlag.html',{'hints':Flag.objects.get(id=pk),'completeds':complete.objects.all(),'value':value,'error':error,'token':token})

    context = {
        "hints" : hints
    }
    return render(request, 'addFlag.html',{'hints':Flag.objects.get(id=pk),'completeds':complete.objects.all(),'value':value})

@login_required(login_url='login')
def leaderboard(request):
    boards = Board.objects.all().order_by('score').reverse()

    context = {
        "boards": boards
    }

    return render(request,'Leaderboard.html',context)

@login_required(login_url='login')
def profile(request):
    user = request.user
    boards = Board.objects.all().order_by('score').reverse()
    for board in boards:
        if board.user.id == user.id:
            score = board.score 
    context = {
        "boards": boards
    }

    return render(request,'profile.html',{'score':score})

@staff_member_required
@login_required(login_url='login')
def finish(request,pk):
    completeds = complete.objects.filter(hint_id = pk)
    object = completeds.first()
    token = int(object.hint.q1)
    context = {
        "completeds": completeds
    }

    return render(request,'finish.html',{'completeds':complete.objects.filter(hint_id = pk),'token':token})