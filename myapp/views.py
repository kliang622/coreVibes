from django.shortcuts import render
from .models import Marker
from django.http import HttpResponse
import mysql.connector

from django.http import JsonResponse
from django.core.serializers import serialize


#artist sentiment
from .forms import SearchForm
from .models import ArtistSentiment
import math


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


def calculate_sentiment_percentages(artists):
    positive_count = sum(artist.PositiveCount if artist.PositiveCount is not None and not math.isnan(artist.PositiveCount) and artist.PositiveCount != float('inf') else 0 for artist in artists)
    negative_count = sum(artist.NegativeCount if artist.NegativeCount is not None else 0 for artist in artists)

    # if artist.NegativeCount is not None and not math.isnan(artist.NegativeCount) and artist.NegativeCount != float('inf') else 0 for artist in artists
    neutral_count = sum(artist.NeutralCount if artist.NeutralCount is not None and not math.isnan(artist.NeutralCount) and artist.NeutralCount != float('inf') else 0 for artist in artists)
    total = positive_count + neutral_count + negative_count

    positive_percentage = (positive_count / total) * 100 if total != 0 else 0
    neutral_percentage = (neutral_count / total) * 100 if total != 0 else 0
    negative_percentage = (negative_count / total) * 100 if total != 0 else 0


    # After calculating sentiment percentages
    print("Positive Percentage:", positive_percentage)
    print("Neutral Percentage:", neutral_percentage)
    print("Negative Percentage:", negative_percentage)


    return positive_percentage, neutral_percentage, negative_percentage


def search_artist(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            artist_name = form.cleaned_data['artist_name']

            # Perform search in the database
            db_connection = mysql.connector.connect(user="hpham", password="halpal", database="cs179g")
            db_cursor = db_connection.cursor()

            query = "SELECT * FROM ArtistSentiment WHERE artist LIKE %s;"
            db_cursor.execute(query, ('%' + artist_name + '%',))
            artists = [ArtistSentiment(*row) for row in db_cursor.fetchall()]

            # Implement sentiment analysis logic and prepare data for the pie chart
            positive_percentage, neutral_percentage, negative_percentage = calculate_sentiment_percentages(artists)


            return render(request, 'sentiment.html', {
                'artist_name': artist_name,
                'positive_percentage': positive_percentage,
                'neutral_percentage': neutral_percentage,
                'negative_percentage': negative_percentage, 
            })
    else:
        form = SearchForm()
    return render(request, 'sentiment.html', {'form': form})