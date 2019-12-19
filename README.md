# CMS Connecthon Data

This repository contains FHIR resources for Cognitive Status and Functional Status that will be used
during the CMS Connectathon.

All resources are located in the `json/` directory.

## Server

All the resources found in this repository have also been loaded to the HAPI FHIR sandbox:

http://hapi.fhir.org/baseR4/

To search for observations based on Functional Status profile:

http://hapi.fhir.org/baseR4/Observation?_profile=http://hl7.org/fhir/us/PACIO-functional-cognitive-status/StructureDefinition/pacio-fs-FunctionalStatus

To search for observations based on Cognitive Status profile:

http://hapi.fhir.org/baseR4/Observation?_profile=http://hl7.org/fhir/us/PACIO-functional-cognitive-status/StructureDefinition/pacio-cs-CognitiveStatus

## Profiles

The profiles are not included in this repository.
You can find the profiles for Cognitive Status and Functional Status in their respective Implementation Guides:

https://paciowg.github.io/cognitive-status-ig/

https://paciowg.github.io/functional-status-ig/

## Resource List

This is the full list of resources available on the demo server:

### Structure Defintions

http://hapi.fhir.org/baseR4/StructureDefinition/pacio-cs-BundledCognitiveStatus<br>
http://hapi.fhir.org/baseR4/StructureDefinition/pacio-cs-CognitiveStatus

http://hapi.fhir.org/baseR4/StructureDefinition/pacio-fs-BundledFunctionalStatus<br>
http://hapi.fhir.org/baseR4/StructureDefinition/pacio-fs-FunctionalStatus

### Supporting Resources

http://hapi.fhir.org/baseR4/Patient/cms-patient-01

http://hapi.fhir.org/baseR4/Medication/cms-med-01<br>
http://hapi.fhir.org/baseR4/Medication/cms-med-02<br>
http://hapi.fhir.org/baseR4/Medication/cms-med-03<br>
http://hapi.fhir.org/baseR4/Medication/cms-med-04<br>
http://hapi.fhir.org/baseR4/Medication/cms-med-05<br>
http://hapi.fhir.org/baseR4/Medication/cms-med-06<br>
http://hapi.fhir.org/baseR4/Medication/cms-med-07<br>
http://hapi.fhir.org/baseR4/Medication/cms-med-08<br>
http://hapi.fhir.org/baseR4/Medication/cms-med-09<br>
http://hapi.fhir.org/baseR4/Medication/cms-med-10

http://hapi.fhir.org/baseR4/MedicationRequest/cms-medrequest-01<br>
http://hapi.fhir.org/baseR4/MedicationRequest/cms-medrequest-02<br>
http://hapi.fhir.org/baseR4/MedicationRequest/cms-medrequest-03<br>
http://hapi.fhir.org/baseR4/MedicationRequest/cms-medrequest-04<br>
http://hapi.fhir.org/baseR4/MedicationRequest/cms-medrequest-05<br>
http://hapi.fhir.org/baseR4/MedicationRequest/cms-medrequest-06<br>
http://hapi.fhir.org/baseR4/MedicationRequest/cms-medrequest-07<br>
http://hapi.fhir.org/baseR4/MedicationRequest/cms-medrequest-08<br>
http://hapi.fhir.org/baseR4/MedicationRequest/cms-medrequest-09<br>
http://hapi.fhir.org/baseR4/MedicationRequest/cms-medrequest-10

http://hapi.fhir.org/baseR4/Practitioner/cms-practitioner-01<br>
http://hapi.fhir.org/baseR4/Practitioner/cms-practitioner-02<br>
http://hapi.fhir.org/baseR4/Practitioner/cms-practitioner-03<br>
http://hapi.fhir.org/baseR4/Practitioner/cms-practitioner-04<br>
http://hapi.fhir.org/baseR4/Practitioner/cms-practitioner-05<br>
http://hapi.fhir.org/baseR4/Practitioner/cms-practitioner-06<br>
http://hapi.fhir.org/baseR4/Practitioner/cms-practitioner-07<br>
http://hapi.fhir.org/baseR4/Practitioner/cms-practitioner-08

### Cognitive Status Observations

coming soon

### Functional Status Observations

coming soon
