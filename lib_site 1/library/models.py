
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
import itertools

# Create your models here.

"""class BookUniqueSlug(models.Model):

    slug = models.SlugField(null=True, unique=True, max_length=250)
    #generates slugs and check for uniqueness of the slug
    def _generate_slug(self):
        max_length = self._meta.get_field('slug').max_length
        value = self.book_name
        slug_candidate = slug_orignal = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if bookview.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = f'{slug_orignal}-{i}'
        self.slug = slug_candidate

    #this gets invoked when the save is performed.
    def save(self, *args, **kwargs):
        if not self.pk:
            self._generate_slug()
            print("checking pk")
        super().save(*args, **kwargs)"""

class bookview(models.Model):
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    is_issueable = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    slug = models.SlugField(null=True, unique=True, blank=True)

    def __str__(self):
        return f"{self.book_name} made by {self.author_name}"

    def get_absolute_url(self):
       return reverse("library:BookForm_view.as_view()", kwargs={"slug": self.slug})
    
    def _generate_slug(self):
        max_length = self._meta.get_field('slug').max_length
        value = self.book_name
        slug_candidate = slug_orignal = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            print(i)
            if bookview.objects.filter(slug=slug_candidate).exists():
                break
            else:
                slug_candidate = f'{slug_orignal}-{i}'
                break
        self.slug = slug_candidate

    #this gets invoked when the save is performed. this is somehow not working
    def save(self, *args, **kwargs):
        #the if logic is just too different that i cannot wrap my head around.
        if self.pk is None:
           # print("checking pk")
            self._generate_slug()
        super(bookview, self).save(*args, **kwargs)
    

    
"""
class LibUserCreation(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
"""
#made userprofile
class UserProfile(models.Model):
    #pk_val_user = models.OneToOneField(get_user_model(), to_field="pk", unique=True, on_delete=models.CASCADE)
    usr_name = models.ForeignKey(get_user_model(), null=True, related_name="%(app_label)s_%(class)s_related", on_delete=models.CASCADE)
    #we don't need this because we can even so show it in the front end by using User.get_email()
    # email_of_user = models.OneToOneField(get_user_model(),to_field='email', unique=True,null=True, on_delete=models.CASCADE)
    address = models.TextField(max_length=250, blank=True)

    def __str__(self):
        return f"{self.usr_name.username} has address {self.address}"

    def check_pk(self):
        if self.pk is None:
            return True
        return False

    def address_of_user(self, pk_id):
        address = UserProfile.objects.get(pk = pk_id)
        return str(address.address)

    def usrname(self):
        """this should give us username field from the usr_name"""
        return self.usr_name.username
    
class ExtUser(User):
         
        def get_email(self, user):
            """Returns the email id this was custom added by me."""
            user_instance = User.objects.get(username=user)
            email = user_instance.email
            return email

        def get_pk_id(self, user):
            """Returns pk id of the user, function made manually"""
            user_instance = User.objects.get(username = user)
            pk_id = user_instance.pk
            return pk_id 



#orders list all
class UsrBookReqOrdersLogs(models.Model):
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)# input request.user.username here
    #models.ForeignKey( RequestBook,to_field='issue_status', related_name="%(app_label)s_%(class)s_related",on_delete=models.CASCADE)

#specific orders done by user
class RequestBook(models.Model):
    book_req = models.BooleanField(default=False)
    #have to make a foriegn key to associate with user table
    user_details = models.ForeignKey(to=UsrBookReqOrdersLogs, null=True, on_delete=models.CASCADE)
    bookname = models.CharField(max_length=100, default=None)
    author = models.CharField(max_length=100, default=None) 
    issue_status = models.BooleanField(default=True)
    date_time = models.DateTimeField( auto_now_add=True, null=True)
