
meetings = [
    (9, 10),
    (10, 11),
    (12, 13),
    (12, 14)
]

for i in range(len(meetings)):

    for j in range(i + 1, len(meetings)):

        start1, end1 = meetings[i]
        start2, end2 = meetings[j]

        if start1 < end2 and start2 < end1:
            print("Conflict:", meetings[i], meetings[j])