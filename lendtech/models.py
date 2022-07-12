from operator import pos
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    catergory = models.CharField(
        max_length=300,
        choices=[('PAYMENT', 'PAYMENT'),('LOAN', 'LOAN')],
        null=True
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




# Signals
# Loans

@receiver(post_save, sender=BankLoan)
def transaction_creation_handler(*args, **kwargs):
    
    if kwargs['created']:
            transaction = Transaction.objects.create(
            info = kwargs['instance'].bank_name,
            unique_identifier = kwargs['instance'].bank_account_number,
            type = "BANK",
            amount = kwargs['instance'].amount,
            user = kwargs['instance'].user,
            catergory = 'LOAN',
                )
            transaction.save()
            print(f"{kwargs['instance']} transaction successfully created...")
#post_save.connect(transaction_creation_handler, sender=BankLoan)



@receiver(post_save, sender=MobileLoan)
def transaction_creation_handler(*args, **kwargs):

    if kwargs['created']:
            transaction = Transaction.objects.create(
            info = f"{kwargs['instance'].fname} {kwargs['instance'].lname}",
            unique_identifier = kwargs['instance'].phone_number,
            type = "MOBILE",
            amount = kwargs['instance'].amount,
            user = kwargs['instance'].user,
            catergory = 'LOAN',
                )
            transaction.save()

            print(f"{kwargs['instance']} transaction successfully created...")
#post_save.connect(transaction_creation_handler, sender=MobileLoan)



# Signals 
# Payments

@receiver(post_save, sender=BankPayment)
def transaction_creation_handler(*args, **kwargs):

    if kwargs['created']:
            transaction = Transaction.objects.create(
            info = kwargs['instance'].payment.bank_name,
            unique_identifier = kwargs['instance'].payment.bank_account_number,
            type = "BANK",
            amount = kwargs['instance'].amount,
            user = kwargs['instance'].user,
            catergory = 'PAYMENT'
                )
            transaction.save()

            print(f"{kwargs['instance']} transaction successfully created...")
#post_save.connect(transaction_creation_handler, sender=BankPayment)



@receiver(post_save, sender=MobilePayment)
def transaction_creation_handler(*args, **kwargs):

    if kwargs['created']:
            transaction = Transaction.objects.create(
            info = f"{kwargs['instance'].payment.fname} {kwargs['instance'].payment.lname}",
            unique_identifier = kwargs['instance'].payment.phone_number,
            type = "MOBILE",
            amount = kwargs['instance'].amount,
            user = kwargs['instance'].user,
            catergory = 'PAYMENT',
                )
            transaction.save()

            print(f"{kwargs['instance']} transaction successfully created...")
#post_save.connect(transaction_creation_handler, sender=MobilePayment)
