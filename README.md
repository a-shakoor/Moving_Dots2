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

## White-square flash for MEG event signaling

The white-square flash signals the event listener used with the MEG in Coverdell. Its code appears in Sections 1 and 3.5 of `dotsX.m` and in `whiteSquareFlash.m`.

You may need to adjust the flash size or duration in `whiteSquareFlash.m` for your setup.

## Demo and example files

- `Demo1.m`: Demonstrates calling targets and dots. It places multiple targets on screen, changes them, and then displays dots.
- `Demo2.m`: Demonstrates placing targets at a specified distance from either fixation or the aperture and in the direction of possible motion. It was primarily created to test dot movement relative to targets and fixation.
- `dotsOnlyDemo.m`: A simple script for testing `dotsX.m`.
- `keyDots.m`: An experiment using keypress responses, including optional correction-trial loops and additional features.
- `contents.m`: Lists the files in this directory.

## How the dot motion works

Dots are plotted randomly using three sets in round-robin order. For each set, a percentage of dots determined by the requested coherence is designated to move in the motion direction.

After the first set is plotted, dots in the next set are either replotted randomly or displaced in the motion direction. Displacement depends on screen size, viewing distance, dot speed, and display refresh rate. Each set appears every third frame. A dot is never displayed for more than one frame at a time.

## Dot wrap-around

Wrap-around primarily affects dots at high coherence. Only dots displaced in the motion direction wrap around; dots appearing at random locations may appear anywhere.

At low coherence, it is extremely unlikely that a dot will appear at an aperture edge, persist long enough, and reappear visibly on the opposite side. The circular aperture determines what is visible, while the square aperture defines the dot boundaries.

When a moving dot exits one side of the aperture, it may reappear at a randomized location along the opposite boundary rather than under a periodic boundary condition. This reduces the spatial cue that would otherwise occur at high coherences, where moving dots can accumulate in the direction of motion. Randomizing the reappearance location also randomizes the delay before a dot returns to the visible circular aperture.

## Attribution

- Original variable-coherence random dot motion code: Maria McKinley, University of Washington (February 2007; updated June 2014)
- Significant modifications for the Sensorimotor Neuroscience Laboratory, University of Georgia: Aly Shakoor (updated May 2019)
