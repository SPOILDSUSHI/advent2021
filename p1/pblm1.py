
def count_increase(nums):
    count = 0
    for index, num in enumerate(nums):
        if index == 0:
            continue
        elif num > nums[index-1]:
            count += 1
    return count


def create_windows_list(nums, window=3):
    return [nums[i:i+window] for i in range(len(nums) - window + 1)]


if __name__ == "__main__":
    # with open("input_p1_1.txt") as input:
    #     line_list = input.readlines()
    # nums_list = list(map(int, line_list))
    # print(count_increase(nums_list))
    with open("input_p1_2.txt") as input:
        line_list = input.readlines()
    nums_list = list(map(int, line_list))
    windows_list = create_windows_list(nums_list, 3)
    sum_list = list(map(sum, windows_list))
    print(count_increase(sum_list))
