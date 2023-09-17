import datetime
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

class ContactItem(models.Model):
    first_name = models.CharField(_("First Name"), max_length=30)
    last_name = models.CharField(_("Last Name"), max_length=30)
    email = models.EmailField(_("Email Address"), max_length=70, default=None)
    phone = models.CharField(_("Phone Number"), max_length=20)
    created_at = models.DateField(_("Created At"), default=datetime.date.today)
    def __str__(self):
        return f'{self.id}. | {self.last_name} | {self.first_name}'
    
class CategoryItem(models.Model):
    name = models.CharField(_("Category Name"),max_length=100)
    color_key = models.CharField(_("Hex Color Key"),max_length=20)
    created_at = models.DateField(_("Created At"), default=datetime.date.today)
    def __str__(self):
        return f'{self.id}.  | {self.name}'
     
class TaskItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(_('Description'), max_length=None)
    prio = models.IntegerField(max_length=None,default=0)
    category = models.ForeignKey(
            CategoryItem,
            related_name='Category',
            on_delete=models.CASCADE,
            default=None
    )
    assigned_users = models.ForeignKey(ContactItem,on_delete=models.CASCADE, default=None)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    created_at = models.DateField(_("Created At"), default=datetime.date.today)
    due_date = models.DateField(_("Due Date"), default=datetime.date.today)
    def __str__(self):
        return f'{self.id}. |  {self.title}  |  {self.prio}  |  {self.category.name}  |  {self.due_date}'
    
