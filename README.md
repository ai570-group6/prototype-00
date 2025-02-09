# Prototype 00

This is a prototype that classifies cell images into "neutrophil" and "myeloblast" classes. Note that this is
NOT a completed project that detects cancer. It's only intended to prove we can work with the dataset in a
simple way.

## Setup

Three different pip requirements files are provided. It may be possible to get these into one single file,
that install conditionally. Install the one most approrpiate to your device:

* __requirements-gpu.txt__: if you have a CUDA-capable NVIDIA GPU
* __requirements-mac.txt__: if you have an M* Mac
* __requirements-nogpu.txt__: if you only have CPU (note this will train pretty slowly)

i.e.

```bash
pip install -r ./requirements-gpu.txt
```
