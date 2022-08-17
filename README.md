# VivariumPro

files for the VivariumPro project

**Description**

Vivarium Pro is designed for use in the maintenance and monitoring of enclosed tropical terrariums. Tropical enclosures require careful balance of humidity and temperature to be successful. Many common tropical pets are lost due to broad temperature fluctuations and inadequate monitoring. This program would allow the user to remotely control and monitor their enclosures and stay apprised of any dangerous conditions. Because this program will be written in an object-oriented language, it is easily scalable to multiple enclosures with different temperature, humidity, and sunlight requirements. The Smart Plug allows easy control over all output devices.

The data used to determine the state of each output device (on/off) will be input as HI and LO parameters. Example humidity parameters would be .80 for 80% and .95 for 95%. The program will retrieve the current humidity level from the DHT22/AM2302 hydrothermograph and compare it to the input parameters. If the humidity level exceeds the HI parameter, the program will call the module to supply power to the outlet for the fan. The fan will run until the humidity is back within parameters. If the humidity is below the LO parameter, an email alert will be sent to the user asking them to supply water to the enclosure to raise the humidity. Future versions with expanded functionality may include the addition of a fogger or mister to directly increase humidity levels.

The temperature module will function in a similar manner. A heat mat will be utilized to raise temperatures when below the LO value. If temperatures are above the HI value, the heat mat will be turned to OFF, power to the fan will be turned to ON, and an SMS alert sent to the user. The LED grow light will be controlled according to a cycle that best coincides with the natural habitat of the plants and animals within the terrarium. This reduces stress on the animal and creates an optimal growing environment for the plants.

The data retrieved from the hydrothermographs is not only for use by the program. This data will be exported, stored, and graphically interpreted utilizing AWS via MongoDB which includes built-in data visualization. Users can view historic data as well as view current conditions in an easy-to-read graphic or can select specific data points to export for additional analysis.

**Hardware Requirements**

Raspberry Pi with GPIO

Lead wires

DHT22 sensor

Kasa TP Link smart plugs or smart strip

LCD 16x2

Terrarium

Light source

Heat source

Fan


Optional:

Fogger/Mister

Soil moisture sensor (adafruit)

Mounting Hardware

Aftermarket raspberry pi case and fan


**How To**
-coming soon
