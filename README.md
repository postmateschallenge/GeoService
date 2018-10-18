# GeoService

This Api is defined with Swagger at [PostmatesGeoServices](https://app.swaggerhub.com/apis/PostmatesGeoServices/PostmatesGeoServices/1.0.0), you can also see the `yaml` file in thie github [path](https://github.com/postmateschallenge/GeoService/blob/master/swagger.yaml). Swagger provides a generated server side with flask framwork, then I implemented the service call with Python standard library `urllib`, `json` and `re` in this [file](https://github.com/postmateschallenge/GeoService/blob/master/python-flask-server/swagger_server/controllers/address_controller.py). Functionalities have been fully tested with Python 3.6.6

## Definition 

### Request
Base URL: http://localhost:8080/PostmatesGeoServices/PostmatesGeoServices/1.0.0/

Tag: Address

Query: addr

### Response
Response Code:

200 Successful operation
400 Invalid operation

#### Successful return formats:


{'Success':  
    "PossibleLocations": [  
        {  
        "lat": 0.0,  
        "lng": 0.0  
      }  
    ]  
}  
  
or   
  
{'Success':   
    "PossibleLocations": []   
}   

This happens when the service we are calling is still working, but the address is not a proper one.

#### Failed return formats:

{'Failed':  
    "PossibleLocations": []  
}  
This happens when both primary and backup services are down, but our service exposed is still good. 

## Usage
To run the server, please execute the following from the path `GeoService/python-flask-server`:

```
pip3 install -r requirements.txt
python3 -m swagger_server
```

and open your browser to here:

```
http://localhost:8080/PostmatesGeoServices/PostmatesGeoServices/1.0.0/ui/
```
The definition of service Apis is also located here.

You can try with the UI and or `CURL` command as 

```
curl -X GET "http://localhost:8080/PostmatesGeoServices/PostmatesGeoServices/1.0.0/Address?addr=690%205th%20St%3B%20San%20Francisco%2C%20California%20" 
```

### Demo of service call with both ways

You can copy and paste the URL to browser to see the result as well

![Demo1](http://g.recordit.co/KNqC9cNr4i.gif)

### Demo of service Fallback

Google geocoding service only returns one result and is more stable, so I implemented it with the primary service. In this demo, I use an ambiguous address `10, 1st Ave` which could be mapped to many locations. Here geocoder service should return multiple coordinates if we query through it. I run the service with successful call to Google service first, then disable the Google Api and request again. You can see the service returns result same as what we use Here service directly, it means it switched to Here service after it finds primary service down. 

![Demo2](http://g.recordit.co/PNnviSj49q.gif)

