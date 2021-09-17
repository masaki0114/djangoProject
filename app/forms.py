from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
	"""docstring for ItemForm"""
	class Meta:
		"""docstring for Meta"""
		model = Item
		fields = ('name', 'age', 'sex', 'memo')
		widgets = {
			'name': forms.TextInput(attrs={'placeholder':'記入例：山田太郎'})
			,'age': forms.NumberInput(attrs={'min':1})			
			,'sex': forms.RadioSelect()
			,'memo': forms.Textarea(attrs={'rows':4})
		}