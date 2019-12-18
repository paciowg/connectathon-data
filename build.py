import json

medications = [
    {
        "name": "Lisinopril 10 mg ",
        "subscr": "Take twice a day",
        "code": "314076",
        "codename": "Lisinopril 10 MG Oral Tablet",
    },
    {
        "name": "Atorvastatin 40mg",
        "subscr": "Take nightly",
        "code": "617311",
        "codename": "Atorvastatin 40 MG Oral Tablet  ",
    },
    {
        "name": "Calcium 500mg",
        "subscr": "Take daily",
        "code": "318076",
        "codename": "Calcium Carbonate 500 MG Oral Tablet  ",
    },
    {
        "name": "Vitamin D 400IU ",
        "subscr": "Take 2 tabs daily",
        "code": "316901",
        "codename": "Vitamin D 400 UNT  ",
    },
    {
        "name": "Furosemide 20mg ",
        "subscr": "Take daily",
        "code": "310429",
        "codename": "Furosemide 20 MG Oral Tablet",
    },
    {
        "name": "Ferrous Sulfate 325mg",
        "subscr": "Take three times a day prior to meals",
        "code": "310325",
        "codename": "Ferrous sulfate 325 MG Oral Tablet ",
    },
    {
        "name": "Glargine 24 units",
        "subscr": "Take 0.24 ml SQ nightly",
        "code": "343226",
        "codename": "Insulin Glargine  100u/ML",
    },
    {
        "name": "Insulin 3 units",
        "subscr": " Take 3 ml  with each meal",
        "code": "2179742",
        "codename": "Insulin, regular, human 1 UNT/ML ",
    },
    {
        "name": "Sertraline 25mg",
        "subscr": "Take nightly",
        "code": "312940",
        "codename": "Sertraline 25 MG Oral Tablet  ",
    },
    {
        "name": "Tylenol 650mg",
        "subscr": "Take very 6 hours or as needed",
        "code": "313782",
        "codename": "Acetaminophen 325 MG Oral Tablet",
    },
]

practitioners = [
    {"name": "Primary Care Physician"},
    {"name": "Endocrinologist"},
    {"name": "Psychiatrist"},
    {"name": "Retail Pharmacy"},
    {"name": "Cardiologist"},
    {"name": "Nephrologist"},
    {"name": "Opthamologist"},
    {"name": "Lab Services"},
]


def build_medications():
    for index, medication in enumerate(medications, 1):
        patient_id = "cms-patient-01"
        medication_id = f"cms-med-{index:02}"
        request_id = f"cms-medrequest-{index:02}"

        output_medication = {
            "resourceType": "Medication",
            "text": {
                "status": "generated",
                "div": f"<div xmlns='http://www.w3.org/1999/xhtml'>Medication: {medication['name']}</div>",
            },
            "id": medication_id,
            "status": "active",
            "ingredient": [
                {
                    "itemCodeableConcept": {
                        "coding": [
                            {
                                "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
                                "code": medication["code"],
                                "display": medication["codename"],
                            }
                        ]
                    }
                }
            ],
        }

        output_request = {
            "resourceType": "MedicationRequest",
            "text": {
                "status": "generated",
                "div": f"<div xmlns='http://www.w3.org/1999/xhtml'>MedicationRequest: {medication['name']}</div>",
            },
            "id": request_id,
            "status": "active",
            "intent": "order",
            "medicationReference": {"reference": f"Medication/{medication_id}",},
            "subject": {"reference": f"Patient/{patient_id}"},
        }

        json.dump(
            output_medication,
            open(f"./json/Medication-{medication_id}.json", "w"),
            indent=2,
        )

        json.dump(
            output_request,
            open(f"./json/MedicationRequest-{request_id}.json", "w"),
            indent=2,
        )


def build_practitioners():
    for index, practitioner in enumerate(practitioners, 1):
        practitioner_id = f"cms-practitioner-{index:02}"

        output = {
            "resourceType": "Practitioner",
            "text": {
                "status": "generated",
                "div": f"<div xmlns='http://www.w3.org/1999/xhtml'>Practitioner: {practitioner['name']}</div>",
            },
            "id": practitioner_id,
            "active": True,
            "name": [{"given": ["Sample"], "family": practitioner["name"]}],
        }

        json.dump(
            output, open(f"./json/Practitioner-{practitioner_id}.json", "w"), indent=2,
        )


if __name__ == "__main__":
    build_medications()
    build_practitioners()
