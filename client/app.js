function onClickPrice(){
    var bhks = document.getElementById("bhk");
    var bathrooms = document.getElementById("bath");
    var balconies = document.getElementById("balcony");
    var locations = document.getElementById("location");
    var estPrice = document.getElementById("est_price");
    var area = document.getElementById("total_sqft");

    var predict_url = "${window.location.hostname}/predict-price";
    console.log(predict_url);

    $.post(predict_url,{
        total_sqft: parseFloat(area.value),
        location: locations.value,
        bhk: parseInt(bhks.value),
        bath: parseFloat(bathrooms.value),
        balcony: parseFloat(balconies.value)
    }, function(data,status){
        console.log("price est");
        console.log(data);
        //console.log(data.estimated-price);
        estPrice.innerHTML = "<b>" + data['estimated-price'].toString() + " Lakhs </b>";
        console.log(status);
    });
}


function onPageLoad(){
    console.log("document loaded")
    console.log(${window.location.hostname})
    var url = "${window.location.hostname}/get_loc_names";
    console.log(url);
    $.get(url,function(data,status){
        console.log("Got location from method")
        if(data){
            var locations = data.location;
            var uiLocations = document.getElementById("location");
            console.log(uiLocations);
            $('#uiLocations').empty();
            console.log(uiLocations);
            for(var i in locations){
                //console.log(locations[i]);
                var opt = document.createElement("option");
                opt.value = locations[i];
                opt.text = locations[i];
                uiLocations.add(opt, null);
            }
        }
    });
}

window.onload = onPageLoad;
