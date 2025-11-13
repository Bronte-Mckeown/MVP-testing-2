# MVP Testing Round 2

## Project overview

This code is being developed for the [Teaching Improvement through Data and Evaluation (TIDE) project](https://niot.org.uk/research-projects/teacher_improvement_through_data_evaluation_tide).
It is being developed locally using [synthetic data](https://github.com/bennettoxford/os-schools-data/tree/main/synthetic-data) before being run against real data in the [Teacher Education Dataset (TED)](https://niot.org.uk/research-projects/teacher_education_dataset).
To ensure public transparency, all requests to run research code against the TED dataset can be found [here](https://github.com/bennettoxford/os-schools-requests/issues?q=label%3Arun-request),
and all requests to share the outputs can be found [here](https://github.com/bennettoxford/os-schools-requests/issues?q=label%3Ashare-request).

## Description

This analysis code is used to assess the MMVP version of OS-Schools. It correlates English Lit and Maths KS4 current grade scores in 1 school.

## Instructions to run this code

To run this code, open your Windows Powershell and run:

    python3 analysis\01_correlate_maths_english.py

These instructions assume you have python3 installed. It will first install pandas if you don't have it installed and then it should run.
