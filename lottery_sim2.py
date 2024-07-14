#With executor.submit

import numpy as np
import multiprocessing
import time
from tqdm import tqdm
import plotly.graph_objects as go
from concurrent.futures import ProcessPoolExecutor
import random

# Lottery simulation variables
chosenNumbers = np.array([22, 3, 7, 8, 30])
plays = 10000000
num_processes = multiprocessing.cpu_count()

#_______________________________________________________________________________________________________

# Lottery number generation class
class LotteryGen:
    @staticmethod
    def generate_numbers(start, end, count):
        """Generate a sorted list of unique random numbers within a specified range."""
        numbers = random.sample(range(start, end + 1), count)
        numbers.sort()
        return numbers

    @staticmethod
    def generate_multiple_sets(times, start, end, count):
        """Generate multiple sets of sorted unique random numbers within a specified range."""
        return [LotteryGen.generate_numbers(start, end, count) for _ in range(times)]

#_______________________________________________________________________________________________________

# Super5 Simulation class
class Super5Simulation:
    def __init__(self, chosen_numbers, plays, num_processes):
        self.chosen_numbers = chosen_numbers
        self.plays = plays
        self.num_processes = num_processes

    def play_lottery(self, start, end):
        """Simulate a single chunk of lottery plays."""
        local_match_counts = np.zeros(6, dtype=int)
        np.random.seed()  # Ensures a different seed in each process

        for _ in range(start, end):
            rolled_numbers = np.random.randint(1, 45, size=5)
            matches = np.sum(np.isin(rolled_numbers, self.chosen_numbers))

            local_match_counts[matches] += 1

        return local_match_counts

    def update_progress_bar(self, progress, pbar):
        """Update the progress bar."""
        pbar.update(progress)

    def print_results(self, match_counts):
        """Print the results of the simulation."""
        total_plays = sum(match_counts)
        odds = [total_plays / count if count > 0 else float('inf') for count in match_counts]

        print(f"Super5: {self.chosen_numbers.tolist()}")
        print(f"0 Matches: {match_counts[0]:,} (1 in {odds[0]:,.0f})")
        print(f"1 Match: {match_counts[1]:,} (1 in {odds[1]:,.0f})")
        print(f"2 Matches: {match_counts[2]:,} (1 in {odds[2]:,.0f})")
        print(f"3 Matches: {match_counts[3]:,} (1 in {odds[3]:,.0f})")
        print(f"4 Matches: {match_counts[4]:,} (1 in {odds[4]:,.0f})")
        print(f"5 Matches: {match_counts[5]:,} (1 in {odds[5]:,.0f})")

    def plot_results(self, match_counts):
        """Plot the results of the simulation."""
        categories = ['0 Matches', '1 Match', '2 Matches', '3 Matches', '4 Matches', '5 Matches']
        values = match_counts.tolist()
        
        fig = go.Figure()
        fig.add_trace(go.Bar(x=categories, y=values, name='Matches'))

        fig.update_layout(
            title='Lottery Matches Count',
            xaxis_title='Matches',
            yaxis_title='Counts',
            hovermode='x unified',  # Combine hover info for all bars at a given x
            barmode='group',  # Grouped bar chart
            legend=dict(x=0, y=1.0, bgcolor='rgba(255, 255, 255, 0.5)', bordercolor='rgba(255, 255, 255, 0.5)'),
            annotations=[
                dict(text='Matches Count', x=0.5, y=1.05, showarrow=False, xref='paper', yref='paper')
            ]
        )

        fig.show()

    def run_simulation(self):
        """Run the Super5 lottery simulation."""
        start_time = time.time()
        chunk_size = 10000
        total_chunks = self.plays // chunk_size
        match_counts = np.zeros(6, dtype=int)

        with tqdm(total=self.plays, desc="Playing Super5...") as pbar:
            with ProcessPoolExecutor(max_workers=self.num_processes) as executor:
                futures = []
                for i in range(total_chunks):
                    start = i * chunk_size
                    end = (i + 1) * chunk_size
                    futures.append(executor.submit(self.play_lottery, start, end))

                for future in futures:
                    local_counts = future.result()
                    match_counts += local_counts
                    self.update_progress_bar(chunk_size, pbar)

        self.print_results(match_counts)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Total execution time: {elapsed_time:.2f} seconds")

        self.plot_results(match_counts)

#_______________________________________________________________________________________________________

# Menu class to handle user interactions
class Menu:
    @staticmethod
    def display():
        """Display the menu options."""
        print('\n\nSelect an option:\n')
        print('1. Super5')
        print('2. Powerball')
        print('3. Mega Millions')
        print('4. Run Super5 Lottery Simulation')
        print('Q. Quit')

    @staticmethod
    def process_choice(choice):
        """Process the user's menu choice."""
        if choice == '1':
            print('\nSuper5:', LotteryGen.generate_numbers(1, 45, 5))
        elif choice == '2':
            print('\nPowerball:', LotteryGen.generate_numbers(1, 55, 5), LotteryGen.generate_numbers(1, 42, 1))
        elif choice == '3':
            print('\nMega Millions:', LotteryGen.generate_numbers(1, 75, 5), LotteryGen.generate_numbers(1, 15, 1))
        elif choice == '4':
            sim = Super5Simulation(chosenNumbers, plays, num_processes)
            sim.run_simulation()
        else:
            print("Invalid choice. Please try again.")

# Main worker function
def main_function():
    while True:
        Menu.display()
        choice = input('\nEnter your choice: ').lower()

        if choice.startswith('q'):
            print("Done! Thanks for playing.")
            break
        else:
            Menu.process_choice(choice)

#_______________________________________________________________________________________________________

if __name__ == '__main__':
    main_function()
