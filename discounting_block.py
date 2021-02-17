#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on Wed 17 Feb 2021 04:28:10 PM MSK
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



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'discounting_block'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
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
    originPath='/home/ad/Desktop/Сысоева/M&M 15%/discounting_block.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "welcomeScreen"
welcomeScreenClock = core.Clock()
welcomeText = visual.TextStim(win=win, name='welcomeText',
    text="Welcome to your experiment!\n\nThe task of the game is to win as much as M&Ms as possible. You can do it by choosing between two alternatives: adjustable 4 M&Ms or standard 8 M&Ms. if you choose 4 M&Ms, it will decrease for the next round and revearsly if you choose 8 M&Ms, for the next round 4 M&Ms choice will increase. you will see the amount of your options each time.\n\nIf you choose 4 M&Ms you will have the reward in 100% of time, if you choose 8 M&Ms you will be rewarded 67% of the times. \n\nYou must wait before being rewarded. The reward waiting duration for choice of 4M&Ms and other M&Ms are different and they are demonstrated in the begining of each block by squares.\n\nThere are going to be 4 blocks. \n\nNumber of trials in the block is predefined – you can not have more trials and win more by choosing the shorter waiting duration.\n\nTo choose options use:\n'1' for left option\n'2' for right option\n\nPress SPACE to start the experiment!",
    font='Arial',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
welcomeResp = keyboard.Keyboard()
bb = 1

# Initialize components for Routine "Initialization"
InitializationClock = core.Clock()
chance = ['You got it!', 'You did not get it!', 'You got it!','You did not get it!', 'You got it!', 'You got it!','You did not get it!','You got it!','You got it!' ]

# Initialize components for Routine "fixFramed"
fixFramedClock = core.Clock()
fixImg = visual.ImageStim(
    win=win,
    name='fixImg', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "delayFramed"
delayFramedClock = core.Clock()
delayImg = visual.ImageStim(
    win=win,
    name='delayImg', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
bb = 1

# Initialize components for Routine "choiceScreen"
choiceScreenClock = core.Clock()
choiceImg = visual.ImageStim(
    win=win,
    name='choiceImg', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
choiceResp = keyboard.Keyboard()
choiceWarning = visual.TextStim(win=win, name='choiceWarning',
    text='default text',
    font='Arial',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
total = 0
block = 0
nk = 0

short_reward = [4,4,4,4]
short_delay = [1,1,1,1]

long_reward = [8, 8, 8, 8]
long_delay = [1,15,30,7]

h = 'start'
n = 0

a = [0,0,0,0]

# Initialize components for Routine "choiceLeft"
choiceLeftClock = core.Clock()
leftImg = visual.ImageStim(
    win=win,
    name='leftImg', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "feedbackLeft"
feedbackLeftClock = core.Clock()
rewardImgLeft = visual.ImageStim(
    win=win,
    name='rewardImgLeft', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
rewardText = visual.TextStim(win=win, name='rewardText',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "choiceRight"
choiceRightClock = core.Clock()
rightImg = visual.ImageStim(
    win=win,
    name='rightImg', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "feedbackRight"
feedbackRightClock = core.Clock()
rewardImgRight = visual.ImageStim(
    win=win,
    name='rewardImgRight', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
rightText = visual.TextStim(win=win, name='rightText',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "repeatScreen"
repeatScreenClock = core.Clock()
repeatText = visual.TextStim(win=win, name='repeatText',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
repeatResp = keyboard.Keyboard()

# Initialize components for Routine "Block_screen"
Block_screenClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='This block has ended.\n\nTo start and experience the delay of the next block, press space.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "endScreen"
endScreenClock = core.Clock()
endText = visual.TextStim(win=win, name='endText',
    text='The experiment is finished\n                 Thank you!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcomeScreen"-------
continueRoutine = True
# update component parameters for each repeat
welcomeResp.keys = []
welcomeResp.rt = []
_welcomeResp_allKeys = []
if (n % 2) == 0:
    tx = str(long_reward[block])+'~~~~~~~~~~~~~~~~~~~~~~'+str(short_reward[block])
else:
    tx = str(short_reward[block])+'~~~~~~~~~~~~~~~~~~~'+str(long_reward[block])
# keep track of which components have finished
welcomeScreenComponents = [welcomeText, welcomeResp]
for thisComponent in welcomeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcomeScreen"-------
while continueRoutine:
    # get current time
    t = welcomeScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcomeText* updates
    if welcomeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcomeText.frameNStart = frameN  # exact frame index
        welcomeText.tStart = t  # local t and not account for scr refresh
        welcomeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcomeText, 'tStartRefresh')  # time at next scr refresh
        welcomeText.setAutoDraw(True)
    
    # *welcomeResp* updates
    waitOnFlip = False
    if welcomeResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcomeResp.frameNStart = frameN  # exact frame index
        welcomeResp.tStart = t  # local t and not account for scr refresh
        welcomeResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcomeResp, 'tStartRefresh')  # time at next scr refresh
        welcomeResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcomeResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(welcomeResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if welcomeResp.status == STARTED and not waitOnFlip:
        theseKeys = welcomeResp.getKeys(keyList=['space'], waitRelease=False)
        _welcomeResp_allKeys.extend(theseKeys)
        if len(_welcomeResp_allKeys):
            welcomeResp.keys = _welcomeResp_allKeys[-1].name  # just the last key pressed
            welcomeResp.rt = _welcomeResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcomeScreen"-------
for thisComponent in welcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if welcomeResp.keys in ['', [], None]:  # No response was made
    welcomeResp.keys = None
thisExp.addData('welcomeResp.keys',welcomeResp.keys)
if welcomeResp.keys != None:  # we had a response
    thisExp.addData('welcomeResp.rt', welcomeResp.rt)
thisExp.nextEntry()
# the Routine "welcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
discountingBlockLong = data.TrialHandler(nReps=200, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='discountingBlockLong')
thisExp.addLoop(discountingBlockLong)  # add the loop to the experiment
thisDiscountingBlockLong = discountingBlockLong.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDiscountingBlockLong.rgb)
if thisDiscountingBlockLong != None:
    for paramName in thisDiscountingBlockLong:
        exec('{} = thisDiscountingBlockLong[paramName]'.format(paramName))

for thisDiscountingBlockLong in discountingBlockLong:
    currentLoop = discountingBlockLong
    # abbreviate parameter names if possible (e.g. rgb = thisDiscountingBlockLong.rgb)
    if thisDiscountingBlockLong != None:
        for paramName in thisDiscountingBlockLong:
            exec('{} = thisDiscountingBlockLong[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Initialization"-------
    continueRoutine = True
    # update component parameters for each repeat
    if (n % 2) == 0:
        tx = str(long_reward[block])+'  for 67%'+'              '+str(short_reward[block])+'  for 100%'
        chanceLeft = chance[n%9]
        chanceRight = 'You got it!'
        transparencyRight = 1
        transparencyLeft = 0
        fixedImage = 'img/even_'+str(round(short_reward[block]))+'_square.png'
        delayImage = 'img/even_8_square_'+str(round(short_reward[block]))+'.png'
        choiceImage = 'img/even_choice_'+str(round(short_reward[block]))+'.png'
        choiceImageLeft = 'img/even_8_circle_'+str(round(short_reward[block]))+'.png'
        choiceImageRight = 'img/even_'+str(round(short_reward[block]))+'_circle.png'
        rewardImageLeft = 'img/8m&m.png'
        rewardImageRight = 'img/'+str(round(short_reward[block]))+'m&m.png'
        rewardLeft = long_reward[block]
        rewardRight = short_reward[block]
        block_screen = 0
    else:
        tx = str(short_reward[block])+'  for 100%'+'              '+str(long_reward[block])+'  for 67%'
        chanceLeft= 'You got it!'
        chanceRight= chance[n%9]
        transparencyRight = 0
        transparencyLeft = 1
        fixedImage = 'img/odd_'+str(round(short_reward[block]))+'_square.png'
        delayImage = 'img/odd_8_square_'+str(round(short_reward[block]))+'.png'
        choiceImage = 'img/odd_choice_'+str(round(short_reward[block]))+'.png'
        choiceImageLeft = 'img/odd_'+str(round(short_reward[block]))+'_circle.png'
        choiceImageRight = 'img/odd_8_circle_'+str(round(short_reward[block]))+'.png'
        rewardImageLeft = 'img/'+str(round(short_reward[block]))+'m&m.png'
        rewardImageRight = 'img/8m&m.png'
        rewardLeft = short_reward[block]
        rewardRight = long_reward[block]
        block_screen = 0
    # keep track of which components have finished
    InitializationComponents = []
    for thisComponent in InitializationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    InitializationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Initialization"-------
    while continueRoutine:
        # get current time
        t = InitializationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=InitializationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InitializationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Initialization"-------
    for thisComponent in InitializationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Initialization" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    blockbegin1 = data.TrialHandler(nReps=bb, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='blockbegin1')
    thisExp.addLoop(blockbegin1)  # add the loop to the experiment
    thisBlockbegin1 = blockbegin1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlockbegin1.rgb)
    if thisBlockbegin1 != None:
        for paramName in thisBlockbegin1:
            exec('{} = thisBlockbegin1[paramName]'.format(paramName))
    
    for thisBlockbegin1 in blockbegin1:
        currentLoop = blockbegin1
        # abbreviate parameter names if possible (e.g. rgb = thisBlockbegin1.rgb)
        if thisBlockbegin1 != None:
            for paramName in thisBlockbegin1:
                exec('{} = thisBlockbegin1[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "fixFramed"-------
        continueRoutine = True
        # update component parameters for each repeat
        fixImg.setImage(fixedImage)
        # keep track of which components have finished
        fixFramedComponents = [fixImg]
        for thisComponent in fixFramedComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixFramedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fixFramed"-------
        while continueRoutine:
            # get current time
            t = fixFramedClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixFramedClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixImg* updates
            if fixImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixImg.frameNStart = frameN  # exact frame index
                fixImg.tStart = t  # local t and not account for scr refresh
                fixImg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixImg, 'tStartRefresh')  # time at next scr refresh
                fixImg.setAutoDraw(True)
            if fixImg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixImg.tStartRefresh + short_delay[block]-frameTolerance:
                    # keep track of stop time/frame for later
                    fixImg.tStop = t  # not accounting for scr refresh
                    fixImg.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixImg, 'tStopRefresh')  # time at next scr refresh
                    fixImg.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixFramedComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixFramed"-------
        for thisComponent in fixFramedComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "fixFramed" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed bb repeats of 'blockbegin1'
    
    
    # set up handler to look after randomisation of conditions etc
    blockbegin = data.TrialHandler(nReps=bb, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='blockbegin')
    thisExp.addLoop(blockbegin)  # add the loop to the experiment
    thisBlockbegin = blockbegin.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlockbegin.rgb)
    if thisBlockbegin != None:
        for paramName in thisBlockbegin:
            exec('{} = thisBlockbegin[paramName]'.format(paramName))
    
    for thisBlockbegin in blockbegin:
        currentLoop = blockbegin
        # abbreviate parameter names if possible (e.g. rgb = thisBlockbegin.rgb)
        if thisBlockbegin != None:
            for paramName in thisBlockbegin:
                exec('{} = thisBlockbegin[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "delayFramed"-------
        continueRoutine = True
        # update component parameters for each repeat
        delayImg.setImage(delayImage)
        # keep track of which components have finished
        delayFramedComponents = [delayImg]
        for thisComponent in delayFramedComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        delayFramedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "delayFramed"-------
        while continueRoutine:
            # get current time
            t = delayFramedClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=delayFramedClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *delayImg* updates
            if delayImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                delayImg.frameNStart = frameN  # exact frame index
                delayImg.tStart = t  # local t and not account for scr refresh
                delayImg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(delayImg, 'tStartRefresh')  # time at next scr refresh
                delayImg.setAutoDraw(True)
            if delayImg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > delayImg.tStartRefresh + long_delay[block]-frameTolerance:
                    # keep track of stop time/frame for later
                    delayImg.tStop = t  # not accounting for scr refresh
                    delayImg.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(delayImg, 'tStopRefresh')  # time at next scr refresh
                    delayImg.setAutoDraw(False)
            bb = 0
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in delayFramedComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "delayFramed"-------
        for thisComponent in delayFramedComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "delayFramed" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed bb repeats of 'blockbegin'
    
    
    # ------Prepare to start Routine "choiceScreen"-------
    continueRoutine = True
    # update component parameters for each repeat
    choiceImg.setImage(choiceImage)
    choiceResp.keys = []
    choiceResp.rt = []
    _choiceResp_allKeys = []
    choiceWarning.setText(tx)
    left = 0
    right = 0
    
    # keep track of which components have finished
    choiceScreenComponents = [choiceImg, choiceResp, choiceWarning]
    for thisComponent in choiceScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    choiceScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "choiceScreen"-------
    while continueRoutine:
        # get current time
        t = choiceScreenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=choiceScreenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *choiceImg* updates
        if choiceImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choiceImg.frameNStart = frameN  # exact frame index
            choiceImg.tStart = t  # local t and not account for scr refresh
            choiceImg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choiceImg, 'tStartRefresh')  # time at next scr refresh
            choiceImg.setAutoDraw(True)
        
        # *choiceResp* updates
        waitOnFlip = False
        if choiceResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choiceResp.frameNStart = frameN  # exact frame index
            choiceResp.tStart = t  # local t and not account for scr refresh
            choiceResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choiceResp, 'tStartRefresh')  # time at next scr refresh
            choiceResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(choiceResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(choiceResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if choiceResp.status == STARTED and not waitOnFlip:
            theseKeys = choiceResp.getKeys(keyList=['1', '2'], waitRelease=False)
            _choiceResp_allKeys.extend(theseKeys)
            if len(_choiceResp_allKeys):
                choiceResp.keys = _choiceResp_allKeys[-1].name  # just the last key pressed
                choiceResp.rt = _choiceResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *choiceWarning* updates
        if choiceWarning.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            choiceWarning.frameNStart = frameN  # exact frame index
            choiceWarning.tStart = t  # local t and not account for scr refresh
            choiceWarning.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choiceWarning, 'tStartRefresh')  # time at next scr refresh
            choiceWarning.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in choiceScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "choiceScreen"-------
    for thisComponent in choiceScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if choiceResp.keys in ['', [], None]:  # No response was made
        choiceResp.keys = None
    discountingBlockLong.addData('choiceResp.keys',choiceResp.keys)
    if choiceResp.keys != None:  # we had a response
        discountingBlockLong.addData('choiceResp.rt', choiceResp.rt)
    thisExp.addData('small_reward', short_reward[block])
    thisExp.addData('Delay', long_delay[block])
    
    if (n % 2) == 0:
        left_delay = long_delay[block]
        right_delay = short_delay[block]
        if(choiceResp.keys == '1'):
    
            if(chanceLeft == 'You got it!'):
                transparencyLeft = 1
                total += long_reward[block]
            left = 1 
            short_reward[block] = round(1.15*short_reward[block],2)
            h += choiceResp.keys
    
    
        elif(choiceResp.keys == '2'):
            if(chanceRight == 'You got it!'):
                transparencyRight = 1
                total += short_reward[block]
            right = 1
            short_reward[block] = round(0.85*short_reward[block],2)
            h += choiceResp.keys
    
    
    else:
        left_delay = short_delay[block]
        right_delay = long_delay[block]
        
        if(choiceResp.keys == '1'):
            if(chanceLeft == 'You got it!'):
                transparencyLeft = 1
                total += short_reward[block]
            left = 1 
            short_reward[block] = round(0.85*short_reward[block],2)
            h += choiceResp.keys
    
    
            
        elif(choiceResp.keys == '2'):
            if(chanceRight == 'You got it!'):
                transparencyRight= 1
                total += long_reward[block]
            right = 1
            short_reward[block] = round(1.15*short_reward[block],2)
            h += choiceResp.keys
    
    
    if h[-3:] == '111' or h[-3:] == '222':
    
        a[block] += short_reward[block]
        nk +=1
        
        if nk==5:
            a[block] = a[block] / 5
            
            block +=1
            h = 'start'
            block_screen = 1
            bb = 1
            nk = 0
    elif short_reward[block] < 0.6 :
         a[block] = short_reward[block]
         block += 1
         h = 'start'
         block_screen = 1
         bb = 1
         nk = 0
    elif short_reward[block] > 7.2 :
         a[block] = short_reward[block]
         block += 1
         h = 'start'
         block_screen = 1
         bb = 1
         nk = 0
    
    repeat_text = 'total amount:' + str(round(total,2)) + ', press space to continue'
    n += 1
    # the Routine "choiceScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    choiceLeftLoop = data.TrialHandler(nReps=left, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='choiceLeftLoop')
    thisExp.addLoop(choiceLeftLoop)  # add the loop to the experiment
    thisChoiceLeftLoop = choiceLeftLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisChoiceLeftLoop.rgb)
    if thisChoiceLeftLoop != None:
        for paramName in thisChoiceLeftLoop:
            exec('{} = thisChoiceLeftLoop[paramName]'.format(paramName))
    
    for thisChoiceLeftLoop in choiceLeftLoop:
        currentLoop = choiceLeftLoop
        # abbreviate parameter names if possible (e.g. rgb = thisChoiceLeftLoop.rgb)
        if thisChoiceLeftLoop != None:
            for paramName in thisChoiceLeftLoop:
                exec('{} = thisChoiceLeftLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "choiceLeft"-------
        continueRoutine = True
        # update component parameters for each repeat
        leftImg.setImage(choiceImageLeft)
        # keep track of which components have finished
        choiceLeftComponents = [leftImg]
        for thisComponent in choiceLeftComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        choiceLeftClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "choiceLeft"-------
        while continueRoutine:
            # get current time
            t = choiceLeftClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=choiceLeftClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *leftImg* updates
            if leftImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leftImg.frameNStart = frameN  # exact frame index
                leftImg.tStart = t  # local t and not account for scr refresh
                leftImg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftImg, 'tStartRefresh')  # time at next scr refresh
                leftImg.setAutoDraw(True)
            if leftImg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > leftImg.tStartRefresh + left_delay-frameTolerance:
                    # keep track of stop time/frame for later
                    leftImg.tStop = t  # not accounting for scr refresh
                    leftImg.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(leftImg, 'tStopRefresh')  # time at next scr refresh
                    leftImg.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in choiceLeftComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "choiceLeft"-------
        for thisComponent in choiceLeftComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "choiceLeft" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "feedbackLeft"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        rewardImgLeft.setOpacity(transparencyLeft)
        rewardImgLeft.setImage(rewardImageLeft)
        rewardText.setText(chanceLeft)
        thisExp.addData('result of chosen',chanceLeft )
        thisExp.addData('delay of chosen', left_delay)
        thisExp.addData('reward of chosen', rewardLeft)
        
        thisExp.addData('total amount', total)
        # keep track of which components have finished
        feedbackLeftComponents = [rewardImgLeft, rewardText]
        for thisComponent in feedbackLeftComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        feedbackLeftClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "feedbackLeft"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = feedbackLeftClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=feedbackLeftClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rewardImgLeft* updates
            if rewardImgLeft.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                rewardImgLeft.frameNStart = frameN  # exact frame index
                rewardImgLeft.tStart = t  # local t and not account for scr refresh
                rewardImgLeft.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rewardImgLeft, 'tStartRefresh')  # time at next scr refresh
                rewardImgLeft.setAutoDraw(True)
            if rewardImgLeft.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rewardImgLeft.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    rewardImgLeft.tStop = t  # not accounting for scr refresh
                    rewardImgLeft.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rewardImgLeft, 'tStopRefresh')  # time at next scr refresh
                    rewardImgLeft.setAutoDraw(False)
            
            # *rewardText* updates
            if rewardText.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                rewardText.frameNStart = frameN  # exact frame index
                rewardText.tStart = t  # local t and not account for scr refresh
                rewardText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rewardText, 'tStartRefresh')  # time at next scr refresh
                rewardText.setAutoDraw(True)
            if rewardText.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rewardText.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    rewardText.tStop = t  # not accounting for scr refresh
                    rewardText.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rewardText, 'tStopRefresh')  # time at next scr refresh
                    rewardText.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackLeftComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedbackLeft"-------
        for thisComponent in feedbackLeftComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed left repeats of 'choiceLeftLoop'
    
    
    # set up handler to look after randomisation of conditions etc
    choiceRightLoop = data.TrialHandler(nReps=right, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='choiceRightLoop')
    thisExp.addLoop(choiceRightLoop)  # add the loop to the experiment
    thisChoiceRightLoop = choiceRightLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisChoiceRightLoop.rgb)
    if thisChoiceRightLoop != None:
        for paramName in thisChoiceRightLoop:
            exec('{} = thisChoiceRightLoop[paramName]'.format(paramName))
    
    for thisChoiceRightLoop in choiceRightLoop:
        currentLoop = choiceRightLoop
        # abbreviate parameter names if possible (e.g. rgb = thisChoiceRightLoop.rgb)
        if thisChoiceRightLoop != None:
            for paramName in thisChoiceRightLoop:
                exec('{} = thisChoiceRightLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "choiceRight"-------
        continueRoutine = True
        # update component parameters for each repeat
        rightImg.setImage(choiceImageRight)
        # keep track of which components have finished
        choiceRightComponents = [rightImg]
        for thisComponent in choiceRightComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        choiceRightClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "choiceRight"-------
        while continueRoutine:
            # get current time
            t = choiceRightClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=choiceRightClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rightImg* updates
            if rightImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightImg.frameNStart = frameN  # exact frame index
                rightImg.tStart = t  # local t and not account for scr refresh
                rightImg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightImg, 'tStartRefresh')  # time at next scr refresh
                rightImg.setAutoDraw(True)
            if rightImg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rightImg.tStartRefresh + right_delay-frameTolerance:
                    # keep track of stop time/frame for later
                    rightImg.tStop = t  # not accounting for scr refresh
                    rightImg.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rightImg, 'tStopRefresh')  # time at next scr refresh
                    rightImg.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in choiceRightComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "choiceRight"-------
        for thisComponent in choiceRightComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "choiceRight" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "feedbackRight"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        rewardImgRight.setOpacity(transparencyRight)
        rewardImgRight.setImage(rewardImageRight)
        rightText.setText(chanceRight)
        thisExp.addData('result of chosen',chanceRight)
        thisExp.addData('delay of chosen', right_delay)
        thisExp.addData('reward of chosen', rewardRight)
        
        thisExp.addData('total amount', total)
        # keep track of which components have finished
        feedbackRightComponents = [rewardImgRight, rightText]
        for thisComponent in feedbackRightComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        feedbackRightClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "feedbackRight"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = feedbackRightClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=feedbackRightClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rewardImgRight* updates
            if rewardImgRight.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                rewardImgRight.frameNStart = frameN  # exact frame index
                rewardImgRight.tStart = t  # local t and not account for scr refresh
                rewardImgRight.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rewardImgRight, 'tStartRefresh')  # time at next scr refresh
                rewardImgRight.setAutoDraw(True)
            if rewardImgRight.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rewardImgRight.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    rewardImgRight.tStop = t  # not accounting for scr refresh
                    rewardImgRight.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rewardImgRight, 'tStopRefresh')  # time at next scr refresh
                    rewardImgRight.setAutoDraw(False)
            
            # *rightText* updates
            if rightText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightText.frameNStart = frameN  # exact frame index
                rightText.tStart = t  # local t and not account for scr refresh
                rightText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightText, 'tStartRefresh')  # time at next scr refresh
                rightText.setAutoDraw(True)
            if rightText.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rightText.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    rightText.tStop = t  # not accounting for scr refresh
                    rightText.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rightText, 'tStopRefresh')  # time at next scr refresh
                    rightText.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackRightComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedbackRight"-------
        for thisComponent in feedbackRightComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed right repeats of 'choiceRightLoop'
    
    
    # ------Prepare to start Routine "repeatScreen"-------
    continueRoutine = True
    # update component parameters for each repeat
    repeatText.setText(repeat_text)
    repeatResp.keys = []
    repeatResp.rt = []
    _repeatResp_allKeys = []
    # keep track of which components have finished
    repeatScreenComponents = [repeatText, repeatResp]
    for thisComponent in repeatScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    repeatScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "repeatScreen"-------
    while continueRoutine:
        # get current time
        t = repeatScreenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=repeatScreenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *repeatText* updates
        if repeatText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            repeatText.frameNStart = frameN  # exact frame index
            repeatText.tStart = t  # local t and not account for scr refresh
            repeatText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(repeatText, 'tStartRefresh')  # time at next scr refresh
            repeatText.setAutoDraw(True)
        
        # *repeatResp* updates
        waitOnFlip = False
        if repeatResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            repeatResp.frameNStart = frameN  # exact frame index
            repeatResp.tStart = t  # local t and not account for scr refresh
            repeatResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(repeatResp, 'tStartRefresh')  # time at next scr refresh
            repeatResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(repeatResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(repeatResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if repeatResp.status == STARTED and not waitOnFlip:
            theseKeys = repeatResp.getKeys(keyList=['space'], waitRelease=False)
            _repeatResp_allKeys.extend(theseKeys)
            if len(_repeatResp_allKeys):
                repeatResp.keys = _repeatResp_allKeys[-1].name  # just the last key pressed
                repeatResp.rt = _repeatResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in repeatScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "repeatScreen"-------
    for thisComponent in repeatScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if repeatResp.keys in ['', [], None]:  # No response was made
        repeatResp.keys = None
    discountingBlockLong.addData('repeatResp.keys',repeatResp.keys)
    if repeatResp.keys != None:  # we had a response
        discountingBlockLong.addData('repeatResp.rt', repeatResp.rt)
    
    if block == 4:
        discountingBlockLong.finished=True 
    # the Routine "repeatScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=block_screen, method='random', 
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
        
        # ------Prepare to start Routine "Block_screen"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        Block_screenComponents = [text, key_resp]
        for thisComponent in Block_screenComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Block_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Block_screen"-------
        while continueRoutine:
            # get current time
            t = Block_screenClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Block_screenClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Block_screenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Block_screen"-------
        for thisComponent in Block_screenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        trials.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
        trials.addData('key_resp.started', key_resp.tStartRefresh)
        trials.addData('key_resp.stopped', key_resp.tStopRefresh)
        # the Routine "Block_screen" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed block_screen repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 200 repeats of 'discountingBlockLong'


# ------Prepare to start Routine "endScreen"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat

for i in range(4):
    a[i] = a[i] / a[0] 

k = (7*(a[3]+a[0]) +  8*(a[3]+a[1]) + 15*(a[1]+a[2]) ) / 58
thisExp.addData('DelayFactor', k)
# keep track of which components have finished
endScreenComponents = [endText]
for thisComponent in endScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "endScreen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endText* updates
    if endText.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        endText.frameNStart = frameN  # exact frame index
        endText.tStart = t  # local t and not account for scr refresh
        endText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endText, 'tStartRefresh')  # time at next scr refresh
        endText.setAutoDraw(True)
    if endText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > endText.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            endText.tStop = t  # not accounting for scr refresh
            endText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(endText, 'tStopRefresh')  # time at next scr refresh
            endText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "endScreen"-------
for thisComponent in endScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
endTex = 'Thank you ! you won' + str(total)

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
