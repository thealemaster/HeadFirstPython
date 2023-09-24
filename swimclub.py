import statistics

FOLDER = "swimdata/"

def read_swim_data (filename):
     
    swimmer, age, distance, stroke = filename.removesuffix(".txt").split ("-")

    with open (FOLDER + filename) as file:
        lines = file.readlines()
        times = lines[0].strip().split (",")

    converts = []

    for t in times:
        # Extract the component parts: start weith the minutes value
        if ":" in t:
            minutes, rest = t.split (":")
            seconds, hundreths = rest.split (".")
        else:
            minutes = 0
            seconds, hundreths = t.split (".")

        # Convert the strings
        converts.append((int(minutes) * 60 * 100) + (int(seconds) * 100) + int (hundreths))

    average = statistics.mean(converts)

    mins_secs, hundreths = str(round(average / 100, 2)).split(".")

    mins_secs = int(mins_secs)

    minutes = mins_secs // 60

    seconds = mins_secs - minutes*60

    converted_average = str(minutes) + ":" + str(seconds) + "." + hundreths

    return swimmer, age, distance, stroke, times, converted_average
