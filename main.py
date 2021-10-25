from Vehicle import Car
from Vehicle import Pickup

# SET HARDCODES OPTIONS TO CHOOSE FROM
def optionsPicker():
    startingOptions = [
        "Leather Seats", 
        "Cruise Control", 
        "Heated Seats", 
        "Remote Starter",
        "Satellite Radio",
        "Manual Transmission",
        "Air Conditioning",
        "Power Seats",
        "Power Door Locks",
        "Power Sunroof"]
    chosenOptions = []

    # KEEP PROMPTING MENU WHILE keepPrompt IS TRUE
    keepPrompt = True 
    while keepPrompt:
        print("\nSelect the number of an option to add it to your build, -1 to remove an already added option, or -2 to finish selecting options")
        for i in (range(len(startingOptions))):
            print(f'\t{i} - {startingOptions[i]}')
        selection = input("Selection: ")
        try:
            selectedInt = int(selection)
            if selectedInt not in range(-2, len(startingOptions)):
                raise ValueError
            if selectedInt == -1 and len(chosenOptions) > 0:
                print("\nSelect the number of an option to remove from your vehicle: ")
                for x in (range(len(chosenOptions))):
                    print(f'\t{x} - {chosenOptions[x]}')
                removeSelection = input("Selection: ")
                try:
                    removeSelectionInt = int(removeSelection)
                    if removeSelectionInt not in range(len(chosenOptions)):
                        raise ValueError
                    startingOptions.append(chosenOptions.pop(removeSelectionInt))
                except ValueError:
                    print("Selection made is not value. Trye again.\n")
            elif selectedInt == -1 and len(chosenOptions) == 0:
                print("You don't have any selected options to remove.\n")
            elif selectedInt == -2:
                keepPrompt = False
            else:
                chosenOptions.append(startingOptions.pop(selectedInt))
        except ValueError:
            print("Selection made is not valid. Try again\n")
    return chosenOptions

def displayGarage(garage):
    if len(garage) > 0:
        print("Wow! Nice garage!")
    else:
        print("Not everybody needs a vehicle.")
    vehicleCount = 1
    for vehicle in garage:
        objConfig = vars(vehicle)
        print(f'\nVehicle {vehicleCount}\n')
        for key, value in objConfig.items():
            print(f'\t{key.title()}: {value}')
        vehicleCount += 1


def buildCar():
    print("Awesome! Let's build your car!")
    make = ""
    model = ""
    color = ""
    fuelType = ""
    engineSize = ""
    numDoors = ""

    while make == "":
        make = input("Enter the make: ")
        if make == "":
            print("No make was entered. Please enter a make name for this car.")
    
    while model == "":
        model = input("Enter the model: ")
        if model == "":
            print("No model was entered. Please enter a model name for this car.")
    
    while color == "":
        color = input("Enter the color: ")
        if color == "":
            print("No color was entered. Please enter a color for this car.")

    while fuelType == "":
        fuelType = input("Enter the fuel type: ")
        if fuelType == "":
            print("No fuelType was entered. Please enter a fuel type for this car.")
    
    while engineSize == "":
        engineSize = input("Enter the engine size: ")
        if engineSize == "":
            print("No engine size was entered. Please enter an engine size for this car.")
    
    while numDoors == "":
        numDoors = input("Enter number of doors: ")
        if numDoors == "":
            print("No door count was entered. Please enter the number of doors for this car.")
    options = optionsPicker()
    return Car(make, model, color, fuelType, options, engineSize, numDoors)

def buildPickup():
    print("Awesome! Let's build your pickup!")

    make = ""
    model = ""
    color = ""
    fuelType = ""
    cabStyle = ""
    bedLength = ""

    while make == "":
        make = input("Enter the make: ")
        if make == "":
            print("No make was entered. Please enter a make name for this pickup.")
    
    while model == "":
        model = input("Enter the model: ")
        if model == "":
            print("No model was entered. Please enter a model name for this pickup.")
    
    while color == "":
        color = input("Enter the color: ")
        if color == "":
            print("No color was entered. Please enter a color for this pickup.")
    
    while fuelType == "":
        fuelType = input("Enter the fuel type: ")
        if fuelType == "":
            print("No fuelType was entered. Please enter a fuel type for this pickup.")
    
    while cabStyle == "":
        cabStyle = input("Enter the cab style: ")
        if cabStyle == "":
            print("No cab style was entered. Please enter the cab style for this pickup")
        
    while bedLength == "":
        bedLength = input("Enter the bed length: ")
        if bedLength == "":
            print("No bed length was entered. Please enter a bed length for this pickup.")
    options = optionsPicker()
    return Pickup(make, model, color, fuelType, options, cabStyle, bedLength)

# CREATE EMPY LIST TO STORE CARS AND PICKUPS
garage = []
# KEEP DISPLAYING MENU WHILE displayMenu IS TRUE
displayMenu = True
while displayMenu:
    print("\nMake a selection by choosing the letter of the coresponding action:\n\tC - Create a new Car\n\tP - Create a new Pickup\n\tE - Exit and View Your Garage")
    choice = input("Selection: ")
    if choice.upper() == 'C':
        garage.append(buildCar())
    elif choice.upper() == 'P':
        garage.append(buildPickup())
    elif choice.upper() == 'E':
        displayMenu = False
    else:
        print("You did not enter a valid option. Try again.")

# DISPLAY ALL VEHICLES CREATED ONE USER INDICATES THEY'RE DONE CREATING VEHICLES
displayGarage(garage)