

import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


timeout = time.time() + 10*1  #Set 1 Minute timeout
# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
chan_0 = AnalogIn(ads, ADS.P0)
#chan_1 = AnalogIn(ads, ADS.P1)
#chan_2 = AnalogIn(ads, ADS.P2)
#chan_3 = AnalogIn(ads, ADS.P3)



# Create differential input between channel 0 and 1
# chan = AnalogIn(ads, ADS.P0, ADS.P1)

print("{:>5}\t{:>5}".format("raw", "v"))

while True:
    print("CHAN 0: "+"{:>5}\t{:>5.3f}".format(chan_0.value, chan_0.voltage))
#    print("CHAN 1: "+"{:>5}\t{:>5.3f}".format(chan_1.value, chan_1.voltage))
#    print("CHAN 2: "+"{:>5}\t{:>5.3f}".format(chan_2.value, chan_2.voltage))
#    print("CHAN 3: "+"{:>5}\t{:>5.3f}".format(chan_3.value, chan_3.voltage))
    time.sleep(0.5)
    if time.time() > timeout:
        break
