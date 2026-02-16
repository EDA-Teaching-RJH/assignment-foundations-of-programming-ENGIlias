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
    #remove a member from the crew
    pass

def update_rank(names, ranks, divs, ids):
    #update a crew member's rank
    pass

def search_crew(names, ranks, divs, ids):
    #search for a crew member by name
    pass

def filter_by_division(names, divs):
    #filter crew members by division
    pass

def calculate_payroll(names, divs):
    #calculate pay based on rank
    pass

def count_officers(ranks):
    #count the number of officers in the crew
    pass

def main():


main()#run program