from sys import argv

def cat_shelter():
    """Calculating amount of time for cats in a cat shelter in addition to the total, average, longest and shortest time."""
    total_time = 0
    our_cat = 0
    name = ["OURS", "THEIRS"]
    our_cat_time = []
    their_cat = 0

    try:
        # the variable argument takes the first index of command line argument.
        argument = argv[1]
        with open(argument, "r") as file:
            for line in file:
                row = line.strip().split(",")
                
                try:             
                    if name[0] in line:

                        number = int(row[1])
                        number1 = int(row[2])

                        sub = number1 - number
                        our_cat_time.append(sub)

                        total_time += sub
                        our_cat += 1

                    elif name[1] in line:
                        their_cat += 1

                except IndexError:
                    break
        # creates a new sorted list of the original list if the original list is needed.
        sorted_our_cat_time = sorted(our_cat_time)

        print(f"Cat Visits: {our_cat}")
        print(f"Other Cats: {their_cat} \n")

        print(f"Total Time in House: {total_time//60} Hours, {total_time%60} minutes\n")

        print(f"Average Visit Length: {total_time//our_cat} Minutes")
        print(f"Longest Visit: {sorted_our_cat_time[-1]:9} Minutes")
        print(f"Shortest Visit: {sorted_our_cat_time[0]:7} Minutes\n")

    except IndexError:
            print("Missing command line argument!")
    except FileNotFoundError:
            print(f"Cannot open \"{argument}\"!")


cat_shelter()