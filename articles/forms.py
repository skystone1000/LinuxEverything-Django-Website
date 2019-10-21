from django import forms 
from . import models
# "from ." means from the current directoy we import models

class CreateArticle(forms.ModelForm):
	class Meta:
		model = models.Article
		fields = ['title','body','slug','thumb']