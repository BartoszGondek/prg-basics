def f(dice):
    # Initialize variables to track the most frequent dice number and the longest streak
    max_num = dice[0]  # Assume the first dice roll is the most frequent at first
    max_streak = 1  # Minimum streak is 1 (since the first roll counts as a streak of 1)
    current_num = dice[0]
    current_streak = 1

    # Iterate through the dice string starting from the second character
    for i in range(1, len(dice)):
        if dice[i] == current_num:
            # If the current number is the same as the previous one, increment streak
            current_streak += 1
        else:
            # If the number changes, compare the current streak with max streak
            if current_streak > max_streak:
                max_streak = current_streak
                max_num = current_num
            # Reset current streak and set new number as the current number
            current_num = dice[i]
            current_streak = 1
    
    # Final check to update max_streak if the longest streak is at the end of the string
    if current_streak > max_streak:
        max_streak = current_streak
        max_num = current_num
    
    return int(max_num)


print (f("2133"))
