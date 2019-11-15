This repo has examples of some basic tests for the datacenter network. Each test case has its own directory that contains a robot file.

# Running Robot Tests

```sh
$ cd tests/underlay
$ robot underlay.robot
```

# Example

```sh
$ robot underlay.robot 
==============================================================================
Underlay :: Validating Juniper device OSPF relationships                      
==============================================================================
Log OSPF Info                                                         | PASS |
------------------------------------------------------------------------------
Verify OSPF Info                                                      | PASS |
------------------------------------------------------------------------------
Underlay :: Validating Juniper device OSPF relationships              | PASS |
2 critical tests, 2 passed, 0 failed
2 tests total, 2 passed, 0 failed
==============================================================================
Output:  ~/robot/underlay/output.xml
Log:     ~/robot/underlay/log.html
Report:  ~/robot/underlay/report.html
```

Test reports are generated under the same directory: _report.html_ and _log.html_

# Robot

[Robot Framework](https://robotframework.org)  
[User Guide](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html)
