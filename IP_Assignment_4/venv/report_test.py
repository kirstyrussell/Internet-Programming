import requests
import json_with_dates

PORT = 80

custResponse = requests.get("http://localhost:8000/chinook/customer")
print(custResponse.text)

customers = json_with_dates.loads(custResponse.text)

for spec in species:
    gen_id = species[0]
    invoiceResponse = requests.get(
        "http://localhost:{}/taxa/species/{}".format(PORT, gen_id)
    )
    template = "{:3} {:15} {:15} {:15}"
    line = template.format(gen_id, genus, species, common_name)
    print(line)