
import folium 
import matplotlib.pyplot as plt
from config import args



def display_map(args):
    
    # latitude and logitude range for Malawi 
    # [-15.786111, 35.005833] --> center
    range_latitude_Malw = [-17, -9]
    range_longitude_Malw = [33, 36]
    
    # latitude and logitude range for Mozambique
    # [-13.2512161, 34.3015278] --> center
    range_latitude_Moz = [-26, -10]
    range_longitude_Moz = [31, 41]
    
    while (True):
        Country_Name = input("Enter the name of your chosen country : Malawi or Mozambique\n\n")
        if (Country_Name != "Malawi" and Country_Name != "Mozambique"):
            print("Country name don't match. Try the exact name: Malawi or Mozambique")
        else:
            if Country_Name == "Malawi":
                if ( range_latitude_Malw[0] <= args.latitude <= range_latitude_Malw[1] and range_longitude_Malw[0] <= args.longitude <= range_longitude_Malw[1]):
                    pass
                else:
                    raise ValueError("Your latitude or longitude don't match! Please try again.")

            elif Country_Name == "Mozambique":
                if ( range_latitude_Moz[0] <= args.latitude <= range_latitude_Moz[1] and range_longitude_Moz[0] <= args.longitude <= range_longitude_Moz[1]):
                    pass
                else:
                    raise ValueError("Your latitude or longitude don't match! Please try again.")
            
            M = folium.Map([args.latitude, args.longitude], zoom_start=5)
            folium.GeoJson(args.geojson_file).add_to(M)
            return M