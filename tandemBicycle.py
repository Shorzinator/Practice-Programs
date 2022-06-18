def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    maxSpeeds = []
    if fastest == True :
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort(reverse = True)

        for i in range(len(redShirtSpeeds)) :
            maxSpeeds.append(max(redShirtSpeeds[i], blueShirtSpeeds[i]))

        return sum(maxSpeeds)

    else :
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort()

        for i in range(len(redShirtSpeeds)) :
            maxSpeeds.append(max(redShirtSpeeds[i], blueShirtSpeeds[i]))

        return sum(maxSpeeds)
