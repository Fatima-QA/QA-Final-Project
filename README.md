# QA Final Project

Manual and automated testing project prepared by Fatima Tahirova for ABB Tech Academy.

## Scope

- Bakcell: tariff details, languages, internet packages, roaming and form validation.
- Bakcell Shop: product search, filters, product details and shopping cart workflows.
- Banking API sandbox: authentication, beneficiaries, virtual cards and utility payments.

## Technologies

Java, Maven, Gauge, Selenium WebDriver, RestAssured and JSON Schema Validator.

Gauge executes the scenarios written in `.spec` files. Java step implementations connect those scenarios to reusable helpers.

## Run the UI tests

Run these commands from the project root in PowerShell:

```powershell
mvn.cmd test "-Dgauge.specs.dir=specs/ui-testing/finalProjectBakcell.spec"
mvn.cmd test "-Dgauge.specs.dir=specs/ui-testing/finalProjectBakcellShop.spec"
mvn.cmd test "-Dgauge.specs.dir=specs/api-testing/finalProjectBeneficiaries.spec"
```

