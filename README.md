# GitHub Action to Publish Allure report to Morph object storage
This action allows you to publish [Allure reports](https://github.com/allure-framework/allure2)
to [Morph object storage](https://morphbits.io/).

The Allure report will be available in a web browser at a static link like this:
http://example.com:9100/api/v0.7/buckets/tstbucket/objects/my-report.html/download


## Supported platforms
This action supports the following platforms:
- Linux x86-64

This action was tested on the following runners:
- [Ubuntu 22.04 GitHub-hosted runners](https://github.com/actions/runner-images/blob/main/images/ubuntu/Ubuntu2204-Readme.md)

# Configuration

## GitHub secrets
The following sensitive information must be passed as
[GitHub Actions secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions).
It is very important to use SECRETS and NOT variables, otherwise your username and password will be available to
the whole internet.

| Key                   | Value                                     | Required | Default |
|-----------------------|-------------------------------------------|----------|---------|
| `MORPH_USER_NAME`     | Username for Morph object storage account | **Yes**  | N/A     |
| `MORPH_USER_PASSWORD` | Password for Morph object storage account | **Yes**  | N/A     |

Please keep sensitive data safe.

## GitHub environment variables

### Morph storage network environment variables
The following variables must be passed as
[GitHub Actions vars context](https://docs.github.com/en/actions/learn-github-actions/variables#using-the-vars-context-to-access-configuration-variable-values) 
or [GitHub Actions environment variables](https://docs.github.com/en/actions/learn-github-actions/variables).

Up-to-date information about Morph storage network can be seen on [Morph object storage documentation](https://morphbits.io/).

| Key                         | Value                                   | Required | Default |
|-----------------------------|-----------------------------------------|----------|---------|
| `MORPH_URL`                 | Morph object storage address            | **Yes**  | N/A     |
| `MORPH_PORT`                | Morph object storage port               | **No**   | 9100    |
| `ALLURE_REPORT_BUCKET_NAME` | Bucket name for your Allure report data | **Yes**  | N/A     |

### Workflow environment variables
The following variables must be passed as
[GitHub Actions vars context](https://docs.github.com/en/actions/learn-github-actions/variables#using-the-vars-context-to-access-configuration-variable-values)
or [GitHub Actions environment variables](https://docs.github.com/en/actions/learn-github-actions/variables).

| Key                    | Value                                                                                                                                                                                                                                     | Required | Default                                           |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|---------------------------------------------------|
| `ALLURE_RESULTS_DIR`   | Path to the directory where the Allure test report is stored                                                                                                                                                                              | **Yes**  | N/A                                               |
| `ALLURE_GENERATED_DIR` | Path to the directory that will be used to store the generated report. This directory will be created automatically if it does not exist. ATTENTION - all files that were in this directory before the action was started will be deleted | **No**   | ${GITHUB_WORKSPACE}/morph-allure-generated-report |

## Output

| Key                 | Value                                                                                              |
|---------------------|----------------------------------------------------------------------------------------------------|
| `ALLURE_REPORT_URL` | Output example: http://example.com:9100/api/v0.7/buckets/tstbucket/objects/my-report.html/download |

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
    branches: [ master ]
env:
  ALLURE_RESULTS_DIR: ${GITHUB_WORKSPACE}/allure-results
jobs:
  push-to-morph:
    runs-on: ubuntu-latest
    steps:
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
  
      - uses: actions/checkout@v4
      - name: Publish Allure report to Morph object storage
        id: publish_to_morph_object_storage
        uses: morphbits-io/gh-push-to-morph@master
        with:
          MORPH_USER_NAME: ${{ secrets.MORPH_USER_NAME }}
          MORPH_USER_PASSWORD: ${{ secrets.MORPH_USER_PASSWORD }}
          MORPH_URL: ${{ vars.MORPH_URL }}
          ALLURE_REPORT_BUCKET_NAME: ${{ vars.ALLURE_REPORT_BUCKET_NAME }}
          ALLURE_GENERATED_DIR: ${{ vars.ALLURE_GENERATED_DIR }}
          ALLURE_RESULTS_DIR: ${{ env.ALLURE_RESULTS_DIR }}

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
