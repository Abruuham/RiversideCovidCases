import requests, lxml
from flask import Flask, jsonify, request
import json
import urllib.request
from bs4 import BeautifulSoup
import re

app = Flask(__name__)
city_names_url = 'https://services1.arcgis.com/pWmBUdSlVpXStHU6/arcgis/rest/services/COVID_CASES_CDP_PublicView/FeatureServer/1/query?where=NAME%3D%27'
all_riv_url = 'https://services1.arcgis.com/pWmBUdSlVpXStHU6/ArcGIS/rest/services/COVID_CASES_CDP_PublicView/FeatureServer/1/query?where=0%3D0&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=*&returnGeometry=false&returnCentroid=false&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pjson'

list_url = 'https://services1.arcgis.com/pWmBUdSlVpXStHU6/arcgis/rest/services/COVID_CASES_CDP_PublicView/FeatureServer/1/query?where=0%3D0&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=*&returnGeometry=false&returnCentroid=false&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=true&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=false&quantizationParameters=&sqlFormat=none&f=pjson'


@app.route('/', methods=['GET'])
def index():
    return 'OK'

@app.route('/city/<string:cityName>', methods=['GET'])
def get_cases(cityName):
    url_cityName = cityName.replace("-","+") + "%"
    cityName = cityName.replace("-", " ")
    if (cityName.isdigit() and int(cityName) != 0):
        return jsonify({"Bad Request": "Value must be a string"}),400
    elif (cityName.isdigit() and int(cityName) == 0):
        riv_url = all_riv_url
        data = urllib.request.urlopen(riv_url).read().decode()
        cases_obj = json.loads(data)
        city_details = json.dumps(cases_obj['features'], sort_keys = True, indent = 4, separators = (',', ': '))
        return city_details
    else:
        
        cities_url = city_names_url + url_cityName + '27&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=*&returnGeometry=false&returnCentroid=false&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=true&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=false&quantizationParameters=&sqlFormat=none&f=pjson&token='
        data = urllib.request.urlopen(cities_url).read().decode()
        cases_obj = json.loads(data)
        try:
            if cityName in cases_obj['features'][0]['attributes']['NAME']:
                city_details = json.dumps(cases_obj['features'], sort_keys = True, indent = 4, separators = (',', ': '))
                return city_details
        except:
            cityName = cityName.replace('-', ' ')
            return "No data for target " + cityName + " "
            
    return cityName + "\n"
    
    
# Returns a list of all cities in alphabetical order, displaying
# cases and deaths associated with each in a readable list. At the end
# will also be displayed the number total of cases and deaths
@app.route('/city-list', methods=['GET'])
def list_cities():
    arr = []
    count = 0 #this count was correct but for some reason, the riverside website is
    #showing more cases that was is being counted from all cities
    death_count = 1
    data = urllib.request.urlopen(list_url).read().decode()
    cases_obj = json.loads(data)
    for city_name in cases_obj['features']:
        arr.append(city_name['attributes']['NAME'] + ': \n \t' + "Cases: " +
                   str(city_name['attributes']['Point_Count']) + "\n \t" +
                   'Deaths: ' + str(city_name['attributes']['Sum_Deceased']))
        count += city_name['attributes']['Point_Count']
        death_count += city_name['attributes']['Sum_Deceased']
    arr.sort()
    return "\n".join(arr) + "\n" + "Riverside Total Cases: " + str(count) + "\n" + "Riverside Total Deaths: " + str(death_count) + "\n"


if __name__ == '__main__':
    app.run()
