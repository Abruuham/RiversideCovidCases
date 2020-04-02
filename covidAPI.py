from flask import Flask, jsonify, request
import json
import urllib.request

app = Flask(__name__)
city_names_url = 'https://services1.arcgis.com/pWmBUdSlVpXStHU6/arcgis/rest/services/COVID_CASES_CDP/FeatureServer/1/query?where=NAME%3D%27'
all_riv_url = 'https://services1.arcgis.com/pWmBUdSlVpXStHU6/arcgis/rest/services/COVID_CASES_CDP/FeatureServer/1/query?where=0%3D0&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=*&returnGeometry=false&returnCentroid=false&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=true&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=false&quantizationParameters=&sqlFormat=none&f=pjson'

@app.route('/', methods=['GET'])
def index():
    return 'OK'

@app.route('/city/<string:cityName>', methods=['GET'])
def get_cases(cityName):

    if (cityName.isdigit() and int(cityName) != 0):
        return jsonify({"Bad Request": "Value must be a string"}),400
    elif (cityName.isdigit() and int(cityName) == 0):
        riv_url = all_riv_url
        data = urllib.request.urlopen(riv_url).read().decode()
        cases_obj = json.loads(data)
        city_details = json.dumps(cases_obj['features'], sort_keys = True, indent = 4, separators = (',', ': '))
        return city_details
    else:
        cities_url = city_names_url + cityName + '%27&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=*&returnGeometry=false&returnCentroid=false&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=true&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=false&quantizationParameters=&sqlFormat=none&f=pjson&token='
        data = urllib.request.urlopen(cities_url).read().decode()
        cases_obj = json.loads(data)
        try:
            if cityName in cases_obj['features'][0]['attributes']['NAME']:
                city_details = json.dumps(cases_obj['features'], sort_keys = True, indent = 4, separators = (',', ': '))
                return city_details
        except:
            return "No data for target"
            


if __name__ == '__main__':
    app.run()
