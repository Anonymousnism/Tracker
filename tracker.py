import phonenumbers

from phonenumbers import geocoder, carrier, timezone

print ("PHONE NUMBERS TRACKER")

print ("=====================================")

print ("███╗░░░███╗░█████╗░░░░░░██╗░█████╗░       ") 

print ("████╗░████║██╔══██╗░░░░░██║██╔══██╗       ") 

print ("██╔████╔██║██║░░██║░░░░░██║██║░░██║       ") 

print ("██║╚██╔╝██║██║░░██║██╗░░██║██║░░██║       ") 

print ("██║░╚═╝░██║╚█████╔╝╚█████╔╝╚█████╔╝       ") 

print ("╚═╝░░░░░╚═╝░╚════╝░░╚════╝░░╚════╝░       ")          

print ("=====================================")

number = input ("enter your number: ")

phone_number = phonenumbers.parse(number)

print(f"Location: {geocoder.description_for_number(phone_number, 'en')}")

print(f"Carier: {carrier.name_for_number(phone_number, 'en')} ")

print(f"Time Zone: {timezone.time_zones_for_number(phone_number)}")
