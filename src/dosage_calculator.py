from typing import Optional
from src.drug_data import DrugData

from datetime import datetime
from typing import Optional
from src.drug_data import DrugData
from src.safety_validator import validate_drug_interaction
from src.user_interface import show_dosage_result

def calculate_dosage(drug: DrugData, patient_age: int) -> Optional[int]:
    # Check if the patient age is within the drug's age range
    if not drug.age_min <= patient_age <= drug.age_max:
        return None

    # Example: Simple dosage calculation based on age
    return drug.dosage


def validate_dosage(drug: DrugData, patient_age: int, calculated_dosage: int) -> bool:
    # Placeholder for interaction validation logic
    return validate_drug_interaction(drug, drug)  # This should be replaced with real interaction logic
