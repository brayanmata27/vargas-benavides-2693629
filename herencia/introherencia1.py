class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TracketVehicle(LandVehicle):
    pass 

#print(issubclass(TracketVehicle(LandVehicle,Vehicle)))
v=Vehicle
Lv=LandVehicle
Tv=TracketVehicle



for cls1 in[Vehicle,LandVehicle,TracketVehicle]:
    for cls2 in[Vehicle,LandVehicle,TracketVehicle]:
        print(issubclass(cls1,cls2),end="\t")
    print()
