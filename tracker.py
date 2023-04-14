import phonenumbers

from phonenumbers import geocoder, carier, timezone

number = input ("enter your number: ")

phone_numbers = phonenumbers.parse(number)

print(f"Location {geocoder.description_for_number(phone_number, 'en')}")

print(f"Carier) {carier.name_for_number(phone_number, 'en')} ")

print(f"Time Zone {timezone.Time_Zones_for_number(phone_number)}")
