s = "A Python script"
print(s[0])
print(s[2])
print(s[2:7])
print(s[2:8])

print(s[:8])
print(s[8:])

print(s[2:999])
print(s[222:999]) # w tym miejscu napis jest pusty

# szukamy dwukropka i wycinamy wszystko od niego do konca
message = 'Document "cv.doc" was printed on printer: XEROX'
print(message.find(":"))
print(message[message.find(":")+2:]) # szukamy od dwukropka do konca. +2 przesuwa kursor o dwa znaki w prawo

print(message[message.find('"')+1:])
tmp = message[message.find('"')+1:]
print(tmp[:tmp.find('"')])

# zadania:

q = "THE EYES"
print(q[0] + q[1] + q[2] + q[5] + q[3] + q[7] + q[4] + q[6])

q = "a gentleman"
print(q[3] + q[6] + q[7] + q[2] + q[0] + q[4] + q[5] + q[1] + q[8:])

q = "THE MORSE CODE"
print(q[1:3] + q[6] + q[8] + q[3] + q[10:12] + q[4] + q[13] + q[9] + q[12] + q[5] + q[0] + q[7])

line = 'Program "Kropka nad i" nadamy o: 22:00'
time = line[line.find(":")+2:]
print(time)
tmp = line[line.find('"')+1:]
title = tmp[:tmp.find('"')]
print(title, time)