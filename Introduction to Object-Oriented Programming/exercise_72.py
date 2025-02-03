# Exercise 72: Demonstrate updating a class attribute via an instance.
class Planet:
orbit = "elliptical"

earth = Planet()
# Although not recommended, you can update a class attribute via an instance:
earth.orbit = "circular"
print("Earth orbit (instance):", earth.orbit)
print("Planet orbit (class):", Planet.orbit)
