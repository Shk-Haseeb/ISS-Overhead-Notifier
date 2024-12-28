import requests
from datetime import datetime
import smtplib
import time

MY_LAT = XXX # Add Your latitude
MY_LONG = XXXX # Add Your longitude
MY_POSITION = (MY_LAT, MY_LONG)

#API FOR ISS SATELLITE
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_position = (iss_latitude, iss_longitude)
    if MY_LAT -5 <= iss_latitude <= MY_LAT +5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True



#API FOR SUNRISE AND SUNSET
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="ADD EMAIL HERE", password="ADD PASSWORD HERE")
            connection.sendmail(
                from_addr="ADD EMAIL HERE",
                to_addrs="ADD EMAIL HERE", msg="Subject:ISS SATELLITE\n\n LOOK UP!"
            )

#IN ORDER FOR IT TO RUN EVERY 60 SDECONDS, YOU NEED TO RUN THE CODE IN THE CLOUD: PYTHON ANYWHERE!
