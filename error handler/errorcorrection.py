from errordetection import *

def string2bin(string):
    bitlist = []
    for s in string:
        bitlist.append(char2bin(s))
    return bitlist

def segmentString(string, fillchar):
    desiredwidth = 8
    stringlist = []
    leftstring = string[:8]
    rightstring = string[8:]
    while len(leftstring) < desiredwidth:
        leftstring += fillchar
    stringlist.append(leftstring)
    if len(rightstring) > 1:
        while len(rightstring) < desiredwidth:
            rightstring += fillchar
        stringlist.append(rightstring)
    return stringlist

def printFrames(frames):
    frameN = 0
    for frame in frames:
        charN = 0
        for bin in frame:
            char = bin2char(bin)
            print(f"{charN:2}", bin, char)
            charN += 1
        frameN += 1
        print()

def string2frames(string, fillchar):
    framelist = []
    stringlist = segmentString(string, fillchar)
    for segment in stringlist:
        framelist.append(string2bin(segment))
    return framelist

def appendParityColumn(frame, desiredparity):
    framelist = []
    for bitlist in frame:
        framelist.append(appendParity(bitlist,desiredparity))
    return framelist

def transpose(lst):
    lst = list(map(list, zip(*lst)))
    return lst

def appendParityRow(frame, desiredparity):
    return transpose(appendParityColumn(transpose(frame),desiredparity))
    
def appendParityToFrame(frame, desiredparity):
    return appendParityRow(appendParityColumn(frame, desiredparity),desiredparity)

def appendParityToFrames(framelist, desiredparity):
    newframelist = []
    for frame in framelist:
        newframelist.append(appendParityToFrame(frame, desiredparity))
    return newframelist

def transmitFrames(framelist, errorprob):
    newframelist = []
    for frame in framelist:
        newframe = []
        for row in frame:
            (newRow, bitsFlipped) = addNoise(row, errorprob)
            newframe.append(newRow)
        newframelist.append(newframe)
    return newframelist

def splitFrame(frame):
    payload = []
    paritycolumn = []
    parityrow = []
    for row in frame[:8]:
        payload.append(row[:8])
        paritycolumn.append(row[8])
    parityrow = frame[8]
    return payload, paritycolumn, parityrow

def checkParityOfFrame(frame, desiredparity):
    (recvpayload, recvparitycolumn, recvparityrow) = splitFrame(frame)
    newframe = appendParityToFrame(recvpayload, desiredparity)
    (calcpayload, calcparitycolumn, calcparityrow) = splitFrame(newframe)
    columnerror = []
    rowerror = []
    for i in range(len(recvparitycolumn)):
        if recvparitycolumn[i] != calcparitycolumn[i]:
            rowerror.append(i)
    for j in range(len(recvparityrow)):
        if recvparityrow[j] != calcparityrow[j]:
            columnerror.append(j)
    return columnerror, rowerror

def repairFrame(frame, columnerror, rowerror):
    if len(columnerror) == 0 and len(rowerror) == 0:
        return 'NO ERRORS'
    elif len(columnerror) == 2 and (8 in columnerror) and len(rowerror) == 1:
        frame[rowerror[0]][columnerror[0]] = 1 - frame[rowerror[0]][columnerror[0]]
        return 'CORRECTED'
    elif len(columnerror) == 0 or len(rowerror) == 0:
        return 'PARITY ERROR'
    else:
        return 'NOT CORRECTED'

def repairFrames(framelist, desiredparity):
    statuslist = []
    for i in range(len(framelist)):
        (columnerror, rowerror) = checkParityOfFrame(framelist[i], desiredparity)
        status = repairFrame(framelist[i], columnerror, rowerror)
        statuslist.append(status)
        if status == 'NO ERRORS':
            print('Frame ' + str(i) + ' has no errors')
        elif status == 'CORRECTED':
            print('Frame ' + str(i) + ' has been repaired')
        elif status == 'NOT CORRECTED' or status == 'PARITY ERROR':
            print('Frame ' + str(i) + ' could not be repaired')
    return statuslist

def stripFrames(framelist):
    payloadlist = []
    for frame in framelist:
        (payload, paritycolumn, parityrow) = splitFrame(frame)
        payloadlist.append(payload)
    return payloadlist

def bin2string(frame, fillchar):
    string = ''
    for bits in frame:
        char = bin2char(bits)
        if char != fillchar:
            string += char
    return string

def frames2string(framelist, fillchar):
    finalstring = ''
    for frame in framelist:
        finalstring += bin2string(frame, fillchar)
    return finalstring

def main(errorProb = .01, desiredParity = 0, fillChar = '~'):
    inputstring = str(input('Enter a string: '))
    inputframes = string2frames(inputstring,fillChar)
    transframes = appendParityToFrames(inputframes,desiredParity)
    recvframes = transmitFrames(transframes,errorProb)
    status = repairFrames(recvframes,desiredParity)
    strpframes = stripFrames(recvframes)
    outputstring = frames2string(strpframes,fillChar)
    print(outputstring)
    print(status)

if __name__ == '__main__':
    main()
