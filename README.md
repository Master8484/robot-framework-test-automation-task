# Google Search to Wikipedia Verification

## Overview

This project uses Robot Framework to automate the process of searching for "nokia wikipedia" on Google, navigating to the Wikipedia page for Nokia, and verifying details about Nokia's founding year. The script utilizes Firefox for web browsing and includes error handling, screenshot capture, and verification steps.

Here’s the updated README text that corresponds to the combined `test_selenium.py` file:

## Files

- **`test_selenium.py`**: Contains the complete Selenium test script that performs the search and verification tasks, with all variables and logic included in a single file.

### Variables

- **`${BROWSER}`**: Browser type to use (set to `Firefox`).
- **`${URL}`**: URL of the Google search page.
- **`${SEARCH_TERM}`**: Search term to use in Google.
- **`${EXPECTED_YEAR}`**: Expected founding year of Nokia.
- **`${GOOGLE_SEARCH_INPUT}`**: XPath locator for Google search input field.
- **`${GOOGLE_SEARCH_BUTTON}`**: XPath locator for Google search button.
- **`${WIKIPEDIA_LINK}`**: XPath locator for Wikipedia link in search results.
- **`${FOUNDING_YEAR_XPATH}`**: XPath locator for Nokia's founding year on Wikipedia.
- **`${SCREENSHOT_FILENAME}`**: Filename for the screenshot of the Wikipedia page.

## Script Description

The script performs the following actions:

1. Opens [Google](https://www.google.com/) in Firefox.
2. Searches for "nokia wikipedia".
3. Verifies that a Wikipedia link appears in the search results.
4. Clicks on the first Wikipedia link if it exists.
5. Waits for the Wikipedia page to fully load.
6. Captures a screenshot of the entire Wikipedia page.
7. Verifies that the page title contains "Nokia".
8. Extracts Nokia's founding year from the page using XPath.
9. Verifies that the extracted founding year is 1865.
10. Includes error handling if the Wikipedia link is not found in search results.

## Script Structure

The `test_selenium.py` script includes the following sections:

- **Imports and Setup**: Imports necessary libraries and sets up browser options and web driver management.
- **Test Functions**: Defines the steps for the test scenario, including searching, clicking, verifying and capturing screenshots.
- **Assertions**: Includes checks to verify that the correct page is loaded and the founding year matches the expected value.

## How to Run

1. **Install Required Packages**:

   Ensure you have the required packages installed by running:

   ```bash
   pip install pytest selenium webdriver-manager
   ```

2. **Run the Test**:

   Execute the test script using Pytest:

   ```bash
   pytest test_selenium.py
   ```

3. **Review the Results**:

   - The test results will be displayed in the terminal.
   - A screenshot of the Wikipedia page will be saved as `Nokia_Wikipedia_Screenshot.png` in the same directory.
