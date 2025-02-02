from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class QueryRequest(BaseModel):
    RAG: str

class ClaimRequest(BaseModel):
    Name: str
    PolicyNumber: str
    VehicleMakeAndModel: str
    VehicleYear: str
    LicensePlateNumber: str
    DateOfIncident: str
    TimeOfIncident: str
    LocationOfIncident: str
    WeatherConditions: str
    CauseOfDamage: str
    ExtentOfDamage: str
    DriverLicenseNumber: str
    StateOfDriverLicense: str
    InsuranceCompany: str
    ContactInformation: str
    EmailAddress: str
    IncidentDescription: str
    PoliceReportFiled: str
    PhotosOfDamage: str
    RepairOrReplacementNeeded: str
    PreferredRepairShop: str
    DeductibleAmount: str
    Witnesses: str
    OtherPartiesInvolved: str

insurance_claim_response = {
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
    "ExtentOfDamage": "4-inch crack on the driver's side of windshield",
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
}

repair_shops = [
    {"Name": "Speedy Auto Glass", "Address": "123 Glass Street, Pleasant Hill, CA", "Phone": "555-987-6543", "Email": "contact@speedyautoglass.com"},
    {"Name": "Clear View Glass Repair", "Address": "456 Window Ave, Concord, CA", "Phone": "555-876-5432", "Email": "info@clearviewglass.com"},
    {"Name": "Precision Auto Glass", "Address": "789 Shield Blvd, Walnut Creek, CA", "Phone": "555-765-4321", "Email": "service@precisionautoglass.com"},
    {"Name": "Safe Drive Glass Solutions", "Address": "101 Windshield Rd, Oakland, CA", "Phone": "555-654-3210", "Email": "support@safedriveglass.com"},
    {"Name": "AutoGlass Experts", "Address": "202 CrackFix Ln, San Francisco, CA", "Phone": "555-543-2109", "Email": "help@autoglassexperts.com"}
]

new_claim_no = "20250203testclaim01"

@app.post("/query")
def get_insurance_claim_details(request: QueryRequest):
    if request.RAG == "insuranceClaimData":
        return insurance_claim_response
    else:
        raise HTTPException(status_code=400, detail="Invalid request")

@app.post("/submit-claim")
def submit_insurance_claim(claim: ClaimRequest):
    return {"message": "Claim submitted successfully", "claimNo": new_claim_no, "recommended_repair_shops": repair_shops}

# Run the application using: uvicorn script_name:app --host 0.0.0.0 --port 8000
