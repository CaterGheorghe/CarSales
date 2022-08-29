from django import forms


class CarForm(forms.Form):
    BODY_TYPES = (
        ("cabriolet", "Cabriolet"),
        ("combi", "Combi"),
        ("compact_car", "Compact car"),
        ("coupe", "Coupe"),
        ("city_car", "City car"),
        ("small_car", "Small car"),
        ("minivan_car", "Minivan car"),
        ("sedan", "Sedan"),
        ("suv", "SUV"),
    )
    BRANDS = (
        ("bmw", "BMW"),
        ("volkswagen", "Volkswagen"),
        ("mercedes_benz", "Mercedes-Benz"),
        ("audi", "Audi"),
        ("ford", "Ford"),
        ("skoda", "Skoda"),
        ("renault", "Renault"),
        ("opel", "Opel"),
        ("dacia", "Dacia"),
        ("volvo", "Volvo"),
        ("honda", "Honda"),
        ("iveco", "Iveco"),
        ("kia", "Kia"),
        ("mitsubishi", "Mitsubishi"),
        ("suzuki", "Suzuki"),
        ("toyota", "Toyota"),
        ("seat", "Seat"),
        ("geep", "Geep"),
        ("porsche", "Porsche"),
        ("jaguar", "Jaguar"),
        ("pontiac", "Pontiac"),
    )
    FUELS = (
        ("gas", "Gas"),
        ("gas_cng", "Gas + CNG"),
        ("gas_gpl", "Gas + GPL"),
        ("diesel", "Diesel"),
        ("electric", "Electric"),
        ("hybrid", "Hybrid"),
        ("hydrogen", "Hydrogen"),
    )
    id = forms.IntegerField()
    body_type = forms.ChoiceField(choices=BODY_TYPES, required=True)
    brand = forms.ChoiceField(choices=BRANDS, required=True)
    model = forms.CharField(max_length=100)
    fuel = forms.ChoiceField(choices=FUELS, required=True)
    year = forms.IntegerField()
    kilometres = forms.IntegerField()
    price = forms.FloatField()


