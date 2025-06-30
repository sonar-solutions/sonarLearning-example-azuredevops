## Overview

This project uses a GitLab CI/CD pipeline defined in the `.gitlab-ci.yml` file. Below is an explanation of the tasks included in the pipeline


**PLEASE READ OUR SONARQUBE DOCUMENTATION FOR WORKING WITH GITLAB ACTION PIPELINES**  
[GitLab - SonarQube Server Integration](https://docs.sonarsource.com/sonarqube-server/latest/devops-platform-integration/gitlab-integration/introduction/)  
[GitLab CI - SonarQube Cloud](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/gitlab-ci/)

## Important Information in Examples
- The pipeline is configured to run only under the following conditions:  
  - When the branch is `main`.  
  - When the pipeline is triggered by a merge request event.  
- They have shallow fetch set to 0. this is required for SonarScanner to properly analyze your project.  
- The pipeline includes a task for SonarQube-Server(`sonarqube-server-check`) and SonarQube-Cloud examples(`sonarqube-cloud-check`).
- For both `sonar.projectKey` and `sonarprojectName`, we are using the following `${CI_PROJECT_NAMESPACE}_gitlab_${CI_PROJECT_NAME}` as naming convention. This results in `OrgName-gitlab_RepoName`.
- Please make sure you have set up your the following variables. Some of these can be hardcoded, please choose how you would like to set these up in your pipeline. 
    - SONAR_TOKEN  > SonarQube Server  
    - SONAR_HOST_URL > SonarQube Server
    - SQ_CLOUD_TOKEN > SonarQube Cloud  
    - SQ_CLOUD_ORGANIZATION > SonarQube Cloud  
    - SQ_CLOUD_URL > SonarQube Cloud  

## Important Links
[SonarQube Server - GitLab Integration](https://docs.sonarsource.com/sonarqube-server/latest/devops-platform-integration/gitlab-integration/introduction/)  
[SonarQube Cloud - GitLab Integration](https://docs.sonarsource.com/sonarqube-cloud/getting-started/gitlab/)  

[SonarScanner Analysis Scope](https://docs.sonarsource.com/sonarqube-server/latest/project-administration/analysis-scope/)  
[SonarScanner Analysis Parameters](https://docs.sonarsource.com/sonarqube-server/latest/analyzing-source-code/analysis-parameters/)  

[Python SonarScanner Analysis Extra Information](https://docs.sonarsource.com/sonarqube-server/latest/analyzing-source-code/languages/python/)  
[Python Test Coverage](https://docs.sonarsource.com/sonarqube-server/latest/analyzing-source-code/test-coverage/python-test-coverage/)  

## Example to fail the entire pipeline if Quality Gate fails
In certain situations, you may want to halt/fail the pipeline if the SonarQube Quality Gate fails, preventing subsequent steps from executing.  
This can be achieved by adding `sonar.qualitygate.wait=true` to the `with: args: >` section in the **SonarQube Analysis** task.  

Example:
``` sh
    with:
        args: >
          -Dsonar.verbose=true
          -Dsonar.qualitygate.wait=true
```

## PR Decoration Test  (still working on these instructions)
In SonarQube (Server and Cloud), there is functionality to be able to block PR from being merged to SonarQube  
In GitLab CICD, you need to have the following set up in your Project:  
- Under Settings > Merge Requests > In the Merge Checks section, select Pipelines must succeed.

SonarQube Documentation:
[Prevent Pull Request Merge](https://docs.sonarsource.com/sonarqube-server/latest/devops-platform-integration/gitlab-integration/setting-up-at-project-level/)  

In SonarQube Server, you need to make sure the DevOps Integration is correctly configured. Go to the Project, in Project Settings > General Settings > DevOps Platform Integration.
In SonarQube Cloud, you need to make sure the DevOps Integration is correctly configured. Go to the Project, in Administration > General Settings > Repository Binding. 

To test this, follow these steps:
1. Create New Branch
2. In new branch, go to file src/s1940.py
3. Add the following code snippet
``` sh
def fun(a):
  i = 10
  return i + a       # Noncompliant
  i += 1             # this is never executed
```
4. Create PR to merge to the target branch you have set the Branch Protection Rule
5. Wait for the SonarQube Scanner analysis to complete
6. It should Fail and have the PR get blocked from merging

__**For more examples please check:**__
[Onboarding Examples](https://github.com/sonar-solutions/Onboarding-Examples-List)
