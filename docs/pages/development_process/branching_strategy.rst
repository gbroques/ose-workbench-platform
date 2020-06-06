Branching Strategy
==================
OSE Workbenches should follow the `Feature Branch Workflow <https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow>`_:

    The core idea behind the **Feature Branch Workflow** is that all feature development should take place in a dedicated branch instead of the ``master`` branch.
    This encapsulation makes it easy for multiple developers to work on a particular feature without disturbing the main codebase.
    It also means the ``master`` branch will never contain broken code, which is a huge advantage for continuous integration environments.

    Encapsulating feature development also makes it possible to leverage `pull requests <https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests>`_, which are a way to initiate discussions around a branch.
    They give other developers the opportunity to sign off on a feature before it gets integrated into the official project.
    Or, if you get stuck in the middle of a feature, you can open a pull request asking for suggestions from your colleagues.
    The point is, pull requests make it incredibly easy for your team to comment on each other’s work.

    -- `Atlassian, Git Feature Branch Workflow <https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow>`_
