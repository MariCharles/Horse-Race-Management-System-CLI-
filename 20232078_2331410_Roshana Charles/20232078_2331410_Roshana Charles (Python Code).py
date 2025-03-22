import random

print("Welcome to the Most anticipated event in the town: 'Rapid Run'\n")
print('''----------Operations----------\n
    AHD   Add Horse Details
    UHD   Update Horse Details
    DHD   Delete Horse Details
    VHD   View Horse Details
    SHD   Save Horse Details
    SDD   Select Four Horses Randomly
    WHD   Winning Horses' Details
    VWH   Visualize Winning Horse
    ESC   Exit''')

horse_details=[]

def load_horse_details_from_file(file_path):
    loaded_horse_details = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                fields = line.strip().split()
                horse = {
                    "Horse ID": fields[0],
                    "Horse Name": fields[1],
                    "Jockey Name": fields[2],
                    "Age": fields[3],
                    "Breed": fields[4],
                    "Race Record": fields[5],
                    "Group": fields[6]
                }
                loaded_horse_details.append(horse)
        print("Horse details loaded successfully.")
    except FileNotFoundError:
        print("File not found. No horse details loaded.")
    except Exception as e:
        print(f"An error occurred while loading horse details: {e}")

    return loaded_horse_details

file_path = "D:\\Users\\WIN XI\\PycharmProjects\\pythonProject1\\horse_details.txt"
horse_details = load_horse_details_from_file(file_path)

def add_horse_details():
    horse_id=input("Enter Horse ID: ")
    horse_name=input("Enter Horse Name: ")
    jockey_name=input("Enter Jockey Name: ")
    age=input("Enter Age: ")
    breed=input("Enter Breed: ")
    race_record=input("Enter Race Record: ")
    group=input("Enter group: ")

    horse_details.append({"Horse ID": horse_id, "Horse Name": horse_name, "Jockey Name": jockey_name, "Age": age, "Breed": breed, "Race Record": race_record, "Group": group})

def update_horse_details():
    horse_id = input("Enter the ID of the Horse to Update: ")

    global horse_details

    for horse in horse_details:
        if horse["Horse ID"] == horse_id:
            horse["Horse Name"] = input("Enter Updated Horse Name: ")
            horse["Jockey Name"] = input("Enter Updated Jockey Name: ")
            horse["Age"] = input("Enter Updated Age: ")
            horse["Breed"] = input("Enter Updated Breed: ")
            horse["Race Record"] = input("Enter Updated Race Record: ")
            horse["Group"] = input("Enter Updated Group: ")
            print("Horse Details Updated Successfully!")
            save_horse_details()
            return

    print("Horse does not Exist.")

def delete_horse_details():
    horse_id = input("Enter the ID of the Horse to Delete: ")

    global horse_details

    for horse in horse_details:
        if horse["Horse ID"] == horse_id:
            horse_details.remove(horse)
            print("Horse Details Deleted Successfully!")
            save_horse_details()
            return

    print("Horse does not Exist.")

def view_horse_details():

    def sort_horse_details(horse_details):
        n = len(horse_details)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if horse_details[j]['Horse ID'] > horse_details[j + 1]['Horse ID']:
                    temp = horse_details[j]
                    horse_details[j] = horse_details[j + 1]
                    horse_details[j + 1] = temp

    sort_horse_details(horse_details)

    print("{:<10} {:<20} {:<20} {:<10} {:<20} {:<15} {:<10}".format("Horse ID", "Horse Name", "Jockey Name",
                                                                   "Age", "Breed", "Race Record", "Group"))
    print("-" * 105)

    for horse in horse_details:
        print("{:<10} {:<20} {:<20} {:<10} {:<20} {:<15} {:<10}".format(horse['Horse ID'], horse['Horse Name'], horse['Jockey Name'], horse['Age'], horse['Breed'], horse['Race Record'], horse['Group']))

def save_horse_details():

    def sort_horse_details(horse_details):
        n = len(horse_details)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if horse_details[j]['Group'] > horse_details[j + 1]['Group']:
                    temp = horse_details[j]
                    horse_details[j] = horse_details[j + 1]
                    horse_details[j + 1] = temp

    sort_horse_details(horse_details)

    f = open('horse_details.txt', 'w')
    for horse in horse_details:
        f.write(f"{horse['Horse ID']}  {horse['Horse Name']}  {horse['Jockey Name']}  {horse['Age']}  {horse['Breed']}  {horse['Race Record']}  {horse['Group']}\n")
    f.close()
    print("Horse Details Saved to horse_details.txt Successfully!")

selected_horses=[]

def select_horses():
    try:
        unique_group = set(horse['Group'] for horse in horse_details)

        for group in unique_group:
            group_horse = [horse for horse in horse_details if horse['Group'] == group]

            try:
                selected_horse = random.choice(group_horse)
                selected_horses.append(selected_horse)
            except IndexError:
                print(f"Error: No horses found in group {group}. Skipping this group.")

        print("Horses are Selected")
        print(selected_horses)
    except Exception as e:
        print(f"An error occurred: {e}")

def display_winning_horses():

    import random
    def assign_random_times(selected_horses):
        for horse in selected_horses:
            horse['Race Time'] = random.randint(0, 90)

    def sort_horses_by_race_time(selected_horses):
        n = len(selected_horses)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if selected_horses[j]['Race Time'] > selected_horses[j + 1]['Race Time']:
                    selected_horses[j], selected_horses[j + 1] = selected_horses[j + 1], selected_horses[j]

    assign_random_times(selected_horses)
    sort_horses_by_race_time(selected_horses)

    print("\nFinal Positions:")
    print("{:<10} {:<20} {:<10}".format("Horse ID", "Horse Name", "Race Time"))
    print("-" * 40)

    positions = ["1st", "2nd", "3rd"]
    i = 0
    while i < len(positions):
        horse = selected_horses[i]
        print("{:<10} {:<20} {:<10}".format(horse['Horse ID'], horse['Horse Name'], horse['Race Time']))
        i += 1

def visualize_winning_horses():
    def get_position_text(horse):
        race_times = [h['Race Time'] for h in selected_horses]

        min_race_time = min(race_times)
        second_min_race_time = min(val for val in race_times if val != min_race_time)
        third_min_race_time = min(val for val in race_times if val != min_race_time and val != second_min_race_time)

        if horse['Race Time'] == min_race_time:
            return "1st"
        elif horse['Race Time'] == second_min_race_time:
            return "2nd"
        elif horse['Race Time'] == third_min_race_time:
            return "3rd"

    def visualize_race_time(horse):
        position = get_position_text(horse)
        if position:
            bar_length = horse['Race Time'] // 10
            stars = '*' * bar_length
            print(f"{horse['Horse Name']}: {stars} {horse['Race Time']}s ({position} Place)")

    for horse in selected_horses:
        visualize_race_time(horse)

while True:
    user_input=input("What would you like to do? ").upper()
    if user_input=='AHD':
        add_horse_details()
    elif user_input=='UHD':
        update_horse_details()
    elif user_input=='DHD':
        delete_horse_details()
    elif user_input=='VHD':
        view_horse_details()
    elif user_input=='SHD':
        save_horse_details()
    elif user_input=='SDD':
        select_horses()
    elif user_input=='WHD':
        display_winning_horses()
    elif user_input=='VWH':
        visualize_winning_horses()
    elif user_input=='ESC':
        print("Exiting...Thank You for Your Cooperation!")
        break
    else:
        print("Invalid Action. Please Try Again.")
