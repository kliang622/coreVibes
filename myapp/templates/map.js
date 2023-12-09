// map.js

var map = L.map('map').setView([0, 0], 2);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

function onCountryClick(e) {
    var countryCode = e.target.feature.properties.iso_a2;

    fetch('/world/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')  
        },
        body: JSON.stringify({ country_code: countryCode })
    })
    .then(response => response.json())
    .then(data => {
        var infoPanel = document.getElementById('info-panel');
        var countryInfo = document.getElementById('country-info');
        countryInfo.textContent = `Country: ${data.country}, Artist: ${data.artist}, Song Count: ${data.song_count}`;
    });
}

fetch('https://unpkg.com/world-atlas@1.0.12/countries-110m.json')
    .then(response => response.json())
    .then(data => {
        L.geoJson(data, {
            onEachFeature: function(feature, layer) {
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
