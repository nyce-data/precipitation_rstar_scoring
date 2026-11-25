# DIRS: Dependent infrastructure resilience

## Dependent infrastructure resilience defined

The invisible dependency layer — external infrastructure that datasets depend on but don’t control: calibration facilities, satellite ground stations, field observation networks, specialized instrumentation labs. When NOAA’s Global Monitoring Laboratory calibration services were threatened, every dataset whose quality assurance depends on those standards became more fragile immediately, regardless of its own hosting situation.

DIRS covers what this dataset needs in order to be produced: the instruments and observing networks that make its measurements, the calibration of those instruments, the data feeds it is built from, and the processing that turns them into the dataset. It does not cover where the finished dataset is stored or served. The repository's storage, hosting, access and funding belong to D-2, D-3 and RRS. Count a repository or agency fact here only when a source ties it to this dataset's inputs or processing.

## Subcategories

### DIRS-1

#### Description

Calibration facility dependency

Dataset quality or continuity depends on an external calibration service, reference standard lab, or inter-comparison program that could be disrupted

#### How to find

List the instruments whose measurements reach this dataset (for a compilation, those of each contributing network). Find who calibrates them and against what standard: a national standards lab, a manufacturer, a field support centre, a WMO instrument centre, or a reference sensor (for example GMI for satellite products). Is that calibration done by the group that takes the measurements, or by an outside service that could be cut?

#### What counts as evidence

The instruments whose measurements go into the dataset, who calibrates them and against what standard (a national standards lab, the manufacturer, a field support centre, a WMO instrument centre or a reference satellite sensor), and whether that calibration is done in-house or by an outside service that could be cut.

### DIRS-2

#### Description

Observation network or sensor platform at risk

Upstream sensors, ground stations, buoys, or satellite instruments that feed this dataset are aging out, losing funding, or operating past design life

#### How to find

From the dataset's own documentation (source flags, input lists), list the networks, stations and satellite instruments that feed it, and how much each supplies. For each, look for end-of-life dates, funding cuts, closures or staff losses that would stop or thin its observations.

#### What counts as evidence

The networks, stations and satellite instruments that feed the dataset and how much each supplies, plus any end-of-life dates, funding cuts, closures or staff losses that would stop or thin out their observations.

### DIRS-3

#### Description

Upstream data supply chain at risk

Dataset depends on external data feeds (reanalysis inputs, ancillary fields, reference datasets) that are themselves vulnerable to disruption

#### How to find

Find every other dataset or feed this dataset is built from or processed with (source compilations, reanalysis or model fields, ancillary or reference data), and the route each arrives by (for example WMO exchange or an agency feed). Is any of them stopping, changing or delayed?

#### What counts as evidence

The other datasets and data feeds this one is built from or processed with (source compilations, model or reanalysis fields, reference data), how each one arrives, and whether any of them is stopping, changing or running late.

### DIRS-4

#### Description

External processing infrastructure dependency

Specialized computing, software, or lab facilities not controlled by the data steward are required to produce or update this dataset

#### How to find

Find who processes and quality-controls this dataset, and on what systems. Is it done by the producer on its own systems, or does it rely on outside groups, contracted or commercial computing, or third-party software? The repository's general IT and cloud moves count only if a source says this dataset's processing moves with them.

#### What counts as evidence

Who processes and quality-controls the dataset, and on what systems: the producer's own, or outside groups, contracted or commercial computing, or third-party software. The repository's general IT or cloud moves count only when a source says this dataset's processing moves with them.

### DIRS-5

#### Description

No alternative supplier

If the primary external dependency fails, no backup source, workaround, or substitute exists to maintain data quality or continuity

#### How to find

For each dependency found under DIRS-1 to DIRS-4, look for a backup: a second source, a successor instrument or mission, a substitute feed, or the dataset's own fallback (such as a source priority). Also look for other datasets that could stand in for this one if it stopped, and say how much of it each could replace (region, period, update rate, quality control).

#### What counts as evidence

A backup for each dependency in DIRS-1 to DIRS-4: a second source, a successor instrument or mission, a substitute feed, or the dataset's own fallback. Also other datasets that could stand in for this one if it stopped, and how much of it each could replace.
