class Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time

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


def fcfs_scheduling(processes):
    n = len(processes)
    processes.sort(key=lambda x: x.arrival_time)  # Sort processes based on arrival time

    print("FCFS Scheduling:\n")
    print("Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")

    for i in range(n):
        process = processes[i]
        print(
            f"{process.process_id}\t\t{process.arrival_time}\t\t{process.burst_time}\t\t",
            end="",
        )

        if i == 0:
            waiting_time = 0
        else:
            waiting_time = processes[i - 1].burst_time + processes[i - 1].arrival_time

        print(f"{waiting_time}\t\t{waiting_time + process.burst_time}")

    average_waiting_time, average_turnaround_time = calculate_average_time(processes)
    print("\nAverage Waiting Time:", average_waiting_time)
    print("\nAverage Turnaround Time:", average_turnaround_time)


if __name__ == "__main__":
    processes = [
        Process(1, 0, 5),
        Process(2, 2, 3),
        Process(3, 4, 6),
        Process(4, 6, 4),
        Process(5, 8, 2),
    ]

    fcfs_scheduling(processes)

    # print(f"Avg WT: {average_waiting_time}")
