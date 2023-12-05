from django.shortcuts import render
from .models import Marker
from django.http import HttpResponse
import mysql.connector

from django.http import JsonResponse
from django.core.serializers import serialize


def home(request):
    return render(request, 'home.html')

def season(request):
    # #  seasons = Season.objects.all()
    #  return render(request, 'seasons.html')

        db_connection = mysql.connector.connect(user="hpham", password="halpal")
        db_cursor = db_connection.cursor()
        db_cursor.execute("USE cs179g;")


        #fall
        db_cursor.execute("SELECT * FROM Seasons WHERE season='fall';")
        fall_data = db_cursor.fetchall()

        #winter
        db_cursor.execute("SELECT * FROM Seasons WHERE season='winter';")
        winter_data = db_cursor.fetchall()

        #spring
        db_cursor.execute("SELECT * FROM Seasons WHERE season='spring';")
        spring_data = db_cursor.fetchall()

        #summer
        db_cursor.execute("SELECT * FROM Seasons WHERE season='summer';")
        summer_data = db_cursor.fetchall()

        return render(request, 'season.html', {'spring_data': spring_data,
                                                            'summer_data': summer_data,
                                                            'autumn_data': fall_data,
                                                            'winter_data': winter_data})
    # except Exception as e:
    #     return HttpResponse(f"An error occurred: {str(e)}")
    # finally:
    #     # Close the database connection in the finally block to ensure it's always closed
    #     if db_connection.is_connected():
    #         db_cursor.close()
    #         db_connection.close()

def hotSong(request, year):
    db_connection = mysql.connector.connect(user="hpham", password="halpal")
    db_cursor = db_connection.cursor()
    db_cursor.execute("USE cs179g;")

    query = "SELECT field_name1, field_name2 FROM HottestSongsPerYear WHERE year = %s;"
    db_cursor.execute(query, (year,))
    data_for_year = db_cursor.fetchall()

    return render(request, 'hotSong.html', {'year': year, 'data_for_year': data_for_year})


# def world(request):
#     db_connection = mysql.connector.connect(user="hpham", password="halpal")
#     db_cursor = db_connection.cursor()
#     db_cursor.execute("USE cs179g;")

#     country_id = "United States"  # Replace this with the actual country or parameter you want

#     query = "SELECT * FROM ArtistByRegion WHERE region = %s;"
#     db_cursor.execute(query, (country_id,))
    
#     country_data = db_cursor.fetchone()

#     if country_data:
#         # Adjust this part based on the actual structure of your data
#         response_data = {
#             'region': country_data[0],
#             'field1': country_data[1],
#             'field2': country_data[2],
#             # Add more fields as needed
#         }
#         return JsonResponse(response_data)
#     else:
#         return JsonResponse({'error': 'Country not found'}, status=404)

def world(request):
    markers = Marker.objects.all()
    return render(request, 'world.html', {'markers': markers})