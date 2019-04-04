
from bottle import route, run, static_file, template
from json_with_dates import loads
import requests

REST_PORT = 21212
WEB_PORT = 8085

page_template = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset = "UTF-8">
        <title>Measures Summary Report</title>
        <link rel = "stylesheet"
         type = "text/css"
         href = "style.css" />
    </head>
    
    <body>
        <h1>Measures Summary Report</h1>
        {}
    </body>
    
</html>
"""

template = "<tr>  <td>{:15}</td>  <td>{:15}</td>  <td>{:15}</td>  <td>{:15}</td>  <td>{:20}</td>  </tr>"
template_headers = "<tr>  <th>{:10}</th>  <th>{:15}</th>  <th>{:10}</th>  <th>{:10}</th>  <th>{:20}</th>  </tr>"


@route("/")
def report():

    web_page = "<table class='grid'>" + template_headers.format("Area ID", "Name", "Locations", "Avg Measure",
                                                                "Categories")

    r = requests.get("http://localhost:{}/measures/area".format(REST_PORT))
    rows = loads(r.text)

    for area_rows in rows:
        area_id = area_rows[0]

        # Gets number of locations
        r = requests.get("http://localhost:{}/measures/num_locations/area/{}".format(REST_PORT, area_id))
        num_locations = loads(r.text)

        # Gets avg measurements for location
        measurement_request = requests.get("http://localhost:{}/measures/avg_values/location/{}".format(REST_PORT,
                                                                                                        area_id))
        measurements = loads(measurement_request.text)
        if measurements is None:
            avg_values = "-----"
        else:
            avg_values = measurements

        # Gets Categories
        r = requests.get("http://localhost:{}/measures/categories/area/{}".format(REST_PORT, area_id))
        categories = loads(r.text)
        cat = ""
        if categories is None:
            cat = "-----"
        else:
            for cat_rows in categories:
                cat += str(cat_rows[1]) + " "

        # Constructs line from data retrieved earlier
        line = template.format(area_rows[0], area_rows[1], num_locations, avg_values, str(cat))
        web_page += line

    web_page += "</table>"
    return page_template.format(web_page)


@route('/web/<filepath:path>')
def send_static(filepath):
    print("send_static", filepath)
    return static_file(filepath, root='web')


run(host='localhost', port=WEB_PORT)



