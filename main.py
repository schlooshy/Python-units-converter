import sys

while True:

    wanttocontinue = input("Would you like to start the units converter? (y/n) : \n")
    if wanttocontinue.casefold() == "y":
        print("\n Welcome to the converter! If you would like to go back at any point, please enter 'back'.")
        while True:
            whichconverter = input("\n Which conversion would you like? \n \n For: \n"
                                   "\n TEMPERATURE \n "
                                   "\n Celcius --> Farenheit - 'C-F' "
                                   "\n Celcius --> Kelvin 'C-K' "
                                   "\n Kelvin --> Celcius - 'K-C' "
                                   "\n Kelvin --> Farenheit - 'K-F' "
                                   "\n Farenheit --> Celcius - 'F-C' "
                                   "\n Farenheit --> Kelvin - 'F-K' "
                                   "\n \n WEIGHT \n "
                                   "\n Milligrams --> Grams 'Mg-G' "
                                   "\n Grams --> Milligrams 'G-Mg' "
                                   "\n Milligrams --> Kilograms 'Mg-Kg' "
                                   "\n Kilograms --> Milligrams 'Kg-Mg' "
                                   "\n \n")
            if whichconverter == "back".casefold():
                break
# region Temperature
            if whichconverter.casefold() == "C-F".casefold():
                while True:
                    try:
                        howmanycelcius = int(input("\n How many degrees Celcius would you like to convert into Farenheit? \n "))
                        convertedcelciustofarenheit = (howmanycelcius*1.8) + 32
                        print(f"\n {howmanycelcius} degrees Celcius in Farenheit is {convertedcelciustofarenheit} degrees Farenheit!")
                        break
                    except ValueError:
                        print("Invalid Input, please enter a valid number!")

                while True:

                    wantocontinue = input("\n Would you like to convert another measurement? ('y' to convert again or any other key to exit)  : \n")
                    if wantocontinue == "y".casefold():
                        break
                    else:
                        print("Goodbye.")
                        sys.exit()


            elif whichconverter.casefold() == "F-C".casefold():
                while True:
                    try:
                        howmanyfarenheit = int(input("\n How many degrees Farenheit would you like to convert into Celcius? \n "))
                        convertedfarenheittocelcius = (howmanyfarenheit - 32)/1.8
                        print(f"\n {howmanyfarenheit} degrees Farenheit in Celcius is {convertedfarenheittocelcius} degrees Celcius!")
                        break
                    except ValueError:
                        print("Invalid Input, please enter a valid number!")

                while True:

                    wantocontinue = input("\n Would you like to convert another measurement? ('y' to convert again or any other key to exit)  : \n")
                    if wantocontinue == "y".casefold():
                        break
                    else:
                        print("Goodbye.")
                        sys.exit()

            elif whichconverter.casefold() == "K-C".casefold():
                while True:
                    try:
                        howmanykelvin = int(input("\n How many Kelvin would you like to convert into Celcius? \n "))
                        convertedkelvintocelcius = howmanykelvin - 273.15
                        print(f"\n {howmanykelvin} Kelvin in Celcius is {convertedkelvintocelcius} degrees Celcius!")
                        break
                    except ValueError:
                        print("Invalid Input, please enter a valid number!")

                while True:

                    wantocontinue = input("\n Would you like to convert another measurement? ('y' to convert again or any other key to exit)  : \n")
                    if wantocontinue == "y".casefold():
                        break
                    else:
                        print("Goodbye.")
                        sys.exit()


            elif whichconverter.casefold() == "C-K".casefold():
                while True:
                    try:
                        howmanycelciusforkelvin = int(input("\n How many degrees Celcius would you like to convert into Kelvin? \n "))
                        convertedcelciustokelvin = howmanycelciusforkelvin + 273.15
                        print(f"\n {howmanycelciusforkelvin} degrees Celcius in Kelvin is {convertedkelvintocelcius} Kelvin!")
                        break
                    except ValueError:
                        print("Invalid Input, please enter a valid number!")

                while True:

                    wantocontinue = input("\n Would you like to convert another measurement? ('y' to convert again or any other key to exit)  : \n")
                    if wantocontinue == "y".casefold():
                        break
                    else:
                        print("Goodbye.")
                        sys.exit()


            elif whichconverter.casefold() == "C-K".casefold():
                while True:
                    try:
                        howmanycelciusforkelvin = int(input("\n How many degrees Celcius would you like to convert into Kelvin? \n "))
                        convertedcelciustokelvin = howmanycelciusforkelvin + 273.15
                        print(f"\n {howmanycelciusforkelvin} degrees Celcius in Kelvin is {convertedkelvintocelcius} Kelvin!")
                        break
                    except ValueError:
                        print("Invalid Input, please enter a valid number!")

                while True:

                    wantocontinue = input("\n Would you like to convert another measurement? ('y' to convert again or any other key to exit)  : \n")
                    if wantocontinue == "y".casefold():
                        break
                    else:
                        print("Goodbye.")
                        sys.exit()


            elif whichconverter.casefold() == "F-K".casefold():
                while True:
                    try:
                        howmanyfarenheitforkelvin = int(input("\n How many degrees Farenheit would you like to convert into Kelvin? \n "))
                        convertedfarenheittokelvin = (howmanyfarenheitforkelvin + 459.67)*5/9
                        print(f"\n {howmanyfarenheitforkelvin} degrees Farenheit in Kelvin is {convertedfarenheittokelvin} Kelvin!")
                        break
                    except ValueError:
                        print("Invalid Input, please enter a valid number!")

                while True:

                    wantocontinue = input("\n Would you like to convert another measurement? ('y' to convert again or any other key to exit)  : \n")
                    if wantocontinue == "y".casefold():
                        break
                    else:
                        print("Goodbye.")
                        sys.exit()


            elif whichconverter.casefold() == "K-F".casefold():
                while True:
                    try:
                        howmanykelvinforfarenheit = int(input("\n How many Kelvin would you like to convert into Farenheit? \n "))
                        convertedkelvintofarenheit = howmanykelvinforfarenheit*1.8 - 459.67
                        print(f"\n {howmanykelvinforfarenheit} Kelvin in degrees Farenheit is {convertedkelvintofarenheit} Degrees Farenheit!")
                        break
                    except ValueError:
                        print("Invalid Input, please enter a valid number!")

                while True:

                    wantocontinue = input("\n Would you like to convert another measurement? ('y' to convert again or any other key to exit)  : \n")
                    if wantocontinue == "y".casefold():
                        break
                    else:
                        print("Goodbye.")
                        sys.exit()
