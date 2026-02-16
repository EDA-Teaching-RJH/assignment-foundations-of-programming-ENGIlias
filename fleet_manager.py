def init_database():
    names = ["Alice", "Bob", "Charlie", "Diana"]
    ranks = ["Captain", "Lieutenant", "Commander"]
    divs = ["Command", "Operations", "Security", "Engineering", "Medical", "Science"]
    ids  = [1001, 1002, 1003, 1004, 1005, 1006]
    return names, ranks, divs, ids
    #create parallel lists for crew names and ranks
    pass

def display_roster(names, ranks, divs, ids):
    #display the crew roster
    pass

def add_member(names, ranks, divs, ids):
    #add a member to the crew
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
    print("FLEET MANAGER")

    names, ranks, divisions, ids = init_database()

    while True:
        print("\n--- MENU ---")
        print("1. Display Roster")
        print("2. Add Member")
        print("3. Remove Member")
        print("4. Update Rank")
        print("5. Search")
        print("6. Filter by Division")
        print("7. Payroll")
        print("8. Count Officers")
        print("9. Exit")

        opt = input("Select: ")

        #should work call function based on input
        pass
        

main()#run program