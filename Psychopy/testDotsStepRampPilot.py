#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.5),
    on February 26, 2021, at 14:20
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

from psychopy.tools.monitorunittools import deg2pix
from psychopy.event import getKeys


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.5'
expName = 'testDotsStepRampPilot'  # from the Builder filename that created this script
expInfo = {'participant': '', 'trials_per_condition': '90', 'pursuit_or_saccade': '0 = none, 1 = pursuit, 2 = saccade', 'practice_version': '0', 'break_every_n_trials': '30', 'pupil_on': '0'}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Lab\\Documents\\GitHub\\Moving_Dots2\\Psychopy\\testDotsStepRampPilot.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=1, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='asus', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='deg')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
break_text = visual.TextStim(win=win, name='break_text',
    text='Please take a break. \nRest your eyes. \nGet up and stretch.\nPress the spacebar when you’re done.',
    font='Arial',
    pos=(0, 0), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
postbreak_text = visual.TextStim(win=win, name='postbreak_text',
    text='Get Ready!',
    font='Arial',
    pos=(0, 0), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
fixation1 = visual.ShapeStim(
    win=win, name='fixation1', vertices='cross',units='deg', 
    size=(.8, .8),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=0, depth=-3.0, interpolate=True)
red_dot = visual.Polygon(
    win=win, name='red_dot',units='deg', 
    edges=100, size=(0.6, 0.6),
    ori=0, pos=(0, 0),
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='Red', fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
fixation2 = visual.ShapeStim(
    win=win, name='fixation2', vertices='cross',
    size=(0.1,0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=0, depth=-5.0, interpolate=True)
pursuit_or_saccade_dot = visual.Polygon(
    win=win, name='pursuit_or_saccade_dot',units='deg', 
    edges=20, size=(0.6, 0.6),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor='Red', fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
#print("dotsize set to:  ", dots_stimulus.dotSize)

## Type checking inputs
typecheck_flag = 0
if expInfo['trials_per_condition'].isdigit():
    print("trials_per_condition is a digit: ", expInfo['trials_per_condition'])
else:
    print("Please input a digit for 'trials_per_condition.' \
    You entered: ", expInfo['trials_per_condition'])
    typecheck_flag = 1;
    
if expInfo['pupil_on'] in ["0","1"]:
    print("pupil_on: ", expInfo['pupil_on'])
else:
    print("Please input 1 or 0 for 'pupil_on'.  \
    You entered: ", expInfo['pupil_on'])
    typecheck_flag = 1;

if expInfo['practice_version'] in ["0","1"]:
    print("practice_version: ", expInfo['practice_version'])
else:
    print("Please input 1 or 0 for 'practice_version'.  \
    You entered: ", expInfo['practice_version'])
    typecheck_flag = 1;

if expInfo['break_every_n_trials'].isdigit():
    print("break_every_n_trials is a digit: ", expInfo['break_every_n_trials'])
else:
    print("Please input a digit for 'break_every_n_trials.' \
    You entered: ", expInfo['break_every_n_trials'])
    typecheck_flag = 1;

if expInfo['pursuit_or_saccade'] in ["0","1","2"]:
    print("pursuit_or_saccade: ", expInfo['pursuit_or_saccade'])
else:
    print("Please input 1 or 0 for 'practice_version'.  \
    You entered: ", expInfo['practice_version'])
    typecheck_flag = 1;

if typecheck_flag == 1:
    print("SEE ABOVE ERROR. Quitting now.")
    core.quit()
import numpy

# adjust these
coh_range = [0.03, .06, .12, .24, .48]
trials_per_condition = int(expInfo['trials_per_condition'])
pupil_on = int(expInfo['pupil_on'])
response_trial = 1 # fix this
practice = int(expInfo['practice_version'])
trialsPerBreak = int(expInfo['break_every_n_trials'])

pursuit_trial = 0
saccade_trial = 0
if int(expInfo['pursuit_or_saccade']) == 1:
    pursuit_trial = 1
elif int(expInfo['pursuit_or_saccade']) == 2:
    saccade_trial = 1
    
print("coherence range: ", coh_range,
      "\ntrials per condition: ", trials_per_condition,
      "\npupil_on: ", pupil_on,
      "\npractice version: ", practice,
      "\ntrials per break: ", trialsPerBreak,
      "\npursuit_trial: ", pursuit_trial,
      "\nsaccade_trial: ", saccade_trial)
      
# randomize coherences in blocks
coh_range_big = []
for x in range(0, trials_per_condition):
    x = coh_range.copy()
    numpy.random.shuffle(x)
    coh_range_big = coh_range_big + x
import zmq
from msgpack import loads

if pupil_on == 1:
    context = zmq.Context()
    # open a req port to talk to pupil
    addr = '198.137.18.59' #'127.0.0.1'  # remote ip or localhost
    req_port = "50020"  # same as in the pupil remote gui
    req = context.socket(zmq.REQ)
    req.connect("tcp://{}:{}".format(addr, req_port))
    # ask for the sub port
    req.send_string('SUB_PORT')
    sub_port = req.recv_string()

    # open a sub port to listen to pupil
    sub = context.socket(zmq.SUB)
    sub.connect("tcp://{}:{}".format(addr, sub_port))

    # set subscriptions to topics
    # recv just pupil/gaze/notifications
    sub.setsockopt_string(zmq.SUBSCRIBE, 'pupil.')
    # sub.setsockopt_string(zmq.SUBSCRIBE, 'gaze')
    # sub.setsockopt_string(zmq.SUBSCRIBE, 'notify.')
    # sub.setsockopt_string(zmq.SUBSCRIBE, 'logging.')
    # or everything:
    # sub.setsockopt_string(zmq.SUBSCRIBE, '')
# test congruency output
# response trial flag
# saccade version
stair_range = [.03, .06, .12, .24, .48, .80, .85, .90, .95, 1]
stair_ind = len(stair_range) - 1

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=100, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    pretrial_sleep_finished = 0
    # practice_text.text = "Coherence: " + str(dots_stimulus.coherence)
    #if practice == 0:
    #    dots_stimulus.coherence = coh_range_big.pop()
    #dots_stimulus.dir = (np.floor(np.random.rand() * 2) * 180)
    
    pursuit_saccade_isLeft = np.floor(np.random.rand() * 2)
    position = 0
    print("this trial: " , trials.thisN)
    psychopy_timestamp = win.getFutureFlipTime(clock=None)
    #topic, payload = sub.recv_multipart()
    #timestamp = loads(payload)[b'timestamp']
    
    if pupil_on:
        req.send_string('t')
        pupil_timestamp = req.recv_string()
        print("pupil timestamp", pupil_timestamp)
        print("psychopy timestamp", psychopy_timestamp)
    else:
        pupil_timestamp = -1;
    
    if practice == 1:
        dots_stimulus.coherence = stair_range[stair_ind]
    # keep track of which components have finished
    trialComponents = [break_text, postbreak_text, fixation1, red_dot, fixation2, pursuit_or_saccade_dot]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *break_text* updates
        if break_text.status == NOT_STARTED and trials.thisN % trialsPerBreak == 0 and trials.thisN != 0 and practice == 0:
            # keep track of start time/frame for later
            break_text.frameNStart = frameN  # exact frame index
            break_text.tStart = t  # local t and not account for scr refresh
            break_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_text, 'tStartRefresh')  # time at next scr refresh
            break_text.setAutoDraw(True)
        if break_text.status == STARTED:
            if bool(('space' in getKeys(keyList=["space"]))):
                # keep track of stop time/frame for later
                break_text.tStop = t  # not accounting for scr refresh
                break_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(break_text, 'tStopRefresh')  # time at next scr refresh
                break_text.setAutoDraw(False)
        
        # *postbreak_text* updates
        if postbreak_text.status == NOT_STARTED and break_text.status == FINISHED:
            # keep track of start time/frame for later
            postbreak_text.frameNStart = frameN  # exact frame index
            postbreak_text.tStart = t  # local t and not account for scr refresh
            postbreak_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(postbreak_text, 'tStartRefresh')  # time at next scr refresh
            postbreak_text.setAutoDraw(True)
        if postbreak_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > postbreak_text.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                postbreak_text.tStop = t  # not accounting for scr refresh
                postbreak_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(postbreak_text, 'tStopRefresh')  # time at next scr refresh
                postbreak_text.setAutoDraw(False)
        if pretrial_sleep_finished == 0 \
            and break_text.status != STARTED \
            and postbreak_text.status != STARTED:
            clock.wait(1) # in sec
            pretrial_sleep_finished = 1;
        
        # *fixation1* updates
        if fixation1.status == NOT_STARTED and pretrial_sleep_finished == 1:
            # keep track of start time/frame for later
            fixation1.frameNStart = frameN  # exact frame index
            fixation1.tStart = t  # local t and not account for scr refresh
            fixation1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation1, 'tStartRefresh')  # time at next scr refresh
            fixation1.setAutoDraw(True)
        if fixation1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation1.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation1.tStop = t  # not accounting for scr refresh
                fixation1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation1, 'tStopRefresh')  # time at next scr refresh
                fixation1.setAutoDraw(False)
        
        # *red_dot* updates
        if red_dot.status == NOT_STARTED and fixation1.status == STARTED:
            # keep track of start time/frame for later
            red_dot.frameNStart = frameN  # exact frame index
            red_dot.tStart = t  # local t and not account for scr refresh
            red_dot.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(red_dot, 'tStartRefresh')  # time at next scr refresh
            red_dot.setAutoDraw(True)
        if red_dot.status == STARTED:
            if bool(fixation2.status == FINISHED):
                # keep track of stop time/frame for later
                red_dot.tStop = t  # not accounting for scr refresh
                red_dot.frameNStop = frameN  # exact frame index
                win.timeOnFlip(red_dot, 'tStopRefresh')  # time at next scr refresh
                red_dot.setAutoDraw(False)
        
        # *fixation2* updates
        if fixation2.status == NOT_STARTED and fixation1.status == FINISHED:
            # keep track of start time/frame for later
            fixation2.frameNStart = frameN  # exact frame index
            fixation2.tStart = t  # local t and not account for scr refresh
            fixation2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation2, 'tStartRefresh')  # time at next scr refresh
            fixation2.setAutoDraw(True)
        if fixation2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation2.tStop = t  # not accounting for scr refresh
                fixation2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation2, 'tStopRefresh')  # time at next scr refresh
                fixation2.setAutoDraw(False)
        if fixation2.status == FINISHED and pursuit_or_saccade_dot.status!=FINISHED:
            pursuitSpeed = 10;
            stepRampTimeBackToCenter = (1.8/10);
            stepRampDist = pursuitSpeed * stepRampTimeBackToCenter;
            stopTime = 1;
            stopPosition = pursuitSpeed*stopTime;
            tStart = fixation2.tStop
            if pursuit_trial == 1:
                if pursuit_saccade_isLeft == 1:
                    position = [-(pursuitSpeed*(t-tStart)) + stepRampDist, 0]
                else:
                    position = [pursuitSpeed*(t-tStart) - stepRampDist, 0]
            elif saccade_trial == 1:
                if pursuit_saccade_isLeft == 0:
                    position = [-20,0] # deg
                else:
                    position = [20,0] # deg
        
        
        # *pursuit_or_saccade_dot* updates
        if pursuit_or_saccade_dot.status == NOT_STARTED and fixation2.status == FINISHED and (pursuit_trial==1 or saccade_trial==1):
            # keep track of start time/frame for later
            pursuit_or_saccade_dot.frameNStart = frameN  # exact frame index
            pursuit_or_saccade_dot.tStart = t  # local t and not account for scr refresh
            pursuit_or_saccade_dot.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pursuit_or_saccade_dot, 'tStartRefresh')  # time at next scr refresh
            pursuit_or_saccade_dot.setAutoDraw(True)
        if pursuit_or_saccade_dot.status == STARTED:
            if bool(position[0] > stopPosition or position[0] < -1*stopPosition):
                # keep track of stop time/frame for later
                pursuit_or_saccade_dot.tStop = t  # not accounting for scr refresh
                pursuit_or_saccade_dot.frameNStop = frameN  # exact frame index
                win.timeOnFlip(pursuit_or_saccade_dot, 'tStopRefresh')  # time at next scr refresh
                pursuit_or_saccade_dot.setAutoDraw(False)
        if pursuit_or_saccade_dot.status == STARTED:  # only update if drawing
            pursuit_or_saccade_dot.setPos(position, log=False)
        if pursuit_or_saccade_dot.status==FINISHED:
            win.flip()
            continueRoutine = False;
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('break_text.started', break_text.tStartRefresh)
    trials.addData('break_text.stopped', break_text.tStopRefresh)
    trials.addData('postbreak_text.started', postbreak_text.tStartRefresh)
    trials.addData('postbreak_text.stopped', postbreak_text.tStopRefresh)
    trials.addData('fixation1.started', fixation1.tStartRefresh)
    trials.addData('fixation1.stopped', fixation1.tStopRefresh)
    trials.addData('red_dot.started', red_dot.tStartRefresh)
    trials.addData('red_dot.stopped', red_dot.tStopRefresh)
    trials.addData('fixation2.started', fixation2.tStartRefresh)
    trials.addData('fixation2.stopped', fixation2.tStopRefresh)
    trials.addData('pursuit_or_saccade_dot.started', pursuit_or_saccade_dot.tStartRefresh)
    trials.addData('pursuit_or_saccade_dot.stopped', pursuit_or_saccade_dot.tStopRefresh)
    #trials.addData('coh', dots_stimulus.coherence)
    #trials.addData('dir', dots_stimulus.dir)
    #print("response keys: ", response.keys)
    #if len(response.keys) != 1:
    #    responseNum = -1
    #if response.keys[0] in ['r', 'right']:
    #  responseNum = 0
    #elif response.keys[0] in ['l', 'left']:
    #  responseNum = 180
    #else:
    #  responseNum = -2
    #correct = -1
    #if responseNum == dots_stimulus.dir:
    #    correct = 1
    #else:
    #    correct = 0
    
    #congruent = -1
    #if (dots_stimulus.dir == 180 and pursuit_saccade_isLeft == 1)  \
    #        or (dots_stimulus.dir == 0 and pursuit_saccade_isLeft == 0):
    #    congruent = 1
    #else:
    #    congruent = 0
    #trials.addData('response', responseNum)
    #trials.addData('correct', correct)
    trials.addData('pursuit_saccade_isLeft',pursuit_saccade_isLeft)
    #trials.addData('congruent', congruent)
    trials.addData('pupil_timestamp', pupil_timestamp)
    trials.addData('psychopy_timestamp', psychopy_timestamp)
    if practice == 1:
        if correct == 0 and stair_range[stair_ind] > .50:
            if stair_ind < len(stair_range) - 1:
                stair_ind += 1
                print("going back up a level to: ", stair_range[stair_ind])
            else:
                print("at max level. staying at: ", stair_range[stair_ind])
                pass
        else: 
            if stair_ind == 0:
                trials.finished = 1
            else:
                stair_ind -= 1
                print("going down to: ", stair_range[stair_ind])
    
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 100 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
