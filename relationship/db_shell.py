# exec(open(r"E:\Python-B9\Files\DjangoProjects\B9_Library\relationship\db_shell.py").read())


from relationship.models import *


# Person.objects.create(name="CCC", age=27, mobile=7561478799, email="ccc@gmail.com")


# all = Person.objects.all()
# print(list(all))


# p3 = Person.objects.get(id=3) # CCC
# print(p1)
# from django.utils import timezone
# from datetime import date


# code optimization -- to reduce time -- 

#1
# Aadhar.objects.create(aadhar_number=451247895623, address="Pune", DOB=date(1995, 7, 25), person=p1) # person instance
#2
# Aadhar.objects.create(aadhar_number=561478956121, address="Mumbai", DOB=date(1997, 8, 25), person_id=2) # person id

# a1 = Aadhar(aadhar_number=514789562658, address="Banglore", DOB=date(1994, 8, 31))
# a1.save()

# a3 = Aadhar.objects.get(aadhar_number=514789562658)
# print(a3.person) # Person.objects.get(aadhar=a3)
# print(a3)

# select_related
# import time

# t1 = time.time()
# a3 = Aadhar.objects.select_related("person").get(aadhar_number=514789562658)
# print(a3.person)
# t2 = time.time()
# print(t2-t1)


# t1 = time.time()
# a3 = Aadhar.objects.get(aadhar_number=514789562658)
# print(a3.person)
# t2 = time.time()
# print(t2-t1)


# t1 = time.time()
# for i in Aadhar.objects.all().select_related("person"):
#     print(i.person)
# t2 = time.time()
# print(t2 - t1)

#3


# for p in Person.objects.all().select_related("aadhar_num"):
#     print(p.aadhar_num)

# a3.person = p3
# a3.save()


# aadhar se person fetch
# a3 = Aadhar.objects.get(id=1)
# print(a3.person.__dict__)

# person_id -- 


# person se aadhar fetch
# p1 = Person.objects.get(id=1)
# print(p1.aadhar)
# print(p1.aadhar.address)
# print(p1.aadhar.__dict__)





# select related


# from relationship.models import Car, CarModel
# mercedes = Car.objects.create(name="Mercedes")
# bmw = Car.objects.create(name="BMW")

# data = Car.objects.all()
# print(data)

# mercedes = Car.objects.get(name="Mercedes")
# c180 = CarModel.objects.create(name="C180", car=mercedes)


# carmodel se car fetch
# c180 = CarModel.objects.get(name="C180")
# print(c180.car.__dict__)

# car se carmodel fetch  -- multiple records

# c1 = Car.objects.get(name="Mercedes")
# print(c1.carmodels.all()) # QuerySet -- multiple

# print(c1.carmodel_set.all()) # in case no related name

# mercedes = Car.objects.get(name="Mercedes")

# c200 = CarModel.objects.create(name="C200")
# c200 = CarModel.objects.get(name="C200")
# c200.car = mercedes
# c200.save()


# print(c200.car.name)



# x1 = CarModel.objects.create(name="X1")
# x3 = CarModel.objects.create(name="X3")

# for car_models in CarModel.objects.all():
#     print(car_models.car)

# x1, x3 = CarModel.objects.filter(name__in=["X1", "X3"])


# bmw = Car.objects.get(name="BMW")
# bmw.carmodels.add(x1, x3)

# model = CarModel.objects.filter(car__name__in=["BMW", "Mercedes"])
# print(model)


# mercedes = Car.objects.get(name="Mercedes")

# mercedes.carmodels.clear()
# cm = CarModel.objects.get(id=1)
# mercedes.carmodels.remove(cm)
# print(mercedes.carmodels.all())


# Car.objects.get(name="BMW").delete()



# many to many example

from relationship.models import *

# c180 = CModel.objects.create(name="C180")
# c200 = CModel.objects.create(name="C200")

# CarModel.objects.all()


# gas = FuelType.objects.create(name="Gas")
# diesel = FuelType.objects.create(name="Diesel")
# hybrid = FuelType.objects.create(name="Hybrid")
# FuelType.objects.all()


# c180 = CModel.objects.get(name="c180")
# # print(c180)

# diesel = FuelType.objects.get(name="Diesel")
gas = FuelType.objects.get(name="Gas")
# hyb = FuelType.objects.get(name="Hybrid")


# c180.fueltype.add(diesel, gas)
# # print(c180.fueltype.all())
# c200 = CModel.objects.get(name="c200")

# c200.fueltype.add(gas, diesel, hyb)

# print(c200.fueltype.all())
# c200.fueltype.create(name="Bio Diesel") # create a fueltype and assign to car model


# print(gas.cmodel_set.all())
# FuelType.objects.get(name="Gas").carmodel_set.all()

# print(gas.cmodels.all())

# all = CModel.objects.filter(fueltype__name__startswith="B")
# print(all.query)

# c180 = CModel.objects.get(name="c180")

# c180.fueltype.clear()


# c180.fueltype.set([diesel, gas])