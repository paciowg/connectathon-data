from datetime import datetime
import csv
import json


def format_date(value):
    newdate = None
    try:
        newdate = datetime.strptime(value, "%m/%d/%y %I:%M %p")
    except ValueError:
        newdate = datetime.strptime(value, "%m/%d/%y %H:%M")

    return newdate.strftime("%Y-%m-%dT%H:%M:%S+00:00")


def build_cognitive(observations):
    patient_id = "cms-patient-01"

    for index, observation in enumerate(observations, 1):
        observation_id = f"cms-cognitive-{index:02}"

        output = {
            "resourceType": "Observation",
            "text": {
                "status": "generated",
                "div": "<div xmlns='http://www.w3.org/1999/xhtml'>"
                f"<p>Cognitive Status Observation: {observation['event']}</p><p>{observation['question']}</p>"
                "</div>",
            },
            "meta": {
                "profile": "http://hl7.org/fhir/us/PACIO-functional-cognitive-status/StructureDefinition/pacio-cs-CognitiveStatus"
            },
            "id": observation_id,
            "status": "final",
            "code": {
                "coding": [
                    {"system": "http://loinc.org", "code": observation["questionLoinc"]}
                ],
                "text": observation["question"],
            },
            "subject": {"reference": f"Patient/{patient_id}"},
            "effectiveDateTime": format_date(observation["date"]),
            "valueCodeableConcept": {
                "coding": [
                    {"system": "http://loinc.org", "code": observation["answerLoinc"]}
                ],
                "text": observation["answer"],
            },
        }

        json.dump(
            output, open(f"./json/Observation-{observation_id}.json", "w"), indent=2,
        )


def build_functional(observations):
    patient_id = "cms-patient-01"

    for index, observation in enumerate(observations, 1):
        observation_id = f"cms-functional-{index:02}"

        output = {
            "resourceType": "Observation",
            "text": {
                "status": "generated",
                "div": "<div xmlns='http://www.w3.org/1999/xhtml'>"
                f"<p>Functional Status Observation: {observation['event']}</p><p>{observation['question']}</p>"
                "</div>",
            },
            "meta": {
                "profile": "http://hl7.org/fhir/us/PACIO-functional-cognitive-status/StructureDefinition/pacio-fs-FunctionalStatus"
            },
            "id": observation_id,
            "status": "final",
            "code": {
                "coding": [
                    {"system": "http://loinc.org", "code": observation["questionLoinc"]}
                ],
                "text": observation["question"],
            },
            "subject": {"reference": f"Patient/{patient_id}"},
            "effectiveDateTime": format_date(observation["date"]),
            "valueCodeableConcept": {
                "coding": [
                    {"system": "http://loinc.org", "code": observation["answerLoinc"]}
                ],
                "text": observation["answer"],
            },
        }

        json.dump(
            output, open(f"./json/Observation-{observation_id}.json", "w"), indent=2,
        )


if __name__ == "__main__":

    with open("./obs-cognitive.csv") as handle:
        observations = list(csv.DictReader(handle))
        build_cognitive(observations)

    with open("./obs-functional.csv") as handle:
        observations = list(csv.DictReader(handle))
        build_functional(observations)
