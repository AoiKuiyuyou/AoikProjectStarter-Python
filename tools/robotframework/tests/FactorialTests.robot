*** Settings ***
Documentation     Test function `factorial`.
...
...               Test function `factorial` against various arguments.

Library           FactorialTestsLibrary.py

*** Test Cases ***
Call `factorial(0 <= n <=1)`
    Factorial of `0` is `1`
    Factorial of `1` is `1`

Call `factorial(n > 1)`
    Factorial of `2` is `2`
    Factorial of `3` is `6`

*** Keywords ***
Result is `${expect}`
    ${result}    result
    Should Be Equal    ${result}    ${expect}

Factorial of `${value}` is `${expect}`
    ${value}    Evaluate    ${value}
    ${expect}    Evaluate    ${expect}
    factorial    ${value}
    Result is `${expect}`
