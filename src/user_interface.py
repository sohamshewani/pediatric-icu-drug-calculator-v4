from typing import Optional
from src.drug_data import DrugData
from src.dosage_calculator import calculate_dosage, validate_dosage
from src.safety_validator import validate_drug_interaction
from src.safety_validator import Interaction
from src.safety_validator import show_error_message
from src.safety_validator import show_dosage_result

from datetime import datetime
from typing import Optional
from src.drug_data import DrugData
from src.dosage_calculator import calculate_dosage
from src.safety_validator import validate_drug_interaction
from src.user_interface import show_error_message
from src.user_interface import show_dosage_result

from typing import List
from src.drug_data import DrugData


def main() -> None:
    print('Welcome to Pediatric ICU Drug Calculator')
    print('Please enter drug data')
    drug_name = input('Drug Name: ').strip()
    dosage = int(input('Dosage (mg): ').strip())
    route = input('Route: ').strip()
    frequency = input('Frequency: ').strip()
    age_min = int(input('Age Min (months): ').strip())
    age_max = int(input('Age Max (months): ').strip())

    drug = DrugData(drug_name, dosage, route, frequency, age_min, age_max)

    print('Drug data entered successfully')
    print('Please enter patient data')
    patient_age = int(input('Patient Age (months): ').strip())

    calculated_dosage = calculate_dosage(drug, patient_age)
    if calculated_dosage is None:
        show_error_message('Patient age is out of the drug’s age range')
    else:
        if not validate_drug_interaction(drug, drug):
            show_error_message('Drug interaction detected')
        else:
            show_dosage_result(drug, calculated_dosage)
