# GeoService

This Api is defined with Swagger at [PostmatesGeoServices](https://app.swaggerhub.com/apis/PostmatesGeoServices/PostmatesGeoServices/1.0.0), you can also see the `yaml` file in thie github [path](https://github.com/postmateschallenge/GeoService/blob/master/swagger.yaml). Swagger provides a generated server side with flask framwork, then I implemented the service call with Python standard library `urllib`, `json` and `re`. Functionalities have been fully tested with Python 3.6.6

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

You can try with the UI and or `CURL` command as 

```
curl -X GET "http://localhost:8080/PostmatesGeoServices/PostmatesGeoServices/1.0.0/Address?addr=690%205th%20St%3B%20San%20Francisco%2C%20California%20" 
```
