# Created by bbkam at 11/6/2024
Feature: Test for left Nav menu feature
  # Enter feature description here


#  @smoke
#  Scenario: user can navigate to Connect the Company page
#    Given Open reelly main page
#    When Input user name
#    When Input user password
#    When Click continue button
#    When Get current window handle
#    When Click Connect the Company icon
#    When Switch to new tab
#    Then Verify Connect the Company page is open in new tab


  @mobile
  Scenario: Mobile user can navigate to Connect the Company page
    Given Open reelly main page
    When Input user name
    When Input user password
    When Click continue button
    When Click on main menu
    When Click on user profile icon
    When Scroll to bottom
    When Click on subcription and payment
    Then Verify Connect the Company page is open