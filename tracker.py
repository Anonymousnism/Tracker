import phonenumber

from phonenumber import geocoder, carrier, timezone

number = input ("enter your number: ")

print
print " Tools Hack By Mojo Anonymous "
print

phone_number = phonenumber.parse(number)

print(f"Location: {geocoder.description_for_number(phone_number, 'en')}")

print(f"Carier: {carrier.name_for_number(phone_number, 'en')} ")

print(f"Time Zone: {timezone.time_zones_for_number(phone_number)}")
