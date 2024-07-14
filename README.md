# Super5-Lottery-Simulator

A powerful and efficient lottery simulation tool to analyze the probability of matching numbers in a Super5 lottery game. This tool also provides functionalities to generate random lottery numbers for various popular lottery games.

## Features

- Generate random lottery numbers for Super5, Powerball, and Mega Millions.
- Run large-scale simulations to understand the probability of matching numbers.
- Visualize the results using interactive Plotly charts.
- Multi-processing support to speed up simulations using all available CPU cores.

## Requirements

- Python 3.x
- numpy
- tqdm
- plotly

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/CliveMlt/Super5-Lottery-Simulator.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Super5-Lottery-Simulator
    ```
3. Install the required packages:
    ```bash
    pip install numpy tqdm plotly
    ```

## Usage

Run the main script:
```bash
python lottery_sim1.py
python lottery_sim2.py
 ```

## Menu Options

1. **Super5**: Generate a random set of Super5 lottery numbers.
2. **Powerball**: Generate random Powerball lottery numbers.
3. **Mega Millions**: Generate random Mega Millions lottery numbers.
4. **Run Lottery Simulation**: Run a simulation to analyze the probability of matching numbers in a Super5 lottery game.
5. **Quit**: Exit the application.

## Lottery Simulation
#enerating Super5 Numbers
If you choose option 1, you will see something like:<br>
Super5: [2, 14, 25, 33, 45]

# Running a Simulation
If you choose option 4, the simulation will run and display the progress:<br>
```bash
Playing Super5...: 100%|██████████████████████████████████████████| 10000000/10000000 [01:00<00:00, 165593.17it/s]
```

After completion, the results will be printed:
```bash
Super5: [22, 3, 7, 8, 30]    
0 Matches: 5,471,343 (1 in 2)
1 Match: 3,505,012 (1 in 3)  
2 Matches: 900,833 (1 in 11)
3 Matches: 115,235 (1 in 87)
4 Matches: 7,382 (1 in 1,355)
5 Matches: 195 (1 in 51,282)
Total execution time: 60.39 seconds
```

An interactive bar chart will also be displayed showing the match counts.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
