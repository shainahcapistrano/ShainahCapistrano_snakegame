jerryAttrickScores = {"CMSC 150" : 87, "Math 151": 93}
roseBushScores = {"Math 151": 75, "Biology 101" : 81, "Physics 105" : 77}
patProgrammerScores = {"Math 151": 95, "CMSC 155" : 86, "CMSC 150": 92}

gradeBook = {"Jerry Attrick" : jerryAttrickScores,
		"Rose Bush" : roseBushScores,
              "Pat Programmer" : patProgrammerScores}

def computeAverage(studentName, gradeBook):
    total = 0
    if studentName in gradeBook:
        scores = gradeBook[studentName]
        if len(scores) > 0:
            for score in scores.values():
                total += score
            return total / len(scores)
        return -1 ## student in gradebook, but has no scores
    return -1 ## student not in gradebook
