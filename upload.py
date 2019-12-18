import json
from io import BytesIO
from zipfile import ZipFile
from tempfile import mkdtemp

import requests

base_url = "https://api.logicahealth.org/PACIO/open"
# base_url = "https://impact-fhir.mitre.org/r4"

resources = [
    "Patient-cms-patient-01.json",
    "Medication-cms-med-01.json",
    "Medication-cms-med-02.json",
    "Medication-cms-med-03.json",
    "Medication-cms-med-04.json",
    "Medication-cms-med-05.json",
    "Medication-cms-med-06.json",
    "Medication-cms-med-07.json",
    "Medication-cms-med-08.json",
    "Medication-cms-med-09.json",
    "Medication-cms-med-10.json",
    "MedicationRequest-cms-medrequest-01.json",
    "MedicationRequest-cms-medrequest-02.json",
    "MedicationRequest-cms-medrequest-03.json",
    "MedicationRequest-cms-medrequest-04.json",
    "MedicationRequest-cms-medrequest-05.json",
    "MedicationRequest-cms-medrequest-06.json",
    "MedicationRequest-cms-medrequest-07.json",
    "MedicationRequest-cms-medrequest-08.json",
    "MedicationRequest-cms-medrequest-09.json",
    "MedicationRequest-cms-medrequest-10.json",
    "Practitioner-cms-practitioner-01.json",
    "Practitioner-cms-practitioner-02.json",
    "Practitioner-cms-practitioner-03.json",
    "Practitioner-cms-practitioner-04.json",
    "Practitioner-cms-practitioner-05.json",
    "Practitioner-cms-practitioner-06.json",
    "Practitioner-cms-practitioner-07.json",
    "Practitioner-cms-practitioner-08.json",
]


def upload_resource(data):
    resource_url = f"{base_url}/{data['resourceType']}/{data['id']}"

    print(resource_url)

    try:
        resp = requests.put(resource_url, json=data)
        resp.raise_for_status()
    except Exception:
        print(resp.json())


def load_implementation_guide(url, files):
    tempdir = mkdtemp()

    resp = requests.get(url, stream=True)
    zf = ZipFile(BytesIO(resp.content))
    zf.extractall(tempdir)

    for filename in files:
        data = json.load(open(f"{tempdir}/{filename}"))
        upload_resource(data)


if __name__ == "__main__":
    # load cognitive status ig
    # load_implementation_guide(
    #     "https://paciowg.github.io/cognitive-status-ig/definitions.json.zip",
    #     [
    #         "StructureDefinition-pacio-cs-BundledCognitiveStatus.json",
    #         "StructureDefinition-pacio-cs-CognitiveStatus.json",
    #     ],
    # )

    # # load functional status ig
    # load_implementation_guide(
    #     "https://paciowg.github.io/functional-status-ig/definitions.json.zip",
    #     [
    #         "StructureDefinition-pacio-fs-BundledFunctionalStatus.json",
    #         "StructureDefinition-pacio-fs-FunctionalStatus.json",
    #     ],
    # )

    # load other resources
    for filename in resources:
        data = json.load(open(f"./json/{filename}"))
        upload_resource(data)
