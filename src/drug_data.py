from typing import NamedTuple
from datetime import datetime

class DrugData(NamedTuple):
    drug_name: str
    dosage: int  # mg
    route: str
    frequency: str  # e.g., 8h, 12h, qd
    age_min: int  # months
    age_max: int  # months

    def __str__(self):
        return (f'Drug: {self.drug_name}
Dosage: {self.dosage} mg
Route: {self.route}
Frequency: {self.frequency}
Age Range: {self.age_min}-{self.age_max} months')
