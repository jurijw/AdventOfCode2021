from recursion import recursionlimit


def main():
    with open("Inputs/input1.txt", "r") as f:
        data = [int(depth.strip()) for depth in f.readlines()]

        # PART A

        def differences(lst, count=0):
            """
            Calculate the number of sequential increases in a list of numbers.
            :param lst: List of numbers, which are checked for differences.
            :param count: Internal parameter that tracks the number of differences.
            :return: count: The number of sequential increases.
            """
            if len(lst) <= 1:
                return count
            else:
                if lst[-1] > lst[-2]:
                    count += 1
                return differences(lst[:-1], count)

        with recursionlimit(len(data) + 3):
            print("------Differences Method------")
            print(f"Number of depth increases: {differences(data)}")
            print(f"Requires a recursion depth of: {len(data) + 3}")

        def double_ended_differences(lst, count=0):
            """
            Calculate the number of sequential increases in a list of numbers.
            'Double-Ended' approach, in which the list is 'eaten away' at from
            both sides.
            :param lst: List of numbers, which are checked for differences.
            :param count: Internal parameter that tracks the number of differences.
            :return: The number of sequential increases.
            """
            if len(lst) <= 1:
                return count
            elif len(lst) == 2:
                return count + int(lst[0] < lst[1])
            else:
                if lst[-2] < lst[-1]:
                    count += 1
                if lst[0] < lst[1]:
                    count += 1
                return double_ended_differences(lst[1:-1], count)

        with recursionlimit(len(data) // 2 + 4):
            print("---Double-Ended Differences Method---")
            print(f"Number of depth increases: {double_ended_differences(data)}")
            print(f"Requires a recursion depth of: {len(data) // 2 + 4}")

        def split_differences(lst, count=0):
            """
            Calculate the number of sequential increases in a list of numbers.
            Splits the list in half recursively, checking for an increase at the split.
            :param lst: List of numbers, which are checked for differences.
            :param count: Internal parameter that tracks the number of differences.
            :return: The number of sequential increases.
            """
            if len(lst) <= 1:
                return count
            else:
                split_index = len(lst) // 2
                if lst[split_index - 1] < lst[split_index]:
                    count += 1
                return count + split_differences(lst[:split_index]) + split_differences(lst[split_index:])

        print("Split Differences")
        print(f"Number of depth increases: {split_differences(data)}")
        print("No additional recursion depth required!")

        # PART B
        # Despite the problem asking for us to compare sums of sets of 3 consecutive depths,
        # because any two consecutive sets share two numbers in common, we can just compare
        # the 1st to 4th depth, the 2nd to 5th depth, and so on, without having to compare
        # the elements in between.

        def group_differences(lst, count=0):
            """
            Calculate the number of increases in consecutive sums of 3 numbers.
            Uses the fact that doing so corresponds to comparing every element, to
            the number 3 indices higher.
            :param lst: List of numbers, which are checked for differences.
            :param count: Internal parameter that tracks the number of differences.
            :return: The number of increases in consecutive sums of 3 numbers.
            """
            if len(lst) <= 3:
                return count
            else:
                if lst[-4] < lst[-1]:
                    count += 1
                return group_differences(lst[:-1], count)

        with recursionlimit(len(data) + 1):
            print("----Group Differences Method----")
            print(f"Number of increases in consecutive sums of 3 depths: {group_differences(data)}")
            print(f"Requires a recursion depth of: {len(data) + 1}")




if __name__ == "__main__":
    main()
