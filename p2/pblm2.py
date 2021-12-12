def command_parse(commands):
    forward = list(
        map(
            int,
            [command.rstrip()[-1:] for command in commands if command.find("forward") != -1]
        )
    )
    down = list(
        map(
            int,
            [command.rstrip()[-1:] for command in commands if command.find("down") != -1]
        )
    )
    up = list(
        map(
            int,
            [command.rstrip()[-1:] for command in commands if command.find("up") != -1]
        )
    )
    return forward, down, up


def aim_parse(commands):
    aim = 0
    x = 0
    y = 0
    for command in commands:
        if command.find("forward") != -1:
            temp = int(command.rstrip()[-1:])
            x += temp
            y += (temp * aim)
            print(f"x{x} - aim{aim} - y{y}")
        elif command.find("down") != -1:
            aim += int(command.rstrip()[-1:])
        else:
            aim -= int(command.rstrip()[-1:])
    return x * y

if __name__ == "__main__":
    # with open("input_p2_1.txt") as input:
    #     line_list = input.readlines()
    # forward, down, up = command_parse(line_list)
    # x = sum(forward)
    # y = sum(down) - sum(up)
    # print(x * y)

    with open("input_p2_2.txt") as input:
        line_list = input.readlines()
    print(aim_parse(line_list))
