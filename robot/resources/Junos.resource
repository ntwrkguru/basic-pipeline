*** Settings ***
Documentation   Resource file for Juniper devices
Variables       ../variables/vars.yaml
Library         ../libraries/Junos.py
Library         String
Library         Collections

*** Variables ***
${os_version}=    15.1X53-D67.6

*** Keywords ***
Log Facts
    FOR  ${device}   IN   @{devices}
        Connect Device    host=${device}
        &{facts}=         Gather Device Info
        Loop Over Facts   &{facts}
        Close Device
    END

Loop Over Facts
    [Arguments]   &{facts}
    FOR  ${key}  IN  @{facts.keys()}
        Log     ${facts["${key}"]}
    END

Validate Facts
    FOR  ${device}   IN       @{devices}
        Connect Device        host=${device}
        ${hostname}=          Get Hostname
        ${spine_device}=      Run Keyword And Return Status    Should Contain    ${hostname}    spine
        Close Device
    END
