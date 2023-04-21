from django.contrib import admin

from .models import bookview,  UsrBookReqOrdersLogs, RequestBook, UserProfile
#LibUserCreation
#BookUniqueSlug,

# Register your models here.

admin.site.register(bookview)
#admin.site.register(LibUserCreation)
#admin.site.register(BookUniqueSlug)
admin.site.register(UsrBookReqOrdersLogs)
admin.site.register(RequestBook)
admin.site.register(UserProfile)