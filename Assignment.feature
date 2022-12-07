Feature: Validate the Subscription Packages – Type & Price and Currency for all Countries (SA/Kuwait/Baharin)

  Scenario: Validate Packages for All Countries
    Given Launch The Google Chrome Browser
    When Open The Subscribe STCTV Site
    Then Verify Countries Names From Span
    Then Click on KSA Country
    Then Subscription Packages Validations For KSA Country
    Then Click on BAHRAIN Country
    Then Subscription Packages Validations For BAHRAIN Country
    Then Click on KUWAIT Country
    And Subscription Packages Validations For KUWAIT Country

