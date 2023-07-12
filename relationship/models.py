from django.db import models

# Create your models here.

class Person(models.Model): # person_object.aadhar  # in case related_name is provied, person_object.aadhar_num 
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    mobile = models.BigIntegerField(null=True, unique=True)
    is_active = models.BooleanField(default=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "person"

class Aadhar(models.Model): # aadhar_object.person
    aadhar_number = models.BigIntegerField(unique=True)
    address = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now=True)
    DOB = models.DateField()
    person = models.OneToOneField(Person, on_delete=models.CASCADE, null=True, related_name="aadhar_num")  # Person Class--in table, person_id
    is_active = models.BooleanField(default=True)
    

    def __str__(self):
        return str(self.aadhar_number)

    class Meta:
        db_table = "aadhar"

# is_active
# created_date
# updated_date
# created_by
# update_by

class Car(models.Model): # car_object.carmodel_set.all(),  in case related_name provided, car_object.carmodels.all()
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "car"


class CarModel(models.Model): # carmodel_object.car
    name = models.CharField(max_length=255)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, related_name="carmodels") # 
    
    def __str__(self):
        return self.name


    class Meta:
        db_table = "car_model"
# ----------------------------------------------------------------------------------

class FuelType(models.Model): # fueltype_object.cmodel_set.all(), in case related_name provided - fueltype_object.cmodels.all()
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "fuel_type"

class CModel(models.Model): # cmodel_object.fueltype.all()
    name = models.CharField(max_length=255)
    fueltype = models.ManyToManyField(FuelType, related_name="cmodels") # id(pk), fueltype_id(fk), cmodel_id(fk)
    def __str__(self):
        return self.name
    
# ERD -- Entity Relationship Digram
# composite key

# # substitute for ManyToManyField
# class CModel_Fueltype(models.Model):# id(pk), cmodel_id(fk), fueltype(fk), extra_field
#     cmodel = models.ForeignKey(CModel, on_delete=models.SET_NULL, null=True)
#     fueltype = models.ForeignKey(FuelType, on_delete=models.SET_NULL, null=True)
#     extra_field = models.CharField(max_length=200)

#     class Meta:
#         unique_together = (('cmodel', 'fueltype'),) # composite key

# id, fuletype_id, cmodel_id, extra_field



# print("in master branch")

# print("changes done by mohini")
# print("in f1 branch")
