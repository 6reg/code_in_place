DATA_FILE: "colors.json"

def load_data():
    data = {}
    file = open("colors.json")
    n_colors = 0
    for line in file:
        line = line.strip()
        add_color(data, line)
        n_colors += 1
    print(len(data), n_colors)
    file.close()
    return data

def add_color(data, line):
    parts = line.split(',')
    color_name = parts(0)
    color_rgb = color_from_line(line)
    if color_name not in data:
        data[color_name] = []
    data[color_name].append(color_rgb)
    print(data)

def color_from_line(line):
    parts = line.split(',')
    r = int(parts[1])
    g = int(parts[2])
    b = int(parts[3])
    return [r, g, b]

load_data()
