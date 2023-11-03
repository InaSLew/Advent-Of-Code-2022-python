with open('input.txt') as f:
    streamBuffer = f.read()
    startIdx = 0
    endIdx = 14
    while (endIdx <= len(streamBuffer) - 1):
        packet = set(streamBuffer[startIdx:endIdx])
        if (len(packet) == 14):
            break
        startIdx += 1
        endIdx += 1

    print(f'{endIdx} characters processed before the first start-of-packet marker is detected')
