Feature: Login Functionality
  As a user,
  I want to be able to login into the tech canvass LMS
  So that I can view course content

  Scenario: Login Success
    Given when a user opens Chrome Browser
    When user navigates to tech canvass url 'https://techedge.techcanvass.co/Login.aspx'
    And user enters username in the login text box
    And user enters password in password text box
    And clicks on the Login button
    Then validate that title is 'Dashbard' after I click on login button
    And validate heading of webpage to be 'My Courses' after I click login button

  Scenario: Login Failed
    Given when a user opens Chrome Browser
    When user navigates to tech canvass url 'https://techedge.techcanvass.co/Login.aspx'
    And user enters username in the login text box
    And user enters password in password text box
    And clicks on the Login button
    Then validate that popup saying 'Please check your login credentials.' is displayed