class Vehicle:
    def __init__(self, colour: str, weight: int, max_speed: int, max_range: int = None, seats: int = None):
        """
        This is the base class for all vehicles.
        
        Parameters:
        - colour: the colour of the vehicle
        - weight: the weight of the vehicle in kg
        - max_speed: the top speed in km/h
        - max_range: how far the vehicle can go without stopping.
        - seats: number of seats in the vehicle
        """
        self.colour = colour
        self.weight = weight
        self.max_speed = max_speed
        self.max_range = max_range
        self.seats = seats

    def move(self, speed: int) -> None:
        """Prints how fast the vehicle is moving."""
        print(f"The vehicle is moving at {speed} km/h")


class Car(Vehicle):
    def __init__(self, colour: str, weight: int, max_speed: int, form_factor: str, **kwargs):
        """
        A class for cars that inherits from Vehicle.

        Parameters:
        - form_factor: e.g. 'SUV', 'Hatchback'
        - kwargs: other keyword arguments passed to the Vehicle class
        """
        super().__init__(colour, weight, max_speed, **kwargs)
        self.form_factor = form_factor

    def move(self, speed: int) -> None:
        """Prints how fast the car is driving."""
        print(f"The car is driving at {speed} km/h")


class Electric(Car):
    def __init__(self, colour: str, weight: int, max_speed: int, form_factor: str, battery_capacity: int, max_range: int = None, **kwargs):
        """
        An electric car class that inherits from Car.

        Parameters:
        - battery_capacity: size of the battery
        - max_range:  maximum driving range
        - kwargs: other keyword arguments passed to parent class
        """
        super().__init__(colour, weight, max_speed, form_factor, max_range=max_range, **kwargs)
        self.battery_capacity = battery_capacity

    def move(self, speed: int) -> None:
        """Prints how fast the electric car is driving and its range."""
        print(f"The electric car is driving at {speed} km/h and has a maximum range of {self.max_range} km\n")


class Petrol(Car):
    def __init__(self, colour: str, weight: int, max_speed: int, form_factor: str, fuel_capacity: int, max_range: int = None, **kwargs):
        """
        A petrol car class that inherits from Car.

        Parameters:
        - fuel_capacity: size of the fuel tank
        - max_range: maximum driving range
        - kwargs: other keyword arguments passed to parent class
        """
        super().__init__(colour, weight, max_speed, form_factor, max_range=max_range, **kwargs)
        self.fuel_capacity = fuel_capacity

    def move(self, speed: int) -> None:
        """Prints how fast the petrol car is driving and its range."""
        print(f"The petrol car is driving at {speed} km/h and has a maximum range of {self.max_range} km\n")


class Plane(Vehicle):
    def __init__(self, colour: str, weight: int, max_speed: int, wingspan: float, **kwargs):
        """
        A class for planes that inherits from Vehicle.

        Parameters:
        - wingspan: the width of the wings
        - kwargs: other keyword arguments passed to parent class
        """
        super().__init__(colour, weight, max_speed, **kwargs)
        self.wingspan = wingspan

    def move(self, speed: int) -> None:
        """Prints how fast the plane is flying."""
        print(f"The plane is flying at {speed} km/h")


class Propeller(Plane):
    def __init__(self, colour: str, weight: int, max_speed: int, wingspan: float, propeller_diameter: float, **kwargs):
        """
        A propeller plane class that inherits from Plane.

        Parameters:
        - propeller_diameter: the size of the propeller
        - kwargs: other keyword arguments passed to parent class
        """
        super().__init__(colour, weight, max_speed, wingspan, **kwargs)
        self.propeller_diameter = propeller_diameter

    def move(self, speed: int) -> None:
        """Prints how fast the propeller plane is flying."""
        print(f"The propeller plane is flying at {speed} km/h")


class Jet(Plane):
    def __init__(self, colour: str, weight: int, max_speed: int, wingspan: float, engine_thrust: int, **kwargs):
        """
        A jet plane class that inherits from Plane.

        Parameters:
        - engine_thrust: the power of the jet engine
        - kwargs: other keyword arguments passed to parent class
        """
        super().__init__(colour, weight, max_speed, wingspan, **kwargs)
        self.engine_thrust = engine_thrust

    def move(self, speed: int) -> None:
        """Prints how fast the jet is flying."""
        print(f"The jet is flying at {speed} km/h")


class FlyingCar(Car, Plane):
    def __init__(self, colour: str, weight: int, max_speed: int, form_factor: str, wingspan: float, **kwargs):
        """
        A flying car that inherits from both Car and Plane.

        Parameters:
        - form_factor: e.g. 'SUV'
        - wingspan: width of the wings
        - kwargs: other keyword arguments passed to both parent classes
        """
        # Pass wingspan to Plane through kwargs
        super().__init__(colour, weight, max_speed, form_factor=form_factor, wingspan=wingspan, **kwargs)

    def move(self, speed: int) -> None:
        """Prints how fast the flying car is flying or driving."""
        print(f"The flying car is driving or flying at {speed} km/h")


# Creating and test objects
# Vehicle object
vehicle = Vehicle("red", 1000, 200, max_range=500, seats=5)
vehicle.move(100)

# Car object
car_vehicle = Car("red", 1000, 200, "SUV", max_range=500, seats=5)
car_vehicle.move(100)

# Electric car object
generic_electric_car = Electric("red", 1000, 200, "SUV", battery_capacity=100, max_range=500, seats=5)
generic_electric_car.move(100)

# Petrol car object
generic_petrol_car = Petrol("red", 1000, 200, "SUV", fuel_capacity=100, max_range=500, seats=5)
generic_petrol_car.move(100)

# Plane object
plane_vehicle = Plane("white", 3000, 400, wingspan=20, max_range=800, seats=2)
plane_vehicle.move(250)

# Propeller plane object
propeller_plane = Propeller("white", 3000, 400, wingspan=20, propeller_diameter=3.5, max_range=800, seats=2)
propeller_plane.move(250)

# Jet plane object
jet_plane = Jet("gray", 5000, 900, wingspan=35, engine_thrust=15000, max_range=1200, seats=4)
jet_plane.move(750)

# generic_flying_car object
generic_flying_car = FlyingCar("red", 1000, 200, "SUV", 30, seats=5)
generic_flying_car.move(100)

print(generic_flying_car.seats, generic_flying_car.wingspan, generic_flying_car.form_factor)
