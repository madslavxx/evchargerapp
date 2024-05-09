#All variables
charger_types = [
    "CCS",
    "CHAdeMO",
    "J1772",
    "Tesla",
]
#All charger types in Windsor
#https://chargefinder.com/en/windsor/charging-station/zx7d5r
#charger_Location_name_list = ["Adventure Bay Family Waterpark","Via Rail Canada Inc. | Windsor","Windsor Engine 1 (QR 2000543)","Market Square Complex","Education Parking Lot","Centre for Engineering Innovation","Renewable Energy Tech Centre","Parking Structure","Assumption Parking Lot","Toldo Lancer Centre Parking Lot","Windsor Professional Centre","Comfort Inn & Suites","| 17834 | Windsor","Trike My Bike","Premier Chevrolet Cadillac | Outside","Windsor Honda","Essex Engine 1 (QR 2000627)","C22022 Windsor","Windsor, ON Supercharger","South West Detention Centre","Reaume Chevrolet Buick GMC","Reaume Chevrolet Buick GMC","Reaume Chevrolet Buick GMC | DC","The Townsend","Windsor Rue des Sources","Ville de Windsor Hotel-de-Ville","Aréna de Windsor"]
#All charger name/what its located near

print("Welcome to my EV map!")

if (input("Would you like a charger to come to you?") == "yes"):
  print(
      "If you would like to see your availability to schedule an appointment go to your calendar at \nhttps://calendar.google.com/ \n\033[1mMobile charging is not available in Windsor yet.\033[0m Here's an article on mobile charging in Quebec: \nhttps://electricautonomy.ca/2023/03/26/cafu-mobile-ev-charger-world-premier-quebec/"
  )
print(
    "Check your port to see which of the EV connectors your car requires. Is your charger number 1,2,3, or 4?(Left to right) Close the image after using it to go further."
)

charger_type_number = input("What is your charger type?")
print("Your charger is a " + charger_types[int(charger_type_number) - 1])

charger_level = input(
    "What is the charger level you are looking for? (1 is slowest and 3 is the fastest) "
)
needed_range = input("How much range do you need? (km)")
print(
    "Use this map to help you find the nearest charger to you.\nhttps://chargefinder.com/en/windsor/charging-station/zx7d5r"
)
# make a list of all the chargers
#https://www.w3schools.com

# %%