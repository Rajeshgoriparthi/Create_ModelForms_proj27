from django import forms

g=[['Mala','Male'],['Female','Female']]
c=[('Python','Python'),('Sql','Sql'),('Django','Django'),('Java','Java')]
class StudentForm(forms.Form):
    sno=forms.IntegerField()
    name=forms.CharField(max_length=30)
    age=forms.IntegerField()
    mail=forms.EmailField()
    date=forms.DateField()
    password=forms.CharField(max_length=50,widget=forms.PasswordInput)
    adress=forms.CharField(max_length=300,widget=forms.Textarea)
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #courses=forms.MultipleChoiceField(choices=c)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)