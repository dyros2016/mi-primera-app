from django import forms
from bootstrap_datepicker_plus import DateTimePickerInput
from django.forms import ValidationError
from .models import Material,Vehiculo,Chofer,Proveedor,Orden


class MaterialForm(forms.ModelForm):

    class Meta:
        model = Material
        fields = ["nombre", "medida"]

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        # validaciones
        return nombre

    def clean_medida(self):
        medida = self.cleaned_data.get("medida")
        # validaciones
        return medida
# Vehiculo
class VehiculoForm(forms.ModelForm):

    class Meta:
        model = Vehiculo
        fields = ["placa", "marca", "modelo"]

    def clean_placa(self):
        placa = self.cleaned_data.get("placa")
        # validaciones
        letras,numeros = placa.split("-")
        if not len(letras)==3:
            raise ValidationError ("La placa debe tener 3 digitos tipo letra")
        if not len(numeros)==4:
            raise ValidationError("La placa debe tener 4 digitos tipo numero")
        return placa

    def clean_marca(self):
        marca = self.cleaned_data.get("marca")
        # validaciones
        return marca

    def clean_modelo(self):
        modelo = self.cleaned_data.get("modelo")
        # validaciones
        return modelo

# Chofer
class ChoferForm(forms.ModelForm):

    class Meta:
        model = Chofer
        fields = ["nombre", "apellido", "cedula"]

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        # validaciones
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data.get("apellido")
        # validaciones
        return apellido

    def clean_cedula(self):
        cedula = self.cleaned_data.get("cedula")
        # validaciones
        if not len(cedula)==10:
            raise forms.ValidationError("La cedula debe tener 10 digitos numericos")
        return cedula



class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = ["nombre", "propietario", "direccion"]

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        # validaciones
        return nombre

    def clean_propietario(self):
        propietario = self.cleaned_data.get("propietario")
        # validaciones
        return propietario

    def clean_direccion(self):
        direccion = self.cleaned_data.get("direccion")
        # validaciones
        return direccion


class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['fecha','material','proveedor','cantidad','chofer','vehiculo','entrega','recibe']
        widgets = {
        'fecha': DateTimePickerInput(attrs={'id':'datetimepicker1'},options={
                     
                     "locale": "es",
                 }),
        #'horae': TimePickerInput(attrs={'id':'timepicker1'}),
        #'horas': TimePickerInput(attrs={'id':'timepicker2'}),
        }

    



    


