
# get the format the input is in 
def getFormatofOutput():
    return input("Enter the format the output must be in (c,f,k): ")

#get the format the output must be in
def getInputFormatofTemperature():
    return input("Enter the format input is in (c,f,k): ")

#convert the data in celcius to the required output type
def convertFromCelcius(converttemp):
    if(converttemp=="f"):
        fahrenheit = (value * 9/5) + 32
        print(f"{value}°C is equal to {fahrenheit}°F")
    elif(converttemp=="k"):
        kelvin=value+273
        print(f"{value}°C is equal to {kelvin}k")


#convert the data in farenheit to the required output type
def convertFromFarenheit(converttemp):
    #convert temp is the format the output must be in
    #the if else will help choose the correct block to ececute with converttemp as a condition
    if converttemp=="c":
        celcius = (value+32)* 5/9
        print(f"{value}°F is equal to {celcius}°C")
    elif converttemp=="k":
        kelvin = (value - 32) * 5/9 + 273.15
        print(f"{value}°F is equal to {kelvin}K")


#convert the data in kelvin to the required output type
def convertFromKelvin(coverttemp):
    if converttemp=="c":
        celcius=value-273
        print(f"{value}°C is equal to {celcius}°C")
    elif converttemp=="f":
        fahrenheit = (value - 273.15) * 9/5 + 32
        print(f"{value}K is equal to {fahrenheit}°F")

""" the main function that will take the numerial value of the the temperature and
sends it to the corrct function
"""
if __name__=="__main__":
    value=float(input("Enter the Temperature value: "))
    tempformat=getInputFormatofTemperature()
    converttemp=getFormatofOutput()

    #if elif will choose the correct method to call
    if(tempformat=="c"):
        convertFromCelcius(converttemp)
    elif tempformat=="f":
        convertFromFarenheit()
    elif tempformat=="k":
        convertFromKelvin()