# endregion

# region Weight
            elif whichconverter.casefold() == "Mg-G".casefold():
                while True:
                    try:
                        howmanymilligramstograms = int(input("\n How many milligrams would you like converted into grams? \n "))
                        convertedmilligramstograms = howmanymilligramstograms/1000
                        print(f"\n {howmanymilligramstograms} milligrams in grams is {convertedmilligramstograms} grams!")
                        break
                    except ValueError:
                        print("Invalid Input, please enter a valid number!")

                while True:

                    wantocontinue = input("\n Would you like to convert another measurement? ('y' to convert again or any other key to exit)  : \n")
                    if wantocontinue == "y".casefold():
                        break
                    else:
                        print("Goodbye.")
                        sys.exit()

            elif whichconverter.casefold() == "G-Mg".casefold():
                while True:
                    try:
                        howmanygramstomilligrams = int(input("\n How many grams would you like converted into milligrams? \n "))
                        howmanygramstomilligramsconverted = howmanygramstomilligrams*1000
                        print(f"\n {howmanygramstomilligrams} grams in milligrams is {howmanygramstomilligramsconverted} milligrams!")
                        break
                    except ValueError:
                        print("Invalid Input, please enter a valid number!")

                while True:

                    wantocontinue = input("\n Would you like to convert another measurement? ('y' to convert again or any other key to exit)  : \n")
                    if wantocontinue == "y".casefold():
                        break
                    else:
                        print("Goodbye.")
                        sys.exit()

            elif whichconverter.casefold() == "Mg-Kg".casefold():
                while True:
                    try:
                        howmanymilligramstokilograms = int(input("\n How many milligrams would you like converted into kilograms? \n "))
                        howmanymilligramstokilogramsconverted = howmanymilligramstokilograms/1000000
                        print(f"\n {howmanymilligramstokilograms} milligrams in kilograms is {howmanymilligramstokilogramsconverted} kilograms!")
                        break
                    except ValueError:
                        print("Invalid Input, please enter a valid number!")

                while True:

                    wantocontinue = input(
                        "\n Would you like to convert another measurement? ('y' to convert again or any other key to exit)  : \n")
                    if wantocontinue == "y".casefold():
                        break
                    else:
                        print("Goodbye.")
                        sys.exit()

            elif whichconverter.casefold() == "Kg-Mg".casefold():
                while True:
                    try:
                        howmanykilogramstomilligrams = int(input("\n How many kilograms would you like converted into milligrams? \n "))
                        howmanykilogramstomilligramsconverted = howmanykilogramstomilligrams*1000000
                        print(f"\n {howmanykilogramstomilligrams} kilograms in milligrams is {howmanykilogramstomilligramsconverted} milligrams!")
                        break
                    except ValueError:
                        print("Invalid Input, please enter a valid number!")

                while True:

                    wantocontinue = input(
                        "\n Would you like to convert another measurement? ('y' to convert again or any other key to exit)  : \n")
                    if wantocontinue == "y".casefold():
                        break
                    else:
                        print("Goodbye.")
                        sys.exit()










            elif whichconverter.casefold() == "back":
                break




    elif wanttocontinue.casefold() == "n":
        print("Goodbye!")
        break


    else:
        print("Invalid input, please enter 'y' or 'n'!")
        continue

