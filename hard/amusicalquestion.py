def merge(nums, c):
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if nums[i] + nums[j] <= c:
                nums[j] = nums[j] + nums[i]
                nums.pop()
                return nums, True
            print(nums)
    return nums, False


def main():
    c, _ = map(int, input().split())
    nums = [int(x) for x in input().split()]
    while len(nums) > 2:
        change = False
        print("Main Loop")
        nums, change = merge(nums, c)
        if not change:
            nums.remove(min(nums))
    nums.sort(reverse=True)
    print(*nums)


if __name__ == "__main__":
    main()
