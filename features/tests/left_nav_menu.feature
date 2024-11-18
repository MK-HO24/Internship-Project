# Created by bbkam at 11/6/2024
Feature: Test for left Nav menu feature
  # Enter feature description here


  @smoke
  Scenario: user can navigate to Connect the Company page
    Given Open reelly main page
    When Input user name
    When Input user password
    When Click continue button
    When Get current window handle
    When Click Connect the Company icon
    When Switch to new tab
    Then Verify Connect the Company page is open in new tab
