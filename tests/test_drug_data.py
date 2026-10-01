import pytest
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

def test_drug_data_creation(drug_data):
    assert drug_data.drug_name == 'Amoxicillin'
    assert drug_data.dosage == 125
    assert drug_data.route == 'Oral'
    assert drug_data.frequency == '8h'
    assert drug_data.age_min == 2
    assert drug_data.age_max == 12

def test_drug_data_str(drug_data):
    expected_str = ('Drug: Amoxicillin
Dosage: 125 mg
Route: Oral
Frequency: 8h
Age Range: 2-12 months')
    assert str(drug_data) == expected_str
