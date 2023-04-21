

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, ListView, View, FormView
from .models import ExtUser, UserProfile, UsrBookReqOrdersLogs, bookview, RequestBook
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as log
from django.contrib.auth.decorators import login_required
# Create your views here.

class LibHomeView(TemplateView):
    template_name = 'library/home.html'

def BookForm_view(request):
    """i changed it because the slug generation wasnot taking place."""
    #model = bookview
    #fields = ['book_name','author_name', 'is_issueable', 'quantity']
    #success_url = "/book_list/"
    
    if request.method == "POST":

        

        book_name = request.POST.get("book_name")
        author_name = request.POST.get("author_name")
        is_issueable = request.POST.get("is_issueable")
        quantity = request.POST.get("quantity")
        print(request.POST)
        #condition = str(bookview.objects.get(book_name))
        #book = book_name.lower()
        #validations for the form
        book = str(book_name)
        Author = str(author_name)
        
        if  bookview.objects.filter(book_name=book_name).exists():
            messages.info(request, "This book already exists")
            book_name = None
            print("filter block exe")
            return render(request, 'library/bookview_form.html')

        if author_name == "None":
            messages.info(request, "please enter author name")
            print("authornone")
            return render(request, 'library/bookview_form.html')
        if book_name == "None":
            print("booknone")
            messages.info(request, "please enter book name.")
            return render(request, 'library/bookview_form.html')

        
        bk = bookview.objects.create(book_name=book_name, author_name=author_name, is_issueable=is_issueable,quantity=quantity)
        bookview.save(self=bk)
        return redirect(reverse("library:booklist"))
    return render(request, 'library/bookview_form.html')   
        

"""need to create the request book page avaliable so that the post request could be send into the page."""



class BooksAvailable(ListView):
    model = bookview
    template_name = 'library/bookavailable_list.html'
    context_object_name = "book_objects"

#requesting books

#    def Book_Request(request):
 #       Rq = RequestBook()
  #      if request.method == 'POST':
   #         send_req = request.POST.get('book_req')
    #        Rq.objects.create(book_rq = send_req)
     #   return render(request, 'library/request_book_panel.html')


def user_profile(request):
    user = request.user.username
    check2 = User.objects.get(username=user)
    id = check2.pk
    check_ad = UserProfile.objects.get(pk = id)
    address = check_ad.address

    if request.method == "POST":
        #email can't be changed because it should be unique throughout.
        email = request.POST.get("email")
        address = request.POST.get("Address")
        user = request.user.username
        print(email,address)
        #static variables from the backend
        #add_check_var = UserProfile.usrname() 
        id_to_search = ExtUser.get_pk_id(ExtUser, user)
        orignal_email = ExtUser.get_email(ExtUser, user)
        #actual_id = id_to_search.pk
        #how do you find the field id from the user model.
        check_add = UserProfile.objects.get(pk = id_to_search)
        try:
            

            #validations
            if email == None or orignal_email == email:
                ob = User.objects.get(username=user)
                email = ob.email

                       
                if address == None or UserProfile.objects.filter(address=address).exists():
                    print(email,address, "1")
                    messages.info(request, "no changes to be made")
                    return render(request, 'library/user_profile_display.html', context={"address":address,"email":orignal_email})

                elif UserProfile.check_pk is True:
                    print(email,address, "2")
                    up = UserProfile.objects.create(address=address)
                    UserProfile.save(self=up)
                    return render(request, 'library/user_profile_display.html', context={"address":address,"email":orignal_email})

                elif check_add.address is not address:
                    print(email,address, "3")
                    #now this checks if its a new address or not
                    check_add.address = address
                    UserProfile.save(self=check_add)
                    return render(request, 'library/user_profile_display.html', context={"address":address,"email":orignal_email})
            else:
                ob = User.objects.get(username=user)
                ob.email = email
                User.save(self=ob)
                print(email,address)

                if address == None or UserProfile.objects.filter(address=address).exists():
                    print(email,address, "4")
                    messages.info(request, "no changes made.")
                    return render(request, 'library/user_profile_display.html', context={"address":address, "email":orignal_email})

                elif UserProfile.check_pk is True:
                    print(email,address, "5")
                    up = UserProfile.objects.create(address=address)
                    UserProfile.save(self=up)
                    return render(request, 'library/user_profile_display.html', context={"address":address, "email":orignal_email})

                elif check_add.address is not address:
                    print(email,address, "6")
                    #now this checks if its a new address or not
                    check_add.address = address
                    UserProfile.save(self=check_add)
                    return render(request, 'library/user_profile_display.html', context={"address":address, "email":orignal_email})

                return render(request, 'library/user_profile_display.html', context={"address":address, "email":orignal_email})

        
        except:
            print(email,address, "7")
            messages.info(request, "Email entered is already in use")
            return render(request, 'library/user_profile.html')



    return render(request, 'library/user_profile.html', context={"address":address})

