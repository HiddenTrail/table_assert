*** Settings ***
Library                   SeleniumLibrary
Library                   libs${/}TableAssertionSeleniumLibrary.py

Suite Teardown            Close Browser

*** Variables ***
${URL}                    https://en.wikipedia.org/wiki/2000%E2%80%9301_Football_Conference
${TABLE_LOCATOR}          //h2[./span[text()="Final\ \ league table"]]//following-sibling::table[1]
${TABLE_HEADERS}          /tbody/tr/th[@scope="col"]
${TABLE_ROWS}             //tr
${TABLE_CELLS}            //*[self::td or self::th/a]
${EXPECTED_TABLE}         expected${/}english_2000-2001_conference.json


*** Test Cases ***
Assert 2000-2001 English Football Conference Results
    Open Browser                     ${URL}
    Wait Until Element Is Enabled    ${TABLE_LOCATOR}    10s
    Verify Table                     ${EXPECTED_TABLE}    ${TABLE_LOCATOR}    header_appendix=${TABLE_HEADERS}    cell_appendix=${TABLE_CELLS}
