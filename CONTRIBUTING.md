# How to contribute

Everyone is free to contribute on this project.

There are two ways to contribute:

- Submit an issue.
- Submit a pull request.

## Submitting an issue

Before creating an issue please make sure that it was not already reported.

### When?

- You encountered an issue.
- You have a change proposal.
- You have a feature request.

### How?

1) Go to the *Issues* tab and click on the *New issue* button.
2) Title should be a small sentence describing the request.
3) The comment should contains as much information as possible
    * Actual behavior (including the version you used)
    * Expected behavior
    * Steps to reproduce

## Submitting a pull request

### When?

- You fixed an issue.
- You changed something.
- You added a new feature.

### How?

#### Code

1) Create a new branch based on *development* branch.
2) Add your changes.
3) Follow [Black](https://black.readthedocs.io/en/stable/) code formatting.
    * To add the pre-commit hook, after the installation run: **pre-commit install**
4) Add at least one test case.
    * Unless it is an internal refactoring request or a documentation update.
5) Increment [version number](https://semver.org) and add related [changelog entry](https://keepachangelog.com/en/1.0.0/).
    * Unless it is a documentation update.

##### Changelog entry

Once the changelog entry is added, please don't forget to also add the link to the proper tag at the end of the changelog.

#### Enter pull request

1) Go to the *Pull requests* tab and click on the *New pull request* button.
2) *base* should always be set to development and it should be compared to your branch.
3) Title should be a small sentence describing the request.
3) The comment should contains as much information as possible
    * Actual behavior (before the new code)
    * Expected behavior (with the new code)
    * Steps to reproduce (with and without the new code to see the difference)