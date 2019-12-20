# CMS Connecthon Data

This repository contains FHIR resources for Cognitive Status and Functional Status that will be used
during the CMS Connectathon.

All resources are located in the `json/` directory.

## Server

All the resources found in this repository have also been loaded to the HAPI FHIR sandbox:

http://hapi.fhir.org/baseR4/

There are many other resources on this server besides our sample data.
This README will help identify which resources are part of our sample data.

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

These observations correspond to the Cognitive Status observations in Observations.xlsx

http://hapi.fhir.org/baseR4/Observation/cms-cognitive-01<br>
http://hapi.fhir.org/baseR4/Observation/cms-cognitive-02<br>
http://hapi.fhir.org/baseR4/Observation/cms-cognitive-03<br>
http://hapi.fhir.org/baseR4/Observation/cms-cognitive-04<br>
http://hapi.fhir.org/baseR4/Observation/cms-cognitive-05<br>
http://hapi.fhir.org/baseR4/Observation/cms-cognitive-06<br>
http://hapi.fhir.org/baseR4/Observation/cms-cognitive-07<br>
http://hapi.fhir.org/baseR4/Observation/cms-cognitive-08<br>
http://hapi.fhir.org/baseR4/Observation/cms-cognitive-09<br>
http://hapi.fhir.org/baseR4/Observation/cms-cognitive-10<br>
http://hapi.fhir.org/baseR4/Observation/cms-cognitive-11<br>
http://hapi.fhir.org/baseR4/Observation/cms-cognitive-12

### Functional Status Observations

These observations correspond to the Functional Status observations in Observations.xlsx

http://hapi.fhir.org/baseR4/Observation/cms-functional-01<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-02<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-03<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-04<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-05<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-06<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-07<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-08<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-09<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-10<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-11<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-12<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-13<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-14<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-15<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-16<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-17<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-18<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-19<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-20<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-21<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-22<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-23<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-24<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-25<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-26<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-27<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-28<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-29<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-30<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-31<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-32<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-33<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-34<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-35<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-36<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-37<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-38<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-39<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-40<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-41<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-42<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-43<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-44<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-45<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-46<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-47<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-48<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-49<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-50<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-51<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-52<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-53<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-54<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-55<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-56<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-57<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-58<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-59<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-60<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-61<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-62<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-63<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-64<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-65<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-66<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-67<br>
http://hapi.fhir.org/baseR4/Observation/cms-functional-68
