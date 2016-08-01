"""
author:  Julio Ruano
email:   jruano03@gmail.com

Simple program to "animate" a "particle" through a "chamber". Various rules
are provided in terms of speed, direction, etc... Essentially is an interesting
approach to a very simple use case of bitmap manipulation.
"""
class ParticleAnimation:
    def animate(self, speed, init):
        animation = []
        right = []
        left = []
        ind = 0

        # Parse init
        for char in init:
            if char == 'R':
                right.append(ind)
            elif char == 'L':
                left.append(ind)
            ind += 1

        # Create frames
        occupied = True
        while occupied:
            frame = ""
            for i in range(len(init)):
                if i in right or i in left:
                    frame += 'X'
                else:
                    frame += '.'
            # Add frame to animation
            animation.append(frame)

            # Move particles going right
            for z in range(len(right)):
                right[z] += speed

            # Move particles going left
            for z in range(len(left)):
                left[z] -= speed

            # Movement complete?
            if 'X' not in frame:
                occupied = False
        return animation


def printAnimation(animation):
    """
    Format animation for print output
    """
    start_string = animation[0]
    start_string = "{" + start_string
    animation[0] = start_string

    end_string = animation.pop()
    end_string = end_string + "}"
    animation.append(end_string)

    for run in animation:
        print run


# Test ParticleAnimation
p2 = ParticleAnimation()
printAnimation(p2.animate(2, "..R...."))
print "\n"
printAnimation(p2.animate(3, "RR..LRL"))
print "\n"
printAnimation(p2.animate(2, "LRLR.LRLR"))
print "\n"
printAnimation(p2.animate(10, "RLRLRLRLRL"))
print "\n"
printAnimation(p2.animate(1, "..."))
print "\n"
printAnimation(p2.animate(1, "LRRL.LR.LRR.R.LRRL."))
print "\n"
