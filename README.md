# GitHub Action to Publish Allure report to Morph object storage
This GitHub Action facilitates the publishing of [Allure reports](https://github.com/allure-framework/allure2)
to [Morph object storage](https://morphbits.io/), a robust and scalable solution for handling test reports.
Designed to streamline the integration and management of test data, this action is a vital tool for teams engaged in TestOps.

For a comprehensive understanding of how Allure TestOps and Morph's cloud-based object storage work in tandem to enhance
your testing workflow, please refer to our [overview](https://morphbits.io/showcases#allure). This document explains
the significance of Allure Reports in Quality Assurance and DevOps, the capabilities of Morph's object storage in
managing test data, and the seamless
integration of these technologies through GitHub Actions.

The published Allure report will be accessible through a static HTTP link, allowing for easy sharing and review in a web browser:
http://example.com:443/api/v0.8/buckets/tstbucket/objects/my-report.html/download


## Supported platforms
This action supports the following platforms:
- Linux x86-64

This action was tested on the following runners:
- [Ubuntu 22.04 GitHub-hosted runners](https://github.com/actions/runner-images/blob/main/images/ubuntu/Ubuntu2204-Readme.md)

# Configuration

## GitHub secrets
_The following sensitive information must be passed as
[GitHub Actions secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions) to protect your data._

**It is very important to use SECRETS and NOT variables, otherwise your username and password will be exposed to the Internet.**

| Key                   | Value                                     | Required | Default |
|-----------------------|-------------------------------------------|----------|---------|
| `MORPH_USER_NAME`     | Username for Morph object storage account | **Yes**  | N/A     |
| `MORPH_USER_PASSWORD` | Password for Morph object storage account | **Yes**  | N/A     |

Please keep sensitive data safe.

## GitHub environment variables

### Morph storage network environment variables
_The following variables are expected to be passed via
[GitHub Actions vars context](https://docs.github.com/en/actions/learn-github-actions/variables#using-the-vars-context-to-access-configuration-variable-values) 
or [GitHub Actions environment variables](https://docs.github.com/en/actions/learn-github-actions/variables)._

Up-to-date information about Morph storage network can be found on [Morph object storage documentation](https://morphbits.io/).

| Key                         | Value                                   | Required | Default                    |
|-----------------------------|-----------------------------------------|----------|----------------------------|
| `MORPH_URL`                 | Morph object storage address            | **No**   | https://morph.morphbits.io |
| `MORPH_PORT`                | Morph object storage port               | **No**   | 443                       |
| `ALLURE_REPORT_BUCKET_NAME` | Bucket name for your Allure report data | **Yes**  | N/A                        |

### Workflow environment variables
_The following variables are expected to be passed via
[GitHub Actions vars context](https://docs.github.com/en/actions/learn-github-actions/variables#using-the-vars-context-to-access-configuration-variable-values)
or [GitHub Actions environment variables](https://docs.github.com/en/actions/learn-github-actions/variables)._

| Key                    | Value                                                                                                                                                                                                                                     | Required | Default                                           |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|---------------------------------------------------|
| `ALLURE_RESULTS_DIR`   | Path to the directory where the Allure test report is stored                                                                                                                                                                              | **Yes**  | N/A                                               |
| `ALLURE_GENERATED_DIR` | Path to the directory that will be used to store the generated report. This directory will be created automatically if it does not exist. ATTENTION - all files that were in this directory before the action was started will be deleted | **No**   | ${GITHUB_WORKSPACE}/morph-allure-generated-report |

### Expiration period environment variables
_The following variables are expected to be passed via
[GitHub Actions vars context](https://docs.github.com/en/actions/learn-github-actions/variables#using-the-vars-context-to-access-configuration-variable-values)
or [GitHub Actions environment variables](https://docs.github.com/en/actions/learn-github-actions/variables)._

These environment variables are responsible for the storage time of the Allure report in the storage network in HOURS.

After the period is over, the Allure report will be deleted. They are convenient to use for test reports rotation.

They default is 0, in which case the Allure reports will be stored until they are manually deleted.
We recommend setting a reasonable and convenient expiration period, for example, a month (744 hours).


| Key        | Value                                                                                                       | Required | Default |
|------------|-------------------------------------------------------------------------------------------------------------|----------|---------|
| `LIFETIME` | Allure report lifetime, in hours. Zero means no expiration. Number of HOURS for Allure report to stay valid | **No**   | 0       |

## Output

| Key                 | Value                                                                                              |
|---------------------|----------------------------------------------------------------------------------------------------|
| `ALLURE_REPORT_URL` | Output example: http://example.com:443/api/v0.8/buckets/tstbucket/objects/my-report.html/download |

# Dependencies

## Python
The GitHub runner must have Python 3 installed on it.

You can install Python like this:
```yml
- name: Set up Python
  uses: actions/setup-python@v4
  with:
    python-version: '3.11.6'
```

# Examples

```yml
name: Publish Allure report to Morph object storage
on:
  push:
    branches: [ main ]

env:
  ALLURE_RESULTS_DIR: ${{ github.workspace }}/allure-results
jobs:
  push-to-morph:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11.6'
          
      - name: Checkout testcases repository
        uses: actions/checkout@v4
        with:
          repository: your_repo
          ref: 'master'
          path: testcases
          
      - name: Run tests and store allure result
        run: |
          source venv/bin/activate && pytest --alluredir=${{ env.ALLURE_RESULTS_DIR }} pytest_tests/testsuites
        working-directory: testcases
  
      - name: Publish Allure report to Morph object storage
        id: publish_to_morph_object_storage
        uses: morphbits-io/gh-push-to-morph@main
        with:
          MORPH_USER_NAME: ${{ secrets.MORPH_USER_NAME }}
          MORPH_USER_PASSWORD: ${{ secrets.MORPH_USER_PASSWORD }}
          MORPH_URL: ${{ vars.MORPH_URL }}
          ALLURE_REPORT_BUCKET_NAME: ${{ vars.ALLURE_REPORT_BUCKET_NAME }}
          ALLURE_GENERATED_DIR: ${{ vars.ALLURE_GENERATED_DIR }}
          ALLURE_RESULTS_DIR: ${{ env.ALLURE_RESULTS_DIR }}
          LIFETIME: ${{ vars.LIFETIME }}

      - name: Post a link to the Allure report stored in the Morph object repository
        id: post_report_link
        timeout-minutes: 60
        if: always() && steps.publish_to_morph_object_storage.outcome == 'success'
        env:
          ALLURE_REPORT_URL: ${{ steps.publish_to_morph_object_storage.outputs.ALLURE_REPORT_URL }}
        uses: Sibz/github-status-action@v1
        with:
          authToken: ${{secrets.GITHUB_TOKEN}}
          context: 'A link to the Allure report stored in the Morph object repository'
          state: 'success'
          sha: ${{github.event.pull_request.head.sha || github.sha}}
          target_url: ${{ env.ALLURE_REPORT_URL }}
```
# Local debugging

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
MORPH_USER_PASSWORD=testuser python push-to-morph.py --url http://localhost --username testuser --bucket tstbucket --report /path_to_report/my-report.html
```
