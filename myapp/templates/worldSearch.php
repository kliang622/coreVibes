<?php
// search.php

$servername = "localhost";
$username = "hpham";
$password = "halpal";
$dbname = "ArtistByRegion";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if (isset($_GET['region'])) {
    $region = $_GET['region'];

    $query = "SELECT region, artist, MAX(song_count) AS max_song_count FROM ArtistByRegion WHERE region LIKE '%$region%' GROUP BY region";
    $result = $conn->query($query);

    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            echo "<h2>{$row['region']}</h2>";
            echo "<p>Top Artist: {$row['artist']}</p>";
            echo "<p>Song Count: {$row['max_song_count']}</p>";
            echo "<hr>";
        }
    } else {
        echo "<p>No results found for '$region'.</p>";
    }

    $conn->close();
} else {
    echo "<p>Please enter a region.</p>";
}
?>
