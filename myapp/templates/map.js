// map.js

// Initialize the map
var map = L.map('map').setView([0, 0], 2);

// Load a tile layer (you may need to obtain an API key)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Define a function to handle country clicks
function onCountryClick(e) {
    // Extract the ISO country code
    var countryCode = e.target.feature.properties.iso_a2;

    // Use fetch to make an AJAX request to the Django view
    fetch('/world/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')  // Include CSRF token for security
        },
        body: JSON.stringify({ country_code: countryCode })
    })
    .then(response => response.json())
    .then(data => {
        // Update the info panel with the fetched data
        var infoPanel = document.getElementById('info-panel');
        var countryInfo = document.getElementById('country-info');
        countryInfo.textContent = `Country: ${data.country}, Artist: ${data.artist}, Song Count: ${data.song_count}`;
    });
}

// Load GeoJSON data for world countries
fetch('https://unpkg.com/world-atlas@1.0.12/countries-110m.json')
    .then(response => response.json())
    .then(data => {
        // Add GeoJSON layer to the map
        L.geoJson(data, {
            onEachFeature: function(feature, layer) {
                // Attach the click event to each country
                layer.on({
                    click: onCountryClick
                });
            }
        }).addTo(map);
    });

// Function to get CSRF token from cookies
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
