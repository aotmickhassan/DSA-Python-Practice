class Process:
    def __init__(self, process_id, arrival_time, burst_time, priority):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority

    def __repr__(self):
        return f"Process {self.process_id}"


def calculate_waiting_time(processes):
    n = len(processes)
    waiting_time = [0] * n
    total_waiting_time = 0

    for i in range(1, n):
        waiting_time[i] = processes[i - 1].burst_time + waiting_time[i - 1]
        total_waiting_time += waiting_time[i]

    return waiting_time, total_waiting_time


def calculate_turnaround_time(processes, waiting_time):
    n = len(processes)
    turnaround_time = [0] * n
    total_turnaround_time = 0

    for i in range(n):
        turnaround_time[i] = processes[i].burst_time + waiting_time[i]
        total_turnaround_time += turnaround_time[i]

    return turnaround_time, total_turnaround_time


def calculate_average_time(processes):
    waiting_time, total_waiting_time = calculate_waiting_time(processes)
    turnaround_time, total_turnaround_time = calculate_turnaround_time(
        processes, waiting_time
    )
    n = len(processes)

    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n

    return average_waiting_time, average_turnaround_time


def priority_scheduling(processes):
    n = len(processes)
    processes.sort(
        key=lambda x: (x.arrival_time, x.priority)
    )  # Sort processes based on arrival time and priority

    print("Priority Scheduling:")
    print(
        "Process ID\tArrival Time\tBurst Time\tPriority\tWaiting Time\tTurnaround Time"
    )

    average_waiting_time, average_turnaround_time = calculate_average_time(processes)

    for i in range(n):
        process = processes[i]
        print(
            f"{process.process_id}\t\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.priority}\t\t",
            end="",
        )
        print(f"{average_waiting_time}\t\t{process.burst_time + average_waiting_time}")

    print("\nAverage Waiting Time:", average_waiting_time)
    print("Average Turnaround Time:", average_turnaround_time)


# Example usage
if __name__ == "__main__":
    # Create a list of processes
    processes = [
        Process(1, 0, 5, 3),
        Process(2, 2, 3, 1),
        Process(3, 4, 6, 4),
        Process(4, 6, 4, 2),
        Process(5, 8, 2, 5),
    ]

    priority_scheduling(processes)
