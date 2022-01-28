#!/usr/bin/python3

colors = {
    "red":      '\033[31m',
    "green":    '\033[32m',
    "default":  '\033[0m',
}

def color(color, string):
    return colors[color] + string + colors["default"]

def red(string):
    return color("red", string)

def green(string):
    return color("green", string)

def main():
    print(green("green"))
    print(red("red"))

if __name__ == '__main__':
    main()


