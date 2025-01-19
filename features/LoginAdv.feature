Feature: Login Functionality Advanced
  As a user,
  I want to be able to login into the tech canvass LMS
  So that I can view course content

  Background: Open Browser
     Given I am on the Login Page

  Scenario Outline: Login Success
    When I enter "<username>" and "<password>"
    And I click on login button
    Examples:
      | username | password |
      | test1    | test1    |
      | test2    | test2    |
      | test3    | test3    |