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

pip freeze | grep -E 'fastapi|uvicorn|pydantic' > requirements.txt





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
{"message":"Claim submitted successfully","claimNo":"20250203testclaim01","recommended_repair_shops":[{"Name":"Speedy Auto Glass","Address":"123 Glass Street, Pleasant Hill, CA","Phone":"555-987-6543","Email":"contact@speedyautoglass.com"},{"Name":"Clear View Glass Repair","Address":"456 Window Ave, Concord, CA","Phone":"555-876-5432","Email":"info@clearviewglass.com"},{"Name":"Precision Auto Glass","Address":"789 Shield Blvd, Walnut Creek, CA","Phone":"555-765-4321","Email":"service@precisionautoglass.com"},{"Name":"Safe Drive Glass Solutions","Address":"101 Windshield Rd, Oakland, CA","Phone":"555-654-3210","Email":"support@safedriveglass.com"},{"Name":"AutoGlass Experts","Address":"202 CrackFix Ln, San Francisco, CA","Phone":"555-543-2109","Email":"help@autoglassexperts.com"}]}
```

