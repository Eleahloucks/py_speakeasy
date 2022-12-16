'use strict';
//check to make sure js is connected
console.log('js connected');

function initMap() {

  const atlanticCoords = {
    lat: 34.50673836013896,
    lng: -39.811884909459955,
  };

  const basicMap = new google.maps.Map(document.getElementById('map'), {
    mapId: "751009d2f3e936a",
    center: atlanticCoords,
    zoom: 2,
  });

  // const atlanticMarker = new google.maps.Marker({
  //   position: atlanticCoords,
  //   title: 'Atlantic',
  //   map: basicMap,
  // });

  // atlanticMarker.addListener('click', () => {
  //   alert('Hi!');
  // });

  const atlanticInfo = new google.maps.InfoWindow({
    // content: '<h1>atlantic!</h1>',
  });

  atlanticInfo.open(basicMap, atlanticCoords);

  const locations = [
    {
      name: 'William & Graham',
      coords: {
        lat: 40.01563220031631,
        lng: -105.27025676465864,
      },
    },
    {
      name: 'Lisbon, Portugal',
      coords: {
        lat: 38.7242049777057,
        lng: -9.13926109963694,
      },
    },
    {
      name: 'San Francisco, CA',
      coords: {
        lat: 37.75550777992014,
        lng: -122.4945940666157,
      },
    },
    {
      name: 'Manhattan, NY',
      coords: {
        lat: 40.732509540838706,
        lng: -73.98777282542899,
      },
    },
    {
      name: 'Puerto Rico, San Juan',
      coords: {
        lat: 18.410867123820488,
        lng: -66.04850152288675,
      },
    },
    {
      name: 'Morocco, North Africa',
      coords: {
        lat: 33.66335789287453,
        lng: -7.228298824177478,
      },
    },
    {
      name: 'Bidart, France',
      coords: {
        lat: 43.44625284939808,
        lng: -1.5884287992049693,
      },
    },
    {
      name: 'Canggu, Bali',
      coords: {
        lat: -8.65471615699866,
        lng: 115.12576792271399,
      },
    },
    {
      name: 'Fuerteventura, Canary Islands',
      coords: {
        lat: 28.30226540939817,
        lng: -13.908063377779829,
      },
    },
    {
      name: 'Santa Teresa, Costa Rica',
      coords: {
        lat: 9.631830142859062,
        lng: -85.13586287262456,
      },
    }
  ];

  const markers = [];
  for (const location of locations) {
    markers.push(
      new google.maps.Marker({
        position: location.coords,
        title: location.name,
        map: basicMap,
        icon: {
          // custom icon
          url: '/static/img/new_marker.svg',
          scaledSize: {
            width: 30,
            height: 30,
          },
        },
      }),
    );
  }

  for (const marker of markers) {
    const markerInfo = `
      <h1>${marker.title}</h1>
      <p>
        Located at: <code>${marker.position.lat()}</code>,
        <code>${marker.position.lng()}</code>
      </p>
    `;

    const infoWindow = new google.maps.InfoWindow({
      content: markerInfo,
      maxWidth: 200,
    });

    marker.addListener('click', () => {
      infoWindow.open(basicMap, marker);
    });
  }
}
