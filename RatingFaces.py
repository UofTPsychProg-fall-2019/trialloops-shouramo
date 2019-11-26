

"""
Rating faces on a likert scale 
This code includes both parts of the assignment
Author: Moaz Shoura
"""

from __future__ import division
from __future__ import print_function

from psychopy import visual, event, core, logging
import os

# create a window:
win = visual.Window(fullscr=False, size=[1100, 800], units='pix', monitor='testMonitor')



# Instructions
instr = visual.TextStim(win, text="""For this experiment, you will rate faces on how attractive they are on a scale from 1 to 7. 1 meaning not attractive
and 7 meaning very attractive. Press any key to start""")

event.clearEvents()
instr.draw()
win.flip()
if 'escape' in event.waitKeys():
    core.quit()

# create a scale:
myRatingScale = visual.RatingScale(win, low=0, high=7, skipKeys=None,
        marker='glow', showValue=False, pos=[0, -200], name='How similar?')

# images used
imageList = [r'CFD-AM-204-122-N.png',r'CFD-AM-203-086-N.png',r'CFD-AM-208-143-N.png',r'CFD-AM-207-108-N.png',
r'CFD-AM-246-184-N.png',r'CFD-AM-221-184-N.png']


data = []
for image in imageList:
    x, y = myRatingScale.win.size
    myItem = visual.SimpleImageStim(win=win, image=image, units='pix', pos=[0, y//7])

    # rate each image on the scale
    for dimension in ['0= not attractive . . . 7=very attractive',
                      ]:
        myRatingScale.reset()  
        myRatingScale.setDescription(dimension)  
        event.clearEvents()
        while myRatingScale.noResponse:
            myItem.draw()
            myRatingScale.draw()
            win.flip()
            if event.getKeys(['escape']):
                core.quit()
        data.append([image, myRatingScale.scaleDescription.text,
                     myRatingScale.getRating(), myRatingScale.getRT()])  # save for later

        # clear the screen & pause between ratings
        win.flip()
        core.wait(0.35)  # brief pause

print('Example 2 (data from 2 images, each rated on 2 dimensions, reporting rating & RT):')
for d in data:
    print('  ', d)

# show & update until a response has been made
while myRatingScale.noResponse:
    myItem.draw()
    myRatingScale.draw()
    win.flip()
    if event.getKeys(['escape']):
        core.quit()



win.close()
core.quit()

# end of experiment
