import time
import board
import adafruit_dht
import datetime
from datetime import timezone
import pymongo
import I2C_LCD_driver
import json

#Initialize the I2C 16x2 LCD Display
display = I2C_LCD_driver.lcd()
display.lcd_clear()

# Initialize the dht sensor connected to GPIO 4 (board.D4)
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False )


# Set up python client for MongoDB
client = pymongo.MongoClient("mongodb+srv://<username>:<password>@vivariumpro.jyp9odj.mongodb.net/?retryWrites=true&w=majority")
    
    
db = client.SensorData
collection = db.DHT22
sensor = 1

while True:
    try:
        # Read values DHT22 sensor
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(f'temp: {temperature_f}  humidity:  {humidity}')
        
        display.lcd_display_string("Temp: %d%s F" % (temperature_f, chr(223)), 1)
        display.lcd_display_string("Humidity: %d %%" % humidity, 2)
        
        
        now = datetime.datetime.now(datetime.timezone.utc)
        print(now)
        
        # Create dictionary to send to GDA in JSON format
        sensor_data = { "Time" : now,
                        "Temp" : temperature_f,
                        "Humidity" : humidity }
       
        data_out = json.dumps(sensor_data)

        # Create Time Series formatted document
        document = {'"timestamp"': now,
                    "metadata": {"sensorId": sensor, "type": "climate"},
                    "temperature_fahrenheit": temperature_f,
                    "temperature_celsius": temperature_c,
                    "humidity": humidity }
        
        try:
            #insert document into database collection
            doc_id = collection.insert_one(document).inserted_id

            print("Recorded reading to document {}".format(doc_id))
            time.sleep(10)
        
        except:
            print("error writing to collection")
            continue

    except RuntimeError as error:
        #try again after sensor read error
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        #dhtDevice.exit()
        #raise error
        print("exception occurred, trying again in 2 seconds")
        time.sleep(2.0)
        continue
    time.sleep(300.0)
