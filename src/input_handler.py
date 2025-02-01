import json

def get_user_input():
    """
    Function to get process details and algorithm choice from the user.
    """
    print("=== CPU Scheduling Simulator ===")
    print("1. Enter new process details")
    print("2. Load saved process details")
    choice = int(input("Enter your choice (1-2): "))

    if choice == 1:
        num_processes = int(input("Enter the number of processes: "))
        processes = []

        for i in range(num_processes):
            print(f"\nProcess {i + 1}:")
            arrival_time = int(input("Enter arrival time: "))
            burst_time = int(input("Enter burst time: "))
            priority = int(input("Enter priority (lower value = higher priority): "))
            processes.append({
                "id": i + 1,
                "arrival_time": arrival_time,
                "burst_time": burst_time,
                "priority": priority
            })

        save_choice = input("Do you want to save these inputs? (y/n): ")
        if save_choice.lower() == "y":
            save_inputs(processes)

    elif choice == 2:
        processes = load_inputs()
        if not processes:
            print("No saved inputs found. Please enter new process details.")
            return get_user_input()

    print("\nSelect a scheduling algorithm:")
    print("1. FCFS (First-Come, First-Served)")
    print("2. SJF (Shortest Job First)")
    print("3. Round Robin")
    print("4. Priority Scheduling")
    algo_choice = int(input("Enter your choice (1-4): "))

    if algo_choice == 3:  # Round Robin requires time quantum
        time_quantum = int(input("Enter time quantum for Round Robin: "))
        return processes, algo_choice, time_quantum

    return processes, algo_choice, None


def save_inputs(processes, filename="inputs.json"):
    """
    Saves process inputs to a JSON file.
    """
    with open(filename, "w") as f:
        json.dump(processes, f)
    print(f"Inputs saved to {filename}.")


def load_inputs(filename="inputs.json"):
    """
    Loads process inputs from a JSON file.
    """
    try:
        with open(filename, "r") as f:
            processes = json.load(f)
        print(f"Inputs loaded from {filename}.")
        return processes
    except FileNotFoundError:
        print("No saved inputs found.")
        return None


if __name__ == "__main__":
    processes, algo_choice, time_quantum = get_user_input()
    print("\nProcesses:", processes)
    print("Algorithm Choice:", algo_choice)
    print("Time Quantum:", time_quantum)