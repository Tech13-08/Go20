import matplotlib.pyplot as plt

def generate_bar_graph():
    # Load data from "daily_screen_time.txt"
    with open("daily_screen_time.txt", "r") as result_file:
        lines = result_file.readlines()

    # Extract days and hours from the data
    days = list(range(1, len(lines) + 1))
    hours = [float(line.strip()) for line in lines]


    # Set the size of the plot area
    plt.figure(figsize=(8, 6))

    # Plot the bar graph
    plt.bar(days, hours, color='skyblue', edgecolor='black')  
    plt.title('Daily Screen Time')
    plt.xlabel('Day')
    plt.ylabel('Screen Time (hours)')
    plt.ylim(bottom=0)

    # Save the bar graph
    plt.savefig('screen_time_bar_graph.png')
    plt.close()

if __name__ == "__main__":
    generate_bar_graph()
