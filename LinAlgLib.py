class Matrix:
    def __init__(self, values):
        self.values = values
        self.rows = len(values)
        self.cols = len(values[0])

    def __str__(self):
        string = ""
        for i in range(self.rows):
            for j in range(self.cols):
                string = string + str(self.values[i][j]) + " "
            string = string + "\n"
        return string

#testing
