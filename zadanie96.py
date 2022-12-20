with open("wyjsciezadanie96.txt", "w") as output:
    with open("danezadanie96.txt", "r") as input:
        for line in input:
            output.write(line.upper())
