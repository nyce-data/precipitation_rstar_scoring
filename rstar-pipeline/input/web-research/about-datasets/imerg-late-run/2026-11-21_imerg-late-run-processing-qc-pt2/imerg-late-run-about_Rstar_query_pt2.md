# About IMERG Late Run Part 2 R* Query for Claude

About dataset = IMERG Late Run

## Query to refine

Perform a web query where you find out about the  dataset” as an overview.

Research information about the IMERG Late Run (Integrated Multi-satellitE Retrievals for GPM) dataset.

## ChatGPT query

Research how the IMERG Late Run dataset is created and processed, including the algorithms, computational methods, and direct measurements involved in producing the dataset. Explain how multiple satellite observations and other incorporated data sources are combined, calibrated, or integrated to generate the final product. Does the dataset undergo quality control (QC), and, if so, what specific methods, procedures, and criteria are used to determine data quality? Is specialized software used to perform QC, and is this work conducted by the group collecting the measurements, the group processing the data, or an independent organization? Identify the software, algorithms, and technical documentation used for these procedures.

## Claude web research skill query

/my:broad-web-research

How is the IMERG Late Run (Integrated Multi-satellitE Retrievals for GPM, Late Run) dataset produced and quality-controlled? Using the earlier run's record on what IMERG Late Run is and what it is made from (in web_search_results/), cover the current version of the Late Run, and say where its processing differs from the Early and Final Runs.

- **Processing:** the steps from satellite observations to the gridded product, and how the sources are combined, calibrated or merged. Check for these steps without assuming each is used as named: microwave retrievals (such as GPROF), intercalibration of the sensors to a common reference, infrared estimates (such as PERSIANN-CCS), morphing and Kalman filtering to fill gaps between satellite passes, and gauge or climatological adjustment. Name each algorithm and the software that runs it, and say which steps use direct measurements and which are computed.
- **Quality control:** whether QC is done; the checks, one line each; whether automated, manual or both; how suspect values are flagged or handled (check for quality-index, error and flag fields in the files, without assuming any is present); and who does it: the instrument teams, the processing system, the IMERG team or an independent group (such as a ground-validation program). Include QC done on inputs before they are used, and validation against gauges or ground radar.
- **Documentation:** the algorithm description documents, technical documents and release notes that describe these steps, with links.

Say where something is not published. Use NASA's and the IMERG team's documentation and the developers' papers ahead of secondary accounts. File formats and whether the code is public are a separate question. With a time limit of 30 minutes and a token ceiling of 240,000.

## Claude comments about the rewritten query

**What you'll get:** the chain of steps that turns satellite observations into IMERG Late Run, with each algorithm and the software behind it; what quality control is done, by whom, and how it shows up in the files; and links to the documents that describe it. Expect a standard-tier run.

**What I changed from your draft:**
- **Built on Part 1:** Part 1 lists the inputs; this run starts from its record and spends its time on how they are combined and checked.
- **Steps as candidates:** IMERG's processing has well-known stages (microwave retrievals, intercalibration, infrared estimates, morphing between satellite passes, gauge adjustment). The question lists them so the run checks each, and says "without assuming each is used as named" because the details change between versions.
- **Late Run differences:** the Late Run can't use the monthly gauge analyses the Final Run uses, so its gauge step differs; the question asks the run to say so where it applies.
- **QC in a merged product:** a satellite product may have little QC of its own beyond checks on its inputs, quality fields in the files and validation. The question asks for those, and who does each, so "no separate QC step" isn't read as "no QC". "Who does it" covers your draft's collecting group, processing group or independent organization.
- **Formats and code availability left to Part 3,** which your Part 3 draft asks about. This run names the software; Part 3 says whether its code is public.
- **Limits:** 30 minutes and 240,000 tokens suit a standard run.

**Order and reuse:** run this after Part 1, in this project. Part 3 uses its record for the list of software to check for public code.
