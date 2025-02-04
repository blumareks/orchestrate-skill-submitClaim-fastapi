from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import uuid
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve the database configuration from the environment
URI = os.getenv("URL")


# Database Configuration
DATABASE_URL = os.getenv("URL", "postgresql://user:password@localhost/insurance_claims")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()

# Claim Model
class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)
    claim_no = Column(String(20), unique=True, nullable=False)
    name = Column(String, nullable=False)
    policy_number = Column(String, nullable=False)
    vehicle_make_model = Column(String, nullable=False)
    vehicle_year = Column(String, nullable=False)
    license_plate = Column(String, nullable=False)
    date_of_incident = Column(String, nullable=False)
    time_of_incident = Column(String, nullable=False)
    location_of_incident = Column(String, nullable=False)
    weather_conditions = Column(String, nullable=False)
    cause_of_damage = Column(String, nullable=False)
    extent_of_damage = Column(String, nullable=False)
    driver_license_number = Column(String, nullable=False)
    state_of_driver_license = Column(String, nullable=False)
    insurance_company = Column(String, nullable=False)
    contact_information = Column(String, nullable=False)
    email_address = Column(String, nullable=False)
    incident_description = Column(String, nullable=False)
    police_report_filed = Column(String, nullable=False)
    photos_of_damage = Column(String, nullable=False)
    repair_or_replacement_needed = Column(String, nullable=False)
    preferred_repair_shop = Column(String, nullable=False)
    deductible_amount = Column(String, nullable=False)
    witnesses = Column(String, nullable=False)
    other_parties_involved = Column(String, nullable=False)

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1️⃣ Submit Claim - Stores claim details in DB
@app.post("/submit-claim")
async def submit_claim(claim: dict, db: Session = Depends(get_db)):
    claim_no = f"{uuid.uuid4().hex[:12]}"  # Generate unique claim number

    new_claim = Claim(
        claim_no=claim_no,
        name=claim["Name"],
        policy_number=claim["PolicyNumber"],
        vehicle_make_model=claim["VehicleMakeAndModel"],
        vehicle_year=claim["VehicleYear"],
        license_plate=claim["LicensePlateNumber"],
        date_of_incident=claim["DateOfIncident"],
        time_of_incident=claim["TimeOfIncident"],
        location_of_incident=claim["LocationOfIncident"],
        weather_conditions=claim["WeatherConditions"],
        cause_of_damage=claim["CauseOfDamage"],
        extent_of_damage=claim["ExtentOfDamage"],
        driver_license_number=claim["DriverLicenseNumber"],
        state_of_driver_license=claim["StateOfDriverLicense"],
        insurance_company=claim["InsuranceCompany"],
        contact_information=claim["ContactInformation"],
        email_address=claim["EmailAddress"],
        incident_description=claim["IncidentDescription"],
        police_report_filed=claim["PoliceReportFiled"],
        photos_of_damage=claim["PhotosOfDamage"],
        repair_or_replacement_needed=claim["RepairOrReplacementNeeded"],
        preferred_repair_shop=claim["PreferredRepairShop"],
        deductible_amount=claim["DeductibleAmount"],
        witnesses=claim["Witnesses"],
        other_parties_involved=claim["OtherPartiesInvolved"]
    )

    db.add(new_claim)
    db.commit()
    db.refresh(new_claim)

    return {"claimNo": claim_no, "message": "Claim submitted and stored successfully"}

# 2️⃣ Get Claim Details by claimNo
@app.get("/get-claim-details/{claim_no}")
async def get_claim_details(claim_no: str, db: Session = Depends(get_db)):
    claim = db.query(Claim).filter(Claim.claim_no == claim_no).first()
    
    if not claim:
        raise HTTPException(status_code=404, detail="Claim not found")
    
    return {
        "claimNo": claim.claim_no,
        "Name": claim.name,
        "PolicyNumber": claim.policy_number,
        "VehicleMakeAndModel": claim.vehicle_make_model,
        "VehicleYear": claim.vehicle_year,
        "LicensePlateNumber": claim.license_plate,
        "DateOfIncident": claim.date_of_incident,
        "TimeOfIncident": claim.time_of_incident,
        "LocationOfIncident": claim.location_of_incident,
        "WeatherConditions": claim.weather_conditions,
        "CauseOfDamage": claim.cause_of_damage,
        "ExtentOfDamage": claim.extent_of_damage,
        "DriverLicenseNumber": claim.driver_license_number,
        "StateOfDriverLicense": claim.state_of_driver_license,
        "InsuranceCompany": claim.insurance_company,
        "ContactInformation": claim.contact_information,
        "EmailAddress": claim.email_address,
        "IncidentDescription": claim.incident_description,
        "PoliceReportFiled": claim.police_report_filed,
        "PhotosOfDamage": claim.photos_of_damage,
        "RepairOrReplacementNeeded": claim.repair_or_replacement_needed,
        "PreferredRepairShop": claim.preferred_repair_shop,
        "DeductibleAmount": claim.deductible_amount,
        "Witnesses": claim.witnesses,
        "OtherPartiesInvolved": claim.other_parties_involved
    }

# 3️⃣ Get All Claim Numbers
@app.get("/get-claims")
async def get_claims(db: Session = Depends(get_db)):
    claims = db.query(Claim.claim_no).all()
    
    if not claims:
        raise HTTPException(status_code=404, detail="No claims found")
    
    return {"claimNos": [claim.claim_no for claim in claims]}
