# SEO & Page Response Regression Test Automation

This project automates the comparison of SEO metadata between a staging site and a production site using Playwright and Python. It takes URLs from a CSV file, captures screenshots, compares SEO tags (like meta description, OpenGraph tags, etc.), and generates HTML reports for better visualization.

## Table of Contents
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [SEO Comparison Flow](#seo-comparison-flow)
- [Styling Reports](#styling-reports)
- [Running the Tests](#running-the-tests)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.11
- Playwright
- Pandas
- Openpyxl

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/seo-regression.git
cd seo-regression
```

### Step 2: Install the dependencies

1. **Install Python dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

2. **Install Playwright dependencies and browsers:**

    ```bash
    playwright install
    ```

## Project Structure

```plaintext
.
├── services/
│   └── seo_service.py               # Core service to run SEO comparison tests
├── pages/
│   └── seo_page.py                  # Page Object Model (POM) for SEO testing
├── utils/
│   ├── comparator.py                # Logic for comparing SEO metadata between Staging and Prod
│   └── csv_reader.py                # Utility to read URLs from CSV files\
│   └── report_styling.py            # Class for styling comparison reports
├── main.py                          # Entry point for running the script
├── requirements.txt                 # Python dependencies file
└── README.md                        # Project documentation
```

## Usage

### Prepare the URLs CSV file:

Ensure that the URLs you want to check are listed in a CSV file. The first column should contain the URLs for comparison.

### Run the script:

Execute the following command to start the SEO comparison test:

```bash
python main.py
```
- The script will prompt for the CSV file path, the production domain URL, and the staging domain URL.
- Example:
  ```bash
   Enter your .csv file path where all URLs are listed for check(ex: a/b/c/df.csv): ./files/urls.csv
   Please write the PROD site Domain Link: https://prod-site.com
   Please write the Staging site Domain Link: https://stage-site.com
  ```

### Reports:

- Screenshots and comparison results will be stored in the Report/ folder under appropriate subdirectories.
- HTML reports with highlighted discrepancies will be generated to visualize the differences between Staging and Production metadata.

### SEO Comparison Flow

The script compares the following SEO metadata for each URL:

- Meta title
- Meta description
- Canonical link
- OpenGraph tags (e.g., og:title, og:description, etc.)
- Twitter tags (e.g., twitter:title, twitter:description, etc.)

## Styling Reports

Reports are styled using the `DataFrameStyler` class, which highlights differences between staging and production environments. The following custom styles are applied:

- **Red:** Non-matching data
- **Green:** Matching data
- **Orange:** Both staging and production have missing data

## Running the Tests

- **Command-line execution:** You can run the script from the command line as described in the [Usage](#usage) section.

- **Continuous Integration:** You can integrate this script into your CI/CD pipeline by automating its execution via tools like Jenkins, GitHub Actions, or GitLab CI.

## Contributing

If you would like to contribute to this project:

1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with a detailed description of the changes.


