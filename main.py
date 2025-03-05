import os

def main():
    userInput = input("Please enter a file directory: ")

    files = os.listdir(userInput)
    downInfo = []
    upInfo = []

    for element in files:
        try:
            element.index(".txt")
            with open(element) as file:
                lines = file.readlines()
                for line in lines:
                    currentLine = line.split()
                    for element in currentLine:
                        try:
                            element.index("Download:")
                            downloadLine = line.split()
                            downInfo.append(downloadLine[1])
                        except:
                            break
                    for element in currentLine:
                        try:
                            element.index("Upload:")
                            uploadLine = line.split()
                            upInfo.append(uploadLine[1])
                        except:
                            break
        except:
            break

    downloadAverage = 0.0
    for element in downInfo:
        downloadAverage = float(downloadAverage) + float(element)
    downloadAverage = downloadAverage / downInfo.__len__()
    downloadAverage = f"{downloadAverage:.2f}"
    print("Average Download Speed: " + str(downloadAverage))

    upAverage = 0.0
    for element in upInfo:
        upAverage = float(upAverage) + float(element)
    upAverage = upAverage / downInfo.__len__()
    upAverage = f"{upAverage:.2f}"
    print("Average Upload Speed: " + str(upAverage))

if __name__ == "__main__":
    main()