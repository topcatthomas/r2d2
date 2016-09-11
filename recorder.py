import datetime, time, threading, glob


start_time = time.clock()
recordingOn = False
recordedEvents = []
playBackIndex = 0

def playBackHandler(mc,playBackIndex,recordedEvents):
    print "playback index " + str(playBackIndex)
    ((strtype,time),(d1,d2)) = recordedEvents[playBackIndex]
    print "====="
    print recordedEvents[playBackIndex]
    print strtype
    print time
    print d1
    print d2
    print "====="
    if ( strtype == "action" ):
        mc.playAction(d1,d2)
    elif ( strtype == "doMove" ):
        mc.doMove(d1,d2)
    if ( playBackIndex+1 < len(recordedEvents) ):
        print 'waiting for ' + str(time)
        threading.Timer(time, playBackHandler,[mc,playBackIndex+1,recordedEvents]).start()
    else:
        print "====PLAYBACK COMPLETE===="

def recordingOnOff():
    global recordingOn 
    if recordingOn == False:
        startRecord()
    else:
        endRecord()
    print "recordong state " + str(recordingOn)
    return recordingOn

def startRecord():
    global recordedEvents,recordingOn,start_time 
    start_time = time.clock()
    recordedEvents = []
    recordingOn = True

def endRecord():
    global recordedEvents,recordingOn 
    recordingOn = False

def playBack(mc):
    global playBackIndex
    print "playback called"
    playBackIndex = 0
    print "playback index is " + str(playBackIndex)
    playBackHandler(mc,playBackIndex,recordedEvents)


def saveRecording(filename):
    with open(filename, 'w') as f:
        for ((strtype,time),(d1,d2)) in recordedEvents:
            f.write(strtype + " " + str(time) + " " + str(d1) + " " + str(d2) + "\n")

def loadRecording(filename):
    global recordedEvents,recordingOn 
    recordedEvents = []
    with open(filename, 'r') as f:
        for line in f:
            line.rstrip('\n')
            bit = line.split(' ')
            recordedEvents.append( ((bit[0],float(bit[1]) ) ,(bit[2],bit[3])))

def recordAction(action,speed):
    global recordedEvents,recordingOn,start_time 
    timePassed = time.clock() - start_time
    start_time = time.clock()
    recordedEvents.append((("action",str(timePassed)),(action,speed)))

def recordDoMove(x,y):
    global recordedEvents,recordingOn,start_time 
    timePassed = time.clock() - start_time
    start_time = time.clock()
    recordedEvents.append((("doMove",str(timePassed)),(x,y)))

def getRecList():
    reclist = glob.glob("*.rec")
    print "==== reclist ===="
    print reclist
    print "==== reclist ===="
    return reclist