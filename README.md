# Monte Carlo Integration GUI

## Table of Contents

* [Overview](#overview)
* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [How It Works](#how-it-works)

  * [Monte Carlo Integration](#monte-carlo-integration)
  * [GUI Components](#gui-components)
* [Code Structure](#code-structure)
* [Example](#example)
* [Dependencies](#dependencies)
* [License](#license)

## Overview

Monte Carlo Integration GUI is a Python application that provides an intuitive graphical interface for performing Monte Carlo integration—a probabilistic method for approximating the area under a curve (definite integral). It allows users to input a function, specify integration bounds, and choose the number of random points for the simulation.

## Features

* User-friendly GUI using `tkinter`.
* Monte Carlo integration for approximating definite integrals.
* Customizable function input and integration range.
* Adjustable number of random points for calculation.
* Real-time visualization of Monte Carlo points (green for points under the curve, red for points above).
* Numerical results displayed, including the integral approximation, rectangle area, and error estimate.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/monte-carlo-integration-gui.git
   cd monte-carlo-integration-gui
   ```

2. **Install Dependencies:**

   ```bash
   pip install matplotlib
   ```

3. **Run the Application:**

   ```bash
   python monte_carlo_integration_gui.py
   ```

## Usage

1. Launch the application.
2. Enter the following inputs in the GUI:

   * **Function:** A mathematical function (e.g., `x**2`, `math.sin(x)`).
   * **Number of Points:** Number of random points for Monte Carlo simulation.
   * **Range Start (a):** Lower bound of integration.
   * **Range End (b):** Upper bound of integration.
3. Click the "Calculate" button.
4. View the results and plot in the GUI.

## How It Works

### Monte Carlo Integration

The Monte Carlo integration method uses random points to estimate the area under a curve (definite integral). It follows these steps:

* Randomly generates points within a defined region.
* Counts points under the curve.
* Calculates the proportion of points under the curve to approximate the integral.

### GUI Components

* **Input Fields:** Function, number of points, range start (a), and range end (b).
* **Calculate Button:** Starts the integration process.
* **Results Section:** Displays the calculated integral, rectangle area, area under/above the curve, and error.
* **Visualization:** A matplotlib plot showing the function and Monte Carlo points.

## Code Structure

* `monte_carlo_integration.py`: Contains the Monte Carlo integration logic.
* `monte_carlo_integration_gui.py`: Defines the GUI interface using `tkinter`.

## Example

To approximate the integral of `f(x) = x^2` from `x = 0` to `x = 1`:

1. Enter `x**2` in the function field.
2. Enter `1000` for the number of points.
3. Enter `0` for Range Start (a) and `1` for Range End (b).
4. Click "Calculate".

## Dependencies

* Python 3.x
* `tkinter` (included with Python)
* `matplotlib`

