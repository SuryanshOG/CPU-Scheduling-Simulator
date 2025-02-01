import matplotlib.pyplot as plt
import plotly.express as px

def visualize_gantt_chart(gantt_chart):
    """
    Visualizes the Gantt chart using Plotly with animations.
    """
    # Prepare data for Plotly
    df = []
    for pid, start, end in gantt_chart:
        df.append(dict(Process=f"P{pid}", Start=start, Finish=end))

    # Create the animated Gantt chart
    fig = px.timeline(
        df,
        x_start="Start",
        x_end="Finish",
        y="Process",
        title="Animated Gantt Chart",
        labels={"Process": "Processes"},
        animation_frame="Start"  # Enables animation based on start times
    )
    fig.update_yaxes(categoryorder="total ascending")  # Sort processes by their order
    fig.show(renderer="browser")


def calculate_metrics(waiting_times, processes):
    """
    Calculates average waiting time and turnaround time.
    """
    avg_waiting_time = sum(waiting_times) / len(waiting_times)
    turnaround_times = [wt + p['burst_time'] for wt, p in zip(waiting_times, processes)]
    avg_turnaround_time = sum(turnaround_times) / len(turnaround_times)
    return avg_waiting_time, avg_turnaround_time

if __name__ == "__main__":
    # Sample Gantt chart data
    gantt_chart = [(1, 0, 5), (2, 5, 8), (3, 8, 16)]

    # Test animated Gantt chart visualization
    print("Displaying Animated Gantt Chart...")
    visualize_gantt_chart(gantt_chart)