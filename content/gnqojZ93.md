# tools/spe_parser · main · Telemetry Solution / Telemetry Solution · GitLab

> 发布时间: 2026-03-18T15:42:19+00:00
> 原文链接: https://gitlab.arm.com/telemetry-solution/telemetry-solution/-/tree/main/tools/spe_parser

---
[**README.md**](/telemetry-solution/telemetry-solution/-/blob/main/tools/spe_parser/README.md)

# spe-parser[](#spe-parser)

The `spe-parser` tool parses SPE (Statistical Profiling Extension) raw data and generates Parquet or CSV files for further processing and analysis.

For guidance on performance analysis with SPE, refer to the [Arm Statistical Profiling Extension: Performance Analysis Methodology White Paper](https://developer.arm.com/documentation/109429/latest/)

For an introduction to Statistical Profiling Extension, refer to the [Arm Architecture Reference Manual for A-profile architecture](https://developer.arm.com/documentation/ddi0487/latest/)

## Installation[](#installation)

Ensure you have the following prerequisites before installing the `spe-parser` tool:

-   pip version 18.0.0 or higher (Use `pip install --upgrade pip` to update pip)
-   python version 3.10 or higher

To install `spe-parser`:

```
pip install .
```

For development mode installation, your pip version should be v21.3 or higher:

```
pip install -e .
```

## Usage[](#usage)

To record SPE performance data:

```
perf record -e arm_spe_0/branch_filter=1,ts_enable=1,load_filter=1,jitter=1,store_filter=1,min_latency=0/ -- test_program
```

For more options and a detailed introduction, please refer to the [Arm Statistical Profiling Extension: Performance Analysis Methodology White Paper](https://developer.arm.com/documentation/109429/latest/)

* * *

To parse the `perf` binary data and output in Parquet format:

```
spe-parser perf.data
```

* * *

To obtain output in CSV format:

```
spe-parser perf.data -t csv
```

* * *

To modify the output files prefix to `record1`:

```
spe-parser perf.data -t csv -p record1
```

This will result in the creation of three files: record1-ldst.csv, record1-br.csv, and record1-other.csv, corresponding respectively to Load/Store, Branch, and Other SPE packets.

* * *

The `spe-parser` will by default parse Load/Store, Branch, and Other SPE packets into three separate files. To disable parsing for a specific packet type, use the options below:

```
spe-parser perf.data --noldst --noother --nobr
```

* * *

To speed up parsing, increase concurrency; to use less resources, decrease it. By default, the system's core count is used. To change it:

```
spe-parser perf.data --concurrency 2
```

* * *

To include symbol information for corresponding instructions in the output files:

```
spe-parser perf.data --symbols
```

Please make sure your workload is compiled with debug information (e.g. -g).

* * *

To parse raw SPE fill buffer data (e.g. generated with [WindowsPerf](https://gitlab.com/Linaro/WindowsPerf/windowsperf)), use the options below:

```
spe-parser spe.data --raw-buffer
```

Please note that raw SPE buffer doesn't contain additional meta-data perf.data file contains, e.g. no symbol name resolution is possible.

* * *

To check the `spe-parser` version, which is crucial as the file schema may change between versions, the updates between each version can be found in the [Changelog](/telemetry-solution/telemetry-solution/-/blob/main/tools/spe_parser/CHANGELOG.md):

```
spe-parser --version
```

* * *

For detailed scheme descriptions of output files, column explanations, and possible values and meanings:

```
spe-parser --help
```

## Development[](#development)

Run tests using the following command.

```
pip install tox
make test
```

For now, please refrain from using pre-commit to install the .pre-commit-config.yaml configuration, and instead run make lint to check.

```
make lint
```

Test data files are located under the spe\_parser/tests/testdata/ directory. Some of them are binary files that are stored using git-lfs; working with them requires installing git-lfs (if not yet done so) by issuing `git lfs install`. Adding a new file is done by `git lfs track <file>`, then `git add` both this file and the resulting change in .gitattributes and then `git commit`. Updating a file is similar to updating regular git files: modify, then `git add` followed by `git commit`.