import phonenumbers

from phonenumbers import geocoder, carrier, timezone

number = input ("enter your number: ")

phone_numbers = phonenumbers.parse(number)

print(f"Location: {geocoder.description_for_number(phone_number, 'en')}")

print(f"Carier: {carrier.name_for_number(phone_number, 'en')} ")

print(f"Time Zone: {timezone.time_zones_for_number(phone_number)}")
