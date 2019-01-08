function showPosition()
  {
  lat=30.6208435;  
  lon=-96.3420207;
  latlon=new google.maps.LatLng(lat, lon)
  mapholder=document.getElementById('mapholder')


  var myOptions={
  center:latlon,zoom:14,
  mapTypeId:google.maps.MapTypeId.ROADMAP,
  mapTypeControl:false,
  navigationControlOptions:{style:google.maps.NavigationControlStyle.SMALL}
  };
  var map=new google.maps.Map(document.getElementById("mapholder"),myOptions);
  var marker=new google.maps.Marker({position:latlon,map:map,title:"We are here!"});
  }

 showPosition();
