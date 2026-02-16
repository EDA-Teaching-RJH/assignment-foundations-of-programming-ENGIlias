def init_database():
    # Basic with 5 items each
    names = ["Picard", "Riker", "Data", "Worf", "La Forge"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Jr. Lieutenant"]
    divs = ["Science", "Engineering", "Operations", "Security", "Medic"]
    ids = [101, 102, 103, 104, 105]
    return names, ranks, divs, ids

def display_menu():
    #display menu and get user input
    user = input("Enter your name: ")
    print("User: " + user)
    print("1. Display Roster")
    print("2. Add Member")
    print("3. Remove Member")
    print("4. Update Rank")
    print("5. Search Crew")
    print("6. Filter by Division")
    print("7. Calculate Payroll")
    print("8. Count Officers")
    print("9. Exit")
    
    choice = input("Select option: ")
    return choice

def display_roster(names, ranks, divs, ids):


def add_member(names, ranks, divs, ids):
    new_name = input("Name: ")
    new_rank = input("Rank: ")
    new_div = input("Division: ")
    new_id = int(input("ID: "))
    #add a member to the crew
    if new_id in ids:
        print("ID already exists. Member not added.")
        return
    
    #check if rank is valid
    valid_ranks = ["Captain", "Commander", "Lieutenant"]
    if new_rank not in valid_ranks:
        print("Invalid rank. Member not added.")
        return
    
    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_div)
    ids.append(new_id)
    print("Member added.")
    pass

def remove_member(names, ranks, divs, ids):
    target = int(input("Enter ID to remove: "))
    
    if target in ids:
        idx = ids.index(target)
        # Remove from all
        names.pop(idx)
        ranks.pop(idx)
        divs.pop(idx)
        ids.pop(idx)
        print("Removed.")
    else:
        print("ID not found.")

def update_rank(names, ranks, divs, ids):
    target = int(input("Enter ID: "))
    
    if target in ids:
        idx = ids.index(target)
        new_rank = input("New Rank: ")
        ranks[idx] = new_rank
        print("Updated.")
    else:
        print("Not found.")

def search_crew(names, ranks, divs, ids):
    search = input("Enter name: ")
    
    for i in range(len(names)):
        if search in names[i]:
            print("Found: " + names[i])

def filter_by_division(names, divs):
    target = input("Enter Division: ")
    
    for i in range(len(divs)):
        if divs[i] == target:
            print(names[i])

def calculate_payroll(names, divs):
    #calculate pay based on rank
    pass

def count_officers(ranks):
    #count the number of officers in the crew
    pass

def main():


main()#run program