def user_profile_display(request):
    """user profile display"""
    user = request.user.username
    id_to_search = ExtUser.get_pk_id(ExtUser, user)
    orignal_email = ExtUser.get_email(ExtUser, user)
    address = UserProfile.address_of_user(UserProfile, id_to_search)
    return render(request, 'library/user_profile_display.html', context={"address":address, "email":orignal_email})

"""need to make a cart page where you can see the requested books"""

def new_user_req(request):

    #forms = LibUserCreation()
    User._meta.get_field('email')._unique = True
    if request.method == 'POST':
        Username = request.POST.get('username') 
        Email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        #added email validator
        if Email == None:
            messages.info(request, 'Email is necessary!')
            return render(request, reverse('library:login'))
        
        #added email validator
        if User.objects.filter(email = Email).exists():
            messages.info(request, 'This email already exists.!')
            return render(request, reverse('library:login'))

        if password1 == password2:
                my_user = User.objects.create_user(Username, Email, password1)
                messages.info(request, 'account sucessfully made!')
                return redirect(reverse('library:homepage'))
                
        else:
            messages.info(request,"password don't match")
          
    return render(request,'library/libnewuser_view.html')

def login(request):
    if request.method == 'POST':
       
        Username = request.POST.get('username')
        password = request.POST.get('password1')
        
        user = authenticate(username = Username, password = password)
        if user is not None:
            log(request, user)
            return redirect(reverse('library:homepage'))
        else:
            messages.info(request, 'Bad credentials')
            return redirect(reverse('library:login'))        

    return render(request, 'library/login.html')

def log_out(request):
    logout(request)
    return redirect(reverse('library:login'))

# this is adding in the cart

@login_required
def add_in_books(request):
    #in time when i start using this request then i will have to make a check for address so that they can order
    instance = UsrBookReqOrdersLogs.objects.get(user=user)
    
    if RequestBook.objects.filter(user_details=instance).exists():
        req_table = RequestBook.objects.get(user_details=instance)
    else:
        return render(request, "library/request_book_panel.html", context={"bool":True})

    if request.method == "POST":
        slug = request.POST.get("slug")
        user = request.user.username 
        book = get_object_or_404(bookview, slug=slug)
       # usr_instance = UsrBookReqOrdersLogs.objects.get(user=user)
       
        
        #creation of logs
        try:
            instance = UsrBookReqOrdersLogs.objects.get(user=user)
            create_rq = RequestBook.objects.create(book_req = True, user_details = instance, bookname = book.book_name, author = book.author_name)
            RequestBook.save(self=create_rq)
            req_table = RequestBook.objects.get(user_details=instance)
            messages.info(request, "Request has been submitted, check in the request panel for info")
            return render(request,  "library/request_book_panel.html", context={"requestObject":req_table})
        except:
            messages.info(request, "An Error occured while processing the request!")
            return render(request,  "library/bookavailable_list.html")
        #else:
         #   create = UsrBookReqOrdersLogs.objects.create(user = user)
          #  UsrBookReqOrdersLogs.save(self=create)

#            usr_instance = UsrBookReqOrdersLogs.objects.get(user=user)
 #           create_rq = RequestBook.objects.create(book_req = True, user_details = usr_instance, bookname = book.book_name, author = book.author_name)
  #          RequestBook.save(self=create_rq)
   #         req_table = RequestBook.objects.get(user_details=usr_instance)
    #        messages.info(request, "Request has been submitted, check in the request panel for more info")
     #       return render(request, "library/request_book_panel.html", context={"requestObject":req_table}) 

    return render(request, "library/request_book_panel.html", context={"requestObject":req_table}) 

        

