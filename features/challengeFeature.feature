@Test_wizeline
Feature: Wizeline_UI_challenge
    As a user
    I want to log in to the platform and see the products.
    Background:
        Given I am on the login page
    @Test01
    Scenario Outline: successfully logged in
        When I enter "<user>" in the user field
        And I enter "secret_sauce" in the password field
        And I press the Login button
        Then I should see the main page
        Examples:
        |   user    |
        |standard_user|
        |locked_out_user|
        |problem_user|
        |performance_glitch_user|
        |error_user|
        |visual_user|
    @Test02
    Scenario: failed to login
        When I enter "standard_user" in the user field
        And I enter "wrong_password" in the password field
        And I press the login button
        Then I should see an error message.