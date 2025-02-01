def fcfs_scheduling(processes):
    """
    First-Come, First-Served (FCFS) scheduling algorithm.
    """
    processes.sort(key=lambda x: x['arrival_time'])
    gantt_chart = []
    current_time = 0
    waiting_times = []

    for process in processes:
        if current_time < process['arrival_time']:
            current_time = process['arrival_time']
        gantt_chart.append((process['id'], current_time, current_time + process['burst_time']))
        waiting_times.append(current_time - process['arrival_time'])
        current_time += process['burst_time']

    return gantt_chart, waiting_times


def sjf_scheduling(processes, preemptive=False):
    """
    Shortest Job First (SJF) scheduling algorithm.
    """
    processes.sort(key=lambda x: (x['arrival_time'], x['burst_time']))
    gantt_chart = []
    current_time = 0
    waiting_times = []
    remaining_times = {p['id']: p['burst_time'] for p in processes}

    while any(remaining_times.values()):
        available = [
            p for p in processes
            if p['arrival_time'] <= current_time and remaining_times[p['id']] > 0
        ]
        if not available:
            current_time += 1
            continue

        selected = min(available, key=lambda x: x['burst_time'] if not preemptive else remaining_times[x['id']])
        gantt_chart.append((selected['id'], current_time, current_time + 1))
        remaining_times[selected['id']] -= 1
        current_time += 1

        if remaining_times[selected['id']] == 0:
            waiting_times.append(current_time - selected['arrival_time'] - selected['burst_time'])

    return gantt_chart, waiting_times


def round_robin_scheduling(processes, time_quantum):
    """
    Round Robin scheduling algorithm.
    """
    processes.sort(key=lambda x: x['arrival_time'])
    gantt_chart = []
    current_time = 0
    waiting_times = []
    remaining_times = {p['id']: p['burst_time'] for p in processes}
    queue = []

    while any(remaining_times.values()) or queue:
        for p in processes:
            if p['arrival_time'] <= current_time and remaining_times[p['id']] > 0 and p not in queue:
                queue.append(p)

        if not queue:
            current_time += 1
            continue

        current_process = queue.pop(0)
        execution_time = min(time_quantum, remaining_times[current_process['id']])
        gantt_chart.append((current_process['id'], current_time, current_time + execution_time))
        remaining_times[current_process['id']] -= execution_time
        current_time += execution_time

        if remaining_times[current_process['id']] > 0:
            queue.append(current_process)
        else:
            waiting_times.append(current_time - current_process['arrival_time'] - current_process['burst_time'])

    return gantt_chart, waiting_times


def priority_scheduling(processes):
    """
    Priority Scheduling algorithm.
    """
    processes.sort(key=lambda x: (x['arrival_time'], x['priority']))
    gantt_chart = []
    current_time = 0
    waiting_times = []

    for process in processes:
        if current_time < process['arrival_time']:
            current_time = process['arrival_time']
        gantt_chart.append((process['id'], current_time, current_time + process['burst_time']))
        waiting_times.append(current_time - process['arrival_time'])
        current_time += process['burst_time']

    return gantt_chart, waiting_times


if __name__ == "__main__":
    # Sample processes
    processes = [
        {"id": 1, "arrival_time": 0, "burst_time": 5, "priority": 2},
        {"id": 2, "arrival_time": 1, "burst_time": 3, "priority": 1},
        {"id": 3, "arrival_time": 2, "burst_time": 8, "priority": 3},
    ]

    # Test FCFS
    print("FCFS:")
    gantt_chart, waiting_times = fcfs_scheduling(processes)
    print("Gantt Chart:", gantt_chart)
    print("Waiting Times:", waiting_times)

    # Test SJF
    print("\nSJF:")
    gantt_chart, waiting_times = sjf_scheduling(processes)
    print("Gantt Chart:", gantt_chart)
    print("Waiting Times:", waiting_times)

    # Test Round Robin
    print("\nRound Robin:")
    gantt_chart, waiting_times = round_robin_scheduling(processes, time_quantum=3)
    print("Gantt Chart:", gantt_chart)
    print("Waiting Times:", waiting_times)

    # Test Priority Scheduling
    print("\nPriority Scheduling:")
    gantt_chart, waiting_times = priority_scheduling(processes)
    print("Gantt Chart:", gantt_chart)
    print("Waiting Times:", waiting_times)