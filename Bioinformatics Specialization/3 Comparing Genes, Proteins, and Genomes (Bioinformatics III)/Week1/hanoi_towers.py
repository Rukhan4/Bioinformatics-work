# Note that the three variables always represent different pegs,
# and so source + destination + middleman
#  is always equal to 1 + 2 + 3 = 6


def hanoi_towers(diskcount, source, destination):
    if diskcount == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    middleman = 6 - source - destination
    hanoi_towers(diskcount-1, source, middleman)
    print("Move disk 1 from source", source, "to destination", destination)
    hanoi_towers(diskcount-1, source, destination)
    return


print(hanoi_towers(4, 1, 3))
