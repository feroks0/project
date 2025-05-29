from machine import ADC, Pin # we import needed classes to convert analog signal to digital and specify the pin
import time # we need time module to set execution period of code

sensorPin = ADC(Pin(34)) #sensor signal is received from specified pin (must be determined and edited by the user)
sensorPin.atten(ADC.ATTN_11DB)  #reducing the input voltage for ADC (must be determined according to the operating voltage of the sensor used)

#openning an csv file in writing mode 
with open("uv_data.csv", "w") as f:
    f.write("UV_Index\n")

while True:
    #reading sensor values
    adcValue = sensorPin.read()

    #calculating uv index and rounding the value by including only 2 digit after the comma
    uvIndex = (adcValue / 4095.0) * 15.0
    uvIndex = round(uvIndex, 2)

    #we are changing dot to the comma to avoid the possible issues in the csv file (use of dots causes the data to be converted to dates within the file)
    uvIndexStr = str(uvIndex).replace(".", ",")

    #openning the created file in adding mode and saving the data
    with open("uvdata.csv", "a") as f:
        f.write(f"{uvIndexStr}\n")

    print("Kaydedildi: UV Index:", uvIndexStr) #printing uv index to the shell
    time.sleep(1) #we set the execution period of code

