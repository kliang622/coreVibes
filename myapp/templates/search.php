<?php
$servername = "localhost";
$username = "hpham";
$password = "halpal";
$dbname = "ArtistSentiment";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Handle search
if (isset($_GET['artist'])) {
    $artist = $_GET['artist'];

    // SQL to search for the artist
    $sql = "SELECT * FROM artists WHERE name LIKE '%$artist%'";
    $result = $conn->query($sql);

    // Display search results
    if ($result->num_rows > 0) {
        echo "<h2>Search Results:</h2>";
        echo "<ul>";
        while ($row = $result->fetch_assoc()) {
            echo "<li>" . $row['name'] . "</li>";
        }
        echo "</ul>";
    } else {
        echo "<p>No results found for '$artist'.</p>";
    }
}

$conn->close();
?>
