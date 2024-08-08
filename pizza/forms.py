from django import forms
from .models import Pizza

# Django Forms
# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label = 'topping1', max_length = 100)
#     topping2 = forms.CharField(label = 'topping2', max_length = 100)
#     size = forms.ChoiceField(label = 'size',choices = [('Small','Small'), ('Medium','Medium'), ('Large','Large')])
    
#Working with Widgets
# class PizzaForm(forms.Form):
#     toppings = forms.MultipleChoiceField(choices=[('pep','Pepperoni'), ('cheese','Cheese'), ('olives','Olives')], widget=forms.CheckboxSelectMultiple)
#     size = forms.ChoiceField(label = 'size',choices = [('Small','Small'), ('Medium','Medium'), ('Large','Large')])

#From Django ModelForms
class PizzaForm(forms.ModelForm):
    class Meta:
            model = Pizza
            fields = ['topping1', 'topping2', 'size']
            labels = {
            "topping1": "Topping 1",
            "topping2": "Topping 2",
            }

#Working with Widgets From Django ModelForms          
# class PizzaForm(forms.ModelForm):

#     size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.RadioSelect)

#     class Meta:
#             model = Pizza
#             fields = ['topping1', 'topping2', 'size']
            
class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)