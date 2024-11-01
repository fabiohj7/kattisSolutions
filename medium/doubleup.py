def merge(run):
    for i in range(len(run) - 1):
        if run[i] == run[i + 1]:
            run[i] = run[i] + run[i + 1]
            run.remove(run[i + 1])
            return run, True
    return run, False


def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    while len(nums) > 1:
        merged = False
        nums, merged = merge(nums)

        if not merged:
            nums.remove(min(nums))
            n -= 1
    print(nums[0])


if __name__ == "__main__":
    main()
