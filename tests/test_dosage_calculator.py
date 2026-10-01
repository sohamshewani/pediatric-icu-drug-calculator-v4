import pytest
from src.dosage_calculator import calculate_dosage
from src.drug_data import DrugData

@pytest.fixture
def drug_data():
    return DrugData(
        drug_name='Amoxicillin',
        dosage=125,  # mg
        route='Oral',
        frequency='8h',
        age_min=2,  # months
        age_max=12  # months
    )

def test_calculate_dosage(drug_data):
    patient_age = 5  # months
    actual_dosage = calculate_dosage(drug_data, patient_age)
    assert actual_dosage == 125
