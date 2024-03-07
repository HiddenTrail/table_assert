# table_assert
This repository contains [Robot Framework](https://robotframework.org/) table assertation tools for both [Selenium Library](https://github.com/robotframework/SeleniumLibrary)
and [Browser Library](https://robotframework-browser.org/).

## libraries
There are two similar libraries in `libs` directory:

- [TableAssertionBrowserLibrary.py](https://github.com/HiddenTrail/table_assert/blob/main/libs/TableAssertionBrowserLibrary.py) to be used with Browser Library
- [TableAssertionSeleniumLibrary.py](https://github.com/HiddenTrail/table_assert/blob/main/libs/TableAssertionSeleniumLibrary.py) to be used with Selenium Library

## keywords
Both libraries contain the same keywords

`Verify Table  <filepath>  <locator>  [header_appendix=//th]  [row_appendix=//tr]  [cell_appendix=//td]` 

Does the actual verification of table.

`Verify Table Init  <filepath>  <locator>  [header_appendix=//th]  [row_appendix=//tr]  [cell_appendix=//td]`

Is used to initialize the verification data. Data is written to file that is appended with a `_template` postfix.
This file can be used as a basis for verification file. In many cases file can be used as is.

Parameters for keywords:

- `filepath`  points to the expected result file
- `locator`  is the locator of the table to be verified
-  `header_appendix`  (optional) defaults to `//th`
-  `row_appendix`  (optional) defaults to `//tr`
-  `cell_appendix`  (optional) defaults to `//td`

`locator` and appendices and used to build the locator pointing to table's headers and data cells on data rows

For example:
When the `locator` is `//table` and default values are used for appendices:

- for headers `//table//th`
- for rows `//table//th//tr`
- for cells `//table//th//tr[`*index*`]//td]`, where *index* is 2..n depending on number of rows (Note: row 1 contains headers!)

## example run

`rf.sh table_assert_browser.robot` to run example for Browser Library

`rf.sh table_assert_selenium.robot` to run example for Selenium Library

## installation
To run some installations are needed:
+ [Python](https://www.python.org/)
+ [Pip](https://pip.pypa.io/en/stable/)
+ [Node.js](https://nodejs.org/en)
+ [Robot Framework](https://robotframework.org/)
+ [Selenium Library](https://github.com/robotframework/SeleniumLibrary) and WebDriver for [Chrome](https://chromedriver.chromium.org/downloads) or [Firefox](https://github.com/mozilla/geckodriver/releases)
+ [BrowserLibrary](https://github.com/MarketSquare/robotframework-browser)

To install these (in addition to Python, Pip & Node.js) run:
```
pip install robotframework
pip install robotframework-seleniumlibrary
pip install robotframework-browser
rfbrowser init
```

## road map

- synchronization of keywords
- using [jsondiff](https://github.com/xlwings/jsondiff) to analyze differences
- adding mechanism to skip verification of certains values (i.e. timestamps and generated IDs)
- sorting lists when verifying results from undeterministic source

## a little exercise

Go to [this page](https://www.pdc.tv/order-of-merit/pdc-order-merit) and check how easily you can create a test case for verifying the PDC Order of Merit table.

Use `Developer -> Inspect elements` to check the following things:

- what is the locator for the table
- what appendix is needed for table headers and does the full locator produce correct count of them?
- what appendix is needed for table rows and does the full locator produce correct count of them?
- what appendix is needed for table cells and does the full locator produce correct count of them?

Remember to use keyword `Verify Table Init` when running the test for the first time to initialize the expected result file.
