# OS Schools research template

After starting a new project from this template:

* Update the project details in `pyproject.toml`.
* Update the title of this document with the name of the repo.
* Update _Description_ belo with a brief description so that a member of the public viewing this repository could understand, at a high level, what the goals of this specific piece of analysis are.  (It may make sense to edit this as your project progresses).
* Update _Instructions to run this code_ with instructions for running your code.  (Again, it may make sense to edit this as your project progresses).
* Remove these instructions.

## Project overview

This code is being developed for the [Teaching Improvement through Data and Evaluation (TIDE) project](https://niot.org.uk/research-projects/teacher_improvement_through_data_evaluation_tide).
It is being developed locally using [synthetic data](https://github.com/bennettoxford/os-schools-data/tree/main/synthetic-data) before being run against real data in the [Teacher Education Dataset (TED)](https://niot.org.uk/research-projects/teacher_education_dataset).
To ensure public transparency, all requests to run research code against the TED dataset can be found [here](https://github.com/bennettoxford/os-schools-requests/issues?q=label%3Arun-request),
and all requests to share the outputs can be found [here](https://github.com/bennettoxford/os-schools-requests/issues?q=label%3Ashare-request).

## Description

_To be updated by the project owner._

## Instructions to run this code

_To be updated by the project owner.  These instructions describe how to run the sample script in the analysis/ directory._

To run this code, install [uv](https://docs.astral.sh/uv/guides/tools/), and run:

    uv run analysis/01_count_rows.py
