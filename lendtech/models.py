import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username
    


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    info = models.CharField(max_length=600, null=False)
    unique_identifier = models.BigIntegerField()
    amount = models.BigIntegerField()
    type = models.CharField(
        max_length=300,
        choices=[('BANK', 'BANK'),('MOBILE', 'MOBILE')]
        )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.info




class BankLoan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bank_name = models.CharField(max_length=500, null=False)
    bank_account_number = models.BigIntegerField( null=False)
    amount = models.BigIntegerField(null=False)
    branch = models.CharField(max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    # transaction = Transaction.objects.create(
    # account = self.account,
    # info = self.bank_name,
    # unique_identifier = self.bank_account_number,
    # type = "BANK",
    # amount = self.amount,
    #     )
    # transaction.save()
    def __str__(self):
        return self.bank_name




class MobileLoan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fname = models.CharField(max_length=300, null=False)
    lname = models.CharField(max_length=300, null=False)
    phone_number = models.BigIntegerField( null=False)
    amount = models.BigIntegerField(null=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.fname } {self.lname } - {self.phone_number}"



class BankPayment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payment =  models.ForeignKey(BankLoan, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    amount = models.BigIntegerField(null=False)
    type = models.CharField(max_length=256, null=False, default='BANK')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.type}-{self.amount}"




class MobilePayment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payment =  models.ForeignKey(MobileLoan, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    amount = models.BigIntegerField(null=False)
    type = models.CharField(max_length=256, null=False, default='MOBILE')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.type}-{self.amount}"




# Form model

class FormModel(models.Model):
    date = models.DateField()