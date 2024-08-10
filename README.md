# Google Search to Wikipedia Verification

## Overview

This project uses Robot Framework to automate the process of searching for "nokia wikipedia" on Google, navigating to the Wikipedia page for Nokia, and verifying details about Nokia's founding year. The script utilizes Firefox for web browsing and includes error handling, screenshot capture, and verification steps.

## Files

1. `search_wikipedia.robot` – Contains the Robot Framework script to perform the search and verification tasks.
2. `Variables.py` – Contains variables used in the Robot Framework script for easy configuration and maintenance.

## Robot Framework Script

### Description

The Robot Framework script performs the following actions:

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

## Usage

1. **Run the Robot Framework test suite**:

   ```bash
   robot search_wikipedia.robot
   ```

2. **Review the results**:
   - The test results will be saved in `output.xml`.
   - Screenshots will be saved with the filename specified in the script.

## Running Tests

1. **Ensure required packages are installed**:

   ```bash
   pip install robotframework selenium webdriver-manager
   ```

2. **Execute the Robot Framework script**:

   ```bash
   robot search_wikipedia.robot
   ```

3. **Check the results**:
   - The results and logs are available in `output.xml`.
   - Screenshots will be saved as defined in the script.

## Script Details

The `search_wikipedia.robot` script includes the following sections:

- **Settings**: Imports necessary libraries and defines variables.
- **Test Cases**: Describes the steps for the test scenario including searching, clicking, and verifying.
- **Keywords**: Defines reusable steps for opening the browser, performing the search, clicking the link, verifying page content, and capturing screenshots.
