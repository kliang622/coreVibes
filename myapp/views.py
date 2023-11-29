from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector

from django.http import JsonResponse
from django.core.serializers import serialize


def home(request):
    return render(request, 'home.html')

# def season(request):
#      seasons = Season.objects.all()
#      return render(request, 'seasons.html', {'seasons': seasons})

        # db_connection = mysql.connector.connect(user="hpham", password="halpal")
        # db_cursor = db_connection.cursor()
        # db_cursor.execute("USE cs179g;")

        # return render(request, 'season.html')

        #fall
        # db_cursor.execute("SELECT * FROM Seasons WHERE season='fall';")
        # fall_data = db_cursor.fetchall()

        # #winter
        # db_cursor.execute("SELECT * FROM Seasons WHERE season='winter';")
        # winter_data = db_cursor.fetchall()

        # #spring
        # db_cursor.execute("SELECT * FROM Seasons WHERE season='spring';")
        # spring_data = db_cursor.fetchall()

        # #summer
        # db_cursor.execute("SELECT * FROM Seasons WHERE season='summer';")
        # summer_data = db_cursor.fetchall()

        # return render(request, 'seasons_template.html', {'spring_data': spring_data,
        #                                                     'summer_data': summer_data,
        #                                                     'autumn_data': fall_data,
        #                                                     'winter_data': winter_data})
    # except Exception as e:
    #     return HttpResponse(f"An error occurred: {str(e)}")
    # finally:
    #     # Close the database connection in the finally block to ensure it's always closed
    #     if db_connection.is_connected():
    #         db_cursor.close()
    #         db_connection.close()