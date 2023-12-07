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


#timeline 
from .models import TimelineArtist, TimelineSong
from django.conf import settings
from django.conf.urls.static import static

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


    print("Positive Percentage:", positive_count)
    print("Neutral Percentage:", neutral_count)
    print("Negative Percentage:", negative_count)


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

            query = "SELECT artist, NegativeCount, NeutralCount, PositiveCount FROM ArtistSentiment WHERE artist LIKE %s;"
            db_cursor.execute(query, ['%' + artist_name + '%'])
            rows = db_cursor.fetchall()

            artists = [ArtistSentiment(*row) for row in rows]

            # Print the executed query and fetched rows
            print("Executed Query:", query % ('%' + artist_name + '%'))
            print("Fetched Rows:", rows)

            # Print the artists list
            print("Artists List:", artists)

            # Implement sentiment analysis logic and prepare data for the pie chart
            positive_percentage, neutral_percentage, negative_percentage = calculate_sentiment_percentages(artists)

            # Print sentiment percentages
            print("Positive Percentage from function:", positive_percentage)
            print("Neutral Percentage from function:", neutral_percentage)
            print("Negative Percentage from function:", negative_percentage)

            # Render the template
            return render(request, 'sentiment.html', {
                'artist_name': artist_name,
                'positive_percentage': positive_percentage,
                'neutral_percentage': neutral_percentage,
                'negative_percentage': negative_percentage,
            })
    else:
        form = SearchForm()
    return render(request, 'sentiment.html', {'form': form})


def timelineView(request): 
    db_connection = mysql.connector.connect(user="hpham", password="halpal", database="cs179g")
    db_cursor = db_connection.cursor()

    # Execute your SQL queries here
    querySong = "SELECT artist, title, TrendCount FROM HottestSongsPerYear WHERE year = %s ORDER BY TrendCount DESC LIMIT 1"
    queryArtist = """
        SELECT *
        FROM (
            SELECT artist, TrendCount AS streams
            FROM HottestSongsPerYear
            WHERE year = %s
            UNION ALL 
            SELECT artist, SongCount AS streams
            FROM MostPopularPerYear 
            WHERE year = %s
        ) AS combinedResults 
        ORDER BY streams DESC 
        LIMIT 1; 
    """

    years = range(2017, 2021)  

    timeline_data = []
    for year in years:
        db_cursor.execute(queryArtist, (year, year))
        top_artist_result = db_cursor.fetchone()
        top_artist = top_artist_result[0] if top_artist_result else 'N/A'
        
        db_cursor.execute(querySong, (year,))
        top_song_result = db_cursor.fetchone()
        top_song_artist = top_song_result[0] if top_song_result else 'N/A'
        top_song_title = top_song_result[1] if top_song_result else 'N/A'

        timeline_data.append({
            'year': year,
            'top_artist': top_artist,
            'top_song_artist': top_song_artist,
            'top_song_title': top_song_title,
        })

    return render(request, 'timeline.html', {'timeline_data': timeline_data})