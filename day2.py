def main():
    # Parse the input based on the submarine instructions
    directions = {"up": [], "down": [], "forward": []}
    with open("Inputs/input2.txt", "r") as f:
        for line in f.readlines():
            direction, distance = line.strip().split()
            directions[direction].append(int(distance))

    # Remember that dictionaries are ordered now :)
    up, down, forward = directions.values()

    # PART A

    print("----Recursive Methods----")
    horizontal_position = sum_list(forward)
    depth = subtract_lists(down, up)
    print(f"Submarine is at a horizontal position: {horizontal_position}")
    print(f"Submarine is at a depth of: {depth}")
    print(f"Result of multiplying horizontal position and depth: {horizontal_position * depth}")

    print("----Iterative Methods----")
    horizontal_position = simple_sum(forward)
    depth = simple_difference(down, up)
    print(f"Submarine is at a horizontal position: {horizontal_position}")
    print(f"Submarine is at a depth of: {depth}")
    print(f"Result of multiplying horizontal position and depth: {horizontal_position * depth}")

    # PART B
    ordered_directions = []
    with open("Inputs/input2.txt", "r") as f:
        for line in f.readlines():
            direction, distance = line.strip().split()
            ordered_directions.append((direction, int(distance)))

    aim, depth, forward = day_two_part_two(ordered_directions)
    print("--------PART B---------")
    print(f"Aim: {aim}, Depth: {depth}, Horizontal Position: {forward}")
    print(f"Product of depth and horizontal position: {depth * forward}")


def simple_sum(lst):
    """
    Sum a list of numbers by iterating over it.
    :param lst: The list of numbers to be summed over
    :return: The sum of the list of numbers.
    """
    count = 0
    for num in lst:
        count += num
    return count


def sum_list(lst):
    """
    Sum a list of numbers by recursively splitting the list in half.
    :param lst: The list of numbers to be summed over
    :return: The sum of the list of numbers.
    """
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    else:
        split_index = len(lst) // 2
        return sum_list(lst[:split_index]) + sum_list(lst[split_index:])


def simple_difference(lst1, lst2):
    """
    Computes the difference of sums of LST1 and LST2
    :param lst1: The list whose positive sum is contributed to the final count
    :param lst2: The list whose negative sum is contributed to the final count
    :return: The difference of sums of LST1 and LST2
    """
    return simple_sum(lst1) - simple_sum(lst2)


def subtract_lists(lst1, lst2):
    """
    Subtracts LST2 from LST1 elementwise, by recursively halving the lists and
    comparing them, and returns the sum of this operation.
    :param lst1: A list from which is subtracted LST2
    :param lst2: The list which is subtracted from LST1
    :return:
    """

    if len(lst1) == 0:
        return - sum_list(lst2)
    if len(lst2) == 0:
        return sum_list(lst1)
    if len(lst1) == 1 and len(lst2) == 1:
        return lst1[0] - lst2[0]
    else:
        split_index = len(lst1) // 2
        return subtract_lists(lst1[:split_index], lst2[:split_index]) \
               + subtract_lists(lst1[split_index:], lst2[split_index:])


def day_two_part_two(directions):
    """
    Computes the depth and horizontal position of the submarine after
    applying the rules according to day two part two.
    :param directions: Ordered list of string int tuple pairs, giving
    direction and distance.
    :return: The final aim, depth, and horizontal position of the sub.
    """
    aim, depth, forward = 0, 0, 0
    for direc, dist in directions:
        if direc == "down":
            aim += dist
        elif direc == "up":
            aim -= dist
        else:
            forward += dist
            depth += aim * dist
    return aim, depth, forward


if __name__ == "__main__":
    main()
