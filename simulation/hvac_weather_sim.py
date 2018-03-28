## HVAC/Weather simulation script ##
# Some code has been ommitted in this script so that it can be used to update the database
# Weather should update every 15 minutes. HVAC should update every one minute. 
# Requires darkskylib and threading

# import necessary modules
from darksky import forecast
import threading

# initialize variables
darkskykey          = "ce3ee51d4f49051735382ee071219e87"            # please do not go crazy with this api key because i am not made of money
bhamlat             = 33.5207                                       # Birmingham, AL latitude
bhamlong            = -86.8025                                      # Birmingham, AL longitude
birmingham          = forecast(darkskykey, bhamlat, bhamlong)       # initalizes birmingham as a forecast object 
internal_temp_low   = 68                                            # value will be set by the app, hard coded for now
internal_temp_high  = 75                                            # value will be set by the app, hard coded for now
internal_temp_curr  = 74.95                                         # value set is arbitrary, will represent current interal temperature for hvac_update
house_state         = 1                                             # state of the house, 0 = closed, 1 = door open, 2 = window open
external_temp       = birmingham.temperature                        # external temperature in Birmingham
weathercycle        = 15 * 60                                       # update_weather will cycle every 15 minutes
hvaccycle           = 60                                            # hvac_update will cycle every 1 minute
powerusage          = 0                                             # daily power usage in watts TODO reset to 0 at the end of the day?

# update weather will update the weather in the database every fifteen minutes as well as store the external temperature in a global variable to be used by hvac_update
def update_weather():
    external_temp       = birmingham.temperature
    precipintensity     = birmingham.precipIntensity
    precipprobability   = birmingham.precipProbability 
    summary             = birmingham.summary
    #TODO - Send weather data to database [timestamp, external_temp, precipintensity, precipprobability, summary]
    print('external_temp: {0} F, precipintensity: {1} mm, precipprobability: {2}%, summary: {3}'.format(external_temp, precipintensity, precipprobability, summary)) # print statement for verification
    threading.Timer(weathercycle, update_weather).start() # threading implemented to run every 15 minutes

# update hvac works under the assumption that values will be updated once per minute. If modifications need to be made, the rates of change will need to be modified as well. 
def update_hvac():
    global internal_temp_curr           # set internal_temp_curr so that it can be used inside this loop
    global powerusage                   # set powerusage so it can be used inside this loop
    powerusage = 0                      # resets to each loop, can be taken out if we want to do an accumulation instead

    if(house_state == 0):               # if the house is closed, run this code
        internal_temp_curr = internal_temp_curr + 0.0033*(external_temp - internal_temp_curr) 
    elif(house_state == 1):             # if a door is open, run this code
        internal_temp_curr = internal_temp_curr + 0.04*(external_temp - internal_temp_curr)
    else:                               # if a window is open, run this code (can be removed if we didn't implement windows)
        internal_temp_curr = internal_temp_curr + 0.02*(external_temp - internal_temp_curr)

    # determine power usage
    # if the internal temperature is above the thermostat high setting, turn on the HVAC to cool the house for one minute
    # Only send HVAC data when the HVAC is run. Theoretically the HVAC should never run longer than one minute unless under extreme scenarios
    if(internal_temp_curr >= internal_temp_high):
        powerusage = powerusage + 58.3 # 58.3 is the value in watts per minute, if we wanted kWh it would be 0.0581 kWh
        # TODO put power usage into power usage table
        internal_temp_curr = internal_temp_curr - 1 
    elif(internal_temp_curr <= internal_temp_low):
        powerusage = powerusage + 58.3 # 58.3 is the value in watts per minute, if we wanted kWh it would be 0.0581 kWh
        # TODO put power usage into power usage table
        internal_temp_curr = internal_temp_curr + 1
        
    print('internal_temp_curr: {0} F, power usage {1} W'.format(internal_temp_curr, powerusage)) # print statement for verification
    threading.Timer(hvaccycle, update_hvac).start() # threading implemented to run once per minute

update_weather()
update_hvac()