# BTC Price Monitoring Automation with Selenium and Behave

This project is designed to monitor the prices of Bitcoin (BTC) at given time intervals over a specified duration. The
automation is implemented using Selenium for browser interaction, Python for scripting, and Behave for behavior-driven
development (BDD).

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed on your local machine.
- Pip (Python package installer).
- Google Chrome browser.
- ChromeDriver (compatible with your Chrome version).

## Installation

1. Clone the Repository:
```
git clone https://github.com/petyank/price_monitorning_python.git
cd price_monitorning_python
```
2. Install the required packages:
```
pip install -r requirements.txt
```
4. Download and place ChromeDriver:
   - Download the appropriate ChromeDriver.
   - Place the ChromeDriver executable in a directory that is in your system's PATH or in the project directory.

## Usage

1. For running the tests, run the following command:
```
behave
```
This command will execute the BDD test scenarios defined in the features directory.

## Project Structure

- features/: Contains the feature files and step definitions.
- environment.py: Setup and teardown configurations for Behave.
- steps/: Directory containing step definition Python files.
- priceMonitoring.feature: The feature file containing BDD scenarios for BTC price monitoring.
- pages/: Page Object Model (POM) scripts.
- finance_page.py: Script representing the finance page containing the BTC price element.
- support/: Utility scripts.
- utils.py: Utility functions for the project.
- tests/: Directory containing test scripts.
- test_script.py: Example test script.
- chrome_config.py: Configuration and setup for ChromeDriver.
- config.ini: Configuration file for application settings.
- config.json: Configuration file for customizable settings related the page to open and default timeout.
- requirements.txt: List of Python dependencies.
- README.md: Project documentation.

## Contributing

Contributions are always welcome! Please follow these steps:

1. Fork the repository.
2. Create your feature branch.
3. Commit your changes.
4. Push to the branch.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
