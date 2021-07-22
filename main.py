import osascript
osascript.osascript("set volume output volume 100")

n = 0
updown = input("Hit W or S to raise or lower the volume respectively: ")
prethresh_vols = [5, 8, 13, 21] # numbers from the fibonacci sequence which are used as volumes until
# the user selects a volume index above 4 at which point the volume=volume_index^2
sq_threshold = len(prethresh_vols) # threshold past which  vol=vol_idx^2
while True:

    if updown.upper() == 'W':
        if n < 10: n += 1
    elif updown.upper() == 'S':
        if n > 0: n -= 1
    if n < sq_threshold and n != 0:
        vol = prethresh_vols[n-1]
    else:
        vol = n**2
    print("Setting volume to: %s" % vol)
    osascript.osascript("set volume output volume %s" % vol)
    updown = input("Hit W or S to raise or lower the volume respectively: ")