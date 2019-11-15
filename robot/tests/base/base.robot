*** Settings ***
Documentation   Validating Juniper device facts
Resource        ../../resources/Junos.resource

*** Test Cases ***
Log Device Facts
    Log Facts

Verify Facts
    Validate Facts
