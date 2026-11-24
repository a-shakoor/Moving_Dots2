# Variable-Coherence Random Dot Motion Paradigm

This repository contains a variable-coherence random dot motion paradigm for visual experiments. The original code was created by Maria McKinley at the University of Washington and was significantly modified by Aly Shakoor for use in the Sensorimotor Neuroscience Laboratory at the University of Georgia under the direction of Dr. Tarkesh Singh and Dr. Deborah Barany.

## Requirements

The original version (v2.0) was tested on:

- macOS 10.9
- MATLAB R2014b
- Psychtoolbox 3.0.11

> **Keyboard note:** Psychtoolbox 3.0.11 does not read keyboard input from Thunderbolt-connected keyboards. Connect keyboards through USB.

## Getting started

Run `dotTrial.m`. It contains most of the paradigm parameters, including coherence levels, dot directions, and aperture velocity.

## Main files

| File | Purpose |
| --- | --- |
| `dotTrial.m` | Main file to run. Defines most experimental parameters, including the sets of coherence, dot direction, and aperture velocity. |
| `createDotInfo.m` | Called by `dotTrial.m` to return the `dotInfo` structure. Contains secondary parameters such as dot speed and aperture size. |
| `dotsX.m` | Uses the `dotInfo` structure to control most drawing and graphical behavior. Returns an output structure. |
| `singleDot.m` | Contains parameters and drawing code for individual dot traversal. |
| `output.m` | Takes the `outputStruct` array returned by `dotsX.m` and writes CSV files. **Update the folder paths in this file before running.** |
| `presentFeedback.m`, `openExperiment.m`, `closeExperiment.m`, `whiteSquareFlash.m` | Helper files for experiment setup, feedback, teardown, and event signaling. |
