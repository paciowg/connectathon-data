import glob
import json
from io import BytesIO
from zipfile import ZipFile
from tempfile import mkdtemp

import requests

# base_url = "https://api.logicahealth.org/PACIO/open"
# base_url = "https://impact-fhir.mitre.org/r4"
base_url = "http://hapi.fhir.org/baseR4"


def upload_resource(data):
    resource_url = f"{base_url}/{data['resourceType']}/{data['id']}"

    print(resource_url)

    try:
        resp = requests.put(resource_url, json=data)
        resp.raise_for_status()
    except requests.exceptions.HTTPError:
        print(resp.json())


def load_implementation_guide(url, files):
    tempdir = mkdtemp()

    resp = requests.get(url, stream=True)
    with ZipFile(BytesIO(resp.content)) as zf:
        zf.extractall(tempdir)

    for filename in files:
        data = json.load(open(f"{tempdir}/{filename}"))
        upload_resource(data)


if __name__ == "__main__":
    # load cognitive status ig
    load_implementation_guide(
        "https://paciowg.github.io/cognitive-status-ig/definitions.json.zip",
        [
            "StructureDefinition-pacio-cs-BundledCognitiveStatus.json",
            "StructureDefinition-pacio-cs-CognitiveStatus.json",
        ],
    )

    # load functional status ig
    load_implementation_guide(
        "https://paciowg.github.io/functional-status-ig/definitions.json.zip",
        [
            "StructureDefinition-pacio-fs-BundledFunctionalStatus.json",
            "StructureDefinition-pacio-fs-FunctionalStatus.json",
        ],
    )

    # load other resources
    # these need to load in a certain order.

    for prefix in ["Patient", "Medication", "MedicationRequest", "Practitioner", "Observation"]:
        for filename in glob.glob(f"./json/{prefix}-*.json"):
            upload_resource(json.load(open(filename)))

