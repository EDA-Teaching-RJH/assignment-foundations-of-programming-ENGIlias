Bug 1: Infinite loop (loading) - The while loading < 5: loop was stuck forever because the variable loading was never increased. It stayed at 0, so the condition 0 < 5 was always true.

Bug 2: Syntax Error - The line if opt = "1": used a single equals sign (=), which Python uses for assigning values (like x = 5). To check if two things are equal, you must use double equals (==).

Bug 3: Index Error - The loop for i in range(10): tried to count up to 10 items, but our list only had 4 names. When it tried to access item #5 (index 4), Python crashed because that item didn't exist.

Bug 4: Logic Error - The code said if rank == "Captain" or "Commander":. Python reads this as "If the rank is Captain OR if the word 'Commander' exists." Since the word "Commander" always exists, this check was always True for everyone.

Bug 5: Type Error - The code tried to add a number to a string: "Officers: " + count. Python doesn't know how to add text and math together. I had to turn the number into text using str(count).

Bug 6: Logic Error (Add Crew) - When adding a new crew member, the old code only added their Name to the list. It forgot to add their Rank and Division, which meant the lists became different lengths and didn't match up anymore.

Bug 7: Syntax Error - The very last line said run_system_monolith without parentheses (). In Python, if you don't put () at the end, the function doesn't actually run.

Bug 8: Logic Error (Remove Crew) - The removal code assumed the name you typed was always in the list. If you typed a name that wasn't there (like "Kirk"), the program crashed. I added a check to see if the name existed first.

Bug 9: Logic Error (Fuel) - The fuel loop had a break command right at the start. This meant the loop ran once and then immediately stopped, making the loop completely useless.

Bug 10: Syntax Error (Colon) - Several lines like if x > 5 were missing the colon (:) at the end. In Python, you need a colon to tell the computer "Okay, here comes the code block for this if statement."