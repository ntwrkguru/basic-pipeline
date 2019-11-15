# basic-pipeline

## Purpose

This repository holds the inventory, variables, and playbooks/roles to configure Junos devices. The purpose is a super simple playbook and robot test that will demonstrate a POC of those 2 things flowing through Jenkins.

## Jenkins

### Plugins

To retrieve a list of installed plugins, run this script in script console:

```
Jenkins.instance.pluginManager.plugins.each{
  plugin -> 
    println ("${plugin.getDisplayName()} (${plugin.getShortName()}): ${plugin.getVersion()}")
}
```

```text
Pipeline Graph Analysis Plugin (pipeline-graph-analysis): 1.9
Folders Plugin (cloudbees-folder): 6.8
Docker Commons Plugin (docker-commons): 1.14
JDK Tool Plugin (jdk-tool): 1.2
Script Security Plugin (script-security): 1.58
Pipeline: REST API Plugin (pipeline-rest-api): 2.11
Command Agent Launcher Plugin (command-launcher): 1.3
Docker Pipeline (docker-workflow): 1.18
Structs Plugin (structs): 1.17
JSch dependency plugin (jsch): 0.1.55
Pipeline: Step API (workflow-step-api): 2.19
SCM API Plugin (scm-api): 2.4.1
Pipeline: API (workflow-api): 2.33
bouncycastle API Plugin (bouncycastle-api): 2.17
JUnit Plugin (junit): 1.27
Pipeline: Job (workflow-job): 2.32
OWASP Markup Formatter Plugin (antisamy-markup-formatter): 1.5
Token Macro Plugin (token-macro): 2.7
Git client plugin (git-client): 2.7.7
Build Timeout (build-timeout): 1.19
Credentials Plugin (credentials): 2.1.18
SSH Credentials Plugin (ssh-credentials): 1.16
GIT server Plugin (git-server): 1.7
Plain Credentials Plugin (plain-credentials): 1.5
Pipeline: Shared Groovy Libraries (workflow-cps-global-lib): 2.13
Credentials Binding Plugin (credentials-binding): 1.18
Timestamper (timestamper): 1.9
Pipeline: Supporting APIs (workflow-support): 3.2
Durable Task Plugin (durable-task): 1.29
Pipeline: Nodes and Processes (workflow-durable-task-step): 2.30
Matrix Project Plugin (matrix-project): 1.14
Display URL API (display-url-api): 2.3.1
Resource Disposer Plugin (resource-disposer): 0.12
Workspace Cleanup Plugin (ws-cleanup): 0.37
Git plugin (git): 3.9.3
Pipeline: Milestone Step (pipeline-milestone-step): 1.3.1
JavaScript GUI Lib: jQuery bundles (jQuery and jQuery UI) plugin (jquery-detached): 1.2.1
Jackson 2 API Plugin (jackson2-api): 2.9.8
JavaScript GUI Lib: ACE Editor bundle plugin (ace-editor): 1.1
Mailer Plugin (mailer): 1.23
Pipeline: SCM Step (workflow-scm-step): 2.7
Pipeline: Groovy (workflow-cps): 2.67
Pipeline: Input Step (pipeline-input-step): 2.10
Branch API Plugin (branch-api): 2.4.0
Pipeline: Stage Step (pipeline-stage-step): 2.3
JavaScript GUI Lib: Handlebars bundle plugin (handlebars): 1.1.1
JavaScript GUI Lib: Moment.js bundle plugin (momentjs): 1.1.1
Pipeline: Build Step (pipeline-build-step): 2.9
Pipeline: Multibranch (workflow-multibranch): 2.21
Pipeline: Model API (pipeline-model-api): 1.3.8
Pipeline: Declarative Extension Points API (pipeline-model-extensions): 1.3.8
Authentication Tokens API Plugin (authentication-tokens): 1.3
Apache HttpComponents Client 4.x API Plugin (apache-httpcomponents-client-4-api): 4.5.5-3.0
Pipeline: Basic Steps (workflow-basic-steps): 2.15
Pipeline: Stage Tags Metadata (pipeline-stage-tags-metadata): 1.3.8
Pipeline: Declarative Agent API (pipeline-model-declarative-agent): 1.1.1
Pipeline: Declarative (pipeline-model-definition): 1.3.8
Lockable Resources plugin (lockable-resources): 2.5
JIRA plugin (jira): 3.0.6
Server Sent Events (SSE) Gateway Plugin (sse-gateway): 1.17
AnsiColor (ansicolor): 0.6.2
Pipeline: Stage View Plugin (pipeline-stage-view): 2.11
MapDB API Plugin (mapdb-api): 1.0.9.0
SSH Slaves plugin (ssh-slaves): 1.29.4
Matrix Authorization Strategy Plugin (matrix-auth): 2.3
PAM Authentication plugin (pam-auth): 1.5
LDAP Plugin (ldap): 1.20
Robot Framework plugin (robot): 1.6.5
Email Extension Plugin (email-ext): 2.66
Pipeline (workflow-aggregator): 2.6
Ansible plugin (ansible): 1.0
Config File Provider Plugin (config-file-provider): 3.6
Pipeline: Multibranch with defaults (pipeline-multibranch-defaults): 2.0
WMI Windows Agents Plugin (windows-slaves): 1.4
External Monitor Job Type Plugin (external-monitor-job): 1.7
Green Balls (greenballs): 1.15
Design Language (jenkins-design-language): 1.14.0
Pub-Sub "light" Bus (pubsub-light): 1.12
HTML Publisher plugin (htmlpublisher): 1.18
GitLab Plugin (gitlab-plugin): 1.5.12
Variant Plugin (variant): 1.2
Favorite (favorite): 2.3.2
Handy Uri Templates 2.x API Plugin (handy-uri-templates-2-api): 2.1.7-1.0
Gitlab Merge Request Builder (gitlab-merge-request-jenkins): 2.0.0
```

### Modifications

To view all of the Robot output (logs/reports), it's necessary to adjust the security settings. This is done in the init script for Jenkins by adding the following variable:

```ROBOT_WORKROUND="sandbox allow-scripts; default-src 'none'; img-src 'self' data: ; style-src 'self' 'unsafe-inline' data: ; script-src 'self' 'unsafe-inline' 'unsafe-eval' ;"```

Then modifying the start command by adding the following:

``` -Dhudson.model.DirectoryBrowserSupport.CSP=$ROBOT_WORKAROUND```

On Ubuntu, this looks like:

```bash
  # Workaround to display Robot reports in Jenkins builds
  ROBOT_WORKROUND="sandbox allow-scripts; default-src 'none'; img-src 'self' data: ; style-src 'self' 'unsafe-inline' data: ; script-src 'self' 'unsafe-inline' 'unsafe-eval' ;"

  # --user in daemon doesn't prepare environment variables like HOME, USER, LOGNAME or USERNAME,
  # so we let su do so for us now
  $SU -l $JENKINS_USER --shell=/bin/bash -c "$DAEMON $DAEMON_ARGS -- $JAVA $JAVA_ARGS -Dhudson.model.DirectoryBrowserSupport.CSP=$ROBOT_WORKAROUND -jar $JENKINS_WAR $JENKINS_ARGS" || return 2
  ```
