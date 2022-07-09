from django.contrib import admin
from .models import Account, Transaction, BankLoan, MobileLoan, MobilePayment, BankPayment
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name = 'Accounts'


class CustomAdmin (UserAdmin):
    inlines = (AccountInline,)


admin.site.unregister(User)
admin.site.register(User, CustomAdmin)


admin.site.register(Transaction)
admin.site.register(BankLoan)
admin.site.register(MobileLoan)
admin.site.register(BankPayment)
admin.site.register(MobilePayment)