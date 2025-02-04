# orchestrate-skill-submitClaim-fastapi
submit a claim with some data

## build it

* If you have a mac, then run commands :

```sh
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

for win OS in powershell run
```sh
.\.venv\bin\activate
```

pip freeze | grep -E 'fastapi|uvicorn|pydantic|SQLAlchemy|python-dotenv|psycopg2-binary' > requirements.txt




Run the application using: 
```sh
uvicorn app:app --host 0.0.0.0 --port 8000

```



## test it

```sh

curl --location 'http://0.0.0.0:8000/submit-claim' \
--header 'Content-Type: application/json' \
--data-raw '{
    "Name": "Jane Doe",
    "PolicyNumber": "ABC123456789",
    "VehicleMakeAndModel": "Toyota Camry",
    "VehicleYear": "2020",
    "LicensePlateNumber": "7XYZ123",
    "DateOfIncident": "January 20, 2025",
    "TimeOfIncident": "3:45 PM",
    "LocationOfIncident": "Interstate 680, near Exit 40, California",
    "WeatherConditions": "Clear and sunny",
    "CauseOfDamage": "Flying pebble hit the windshield",
    "ExtentOfDamage": "4-inch crack on the driver'\''s side of windshield",
    "DriverLicenseNumber": "CA987654321",
    "StateOfDriverLicense": "California",
    "InsuranceCompany": "ABC Insurance Company",
    "ContactInformation": "555-123-4567",
    "EmailAddress": "jane.doe@example.com",
    "IncidentDescription": "While driving on Interstate 680 near Exit 40, a pebble was kicked up by a passing vehicle, causing a crack in the windshield.",
    "PoliceReportFiled": "No",
    "PhotosOfDamage": "Yes",
    "RepairOrReplacementNeeded": "Replacement",
    "PreferredRepairShop": "Speedy Auto Glass, 123 Glass Street, Pleasant Hill, CA",
    "DeductibleAmount": "$100",
    "Witnesses": "None",
    "OtherPartiesInvolved": "None"
}'

```

and the response:

```json
{
    "claimNo": "0c3e2998a2dc",
    "message": "Claim submitted and stored successfully"
}
```

get a claim:
```sh
curl --location --request GET 'http://0.0.0.0:8000/get-claim-details/0c3e2998a2dc' \
--header 'Content-Type: application/json' 

```

```json
{"claimNo":"0c3e2998a2dc","Name":"Amelia Bacon","PolicyNumber":"ABCD123456789","VehicleMakeAndModel":"Ford Mustang","VehicleYear":"2022","LicensePlateNumber":"7XYZ123","DateOfIncident":"February 2, 2025","TimeOfIncident":"3:45 PM","LocationOfIncident":"Interstate 680, near Exit 40, California","WeatherConditions":"Clear and sunny","CauseOfDamage":"Flying pebble hit the windshield","ExtentOfDamage":"2-inch crack on the driver's side of windshield","DriverLicenseNumber":"CA9876543111","StateOfDriverLicense":"California","InsuranceCompany":"ABC Insurance Company","ContactInformation":"925-123-4567","EmailAddress":"amelia.bacon@gmail.com","IncidentDescription":"While driving on Interstate 680 near Exit 40, a pebble was kicked up by a passing vehicle, causing a crack in the windshield.","PoliceReportFiled":"No","PhotosOfDamage":"Yes","RepairOrReplacementNeeded":"Replacement","PreferredRepairShop":"Speedy Auto Glass, 123 Glass Street, Pleasant Hill, CA","DeductibleAmount":"$100","Witnesses":"None","OtherPartiesInvolved":"None"}
```


and get all the claims:
```sh
curl --location --request GET 'http://0.0.0.0:8000/get-claims' \
--header 'Content-Type: application/json' 
```



```json
{
    "claimNos": [
        "69a4332610bd",
        "0c3e2998a2dc"
    ]
}
```