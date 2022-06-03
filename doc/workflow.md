# Recommended workflow

Types of content to push to this repo

* Example scripts (e.g., .py files)
* Notebooks (.ipynb files) - **be sure to always clear the output cells prior to committing notebook files to avoid large files, unnecessary conflicts or frequent updates**
* Documentation (preferably .md files)

Do NOT submit
* Large files
* Images
* Datasets

## One fork per participant

It is recommended that each participant creates their own fork of the main repo. From the [github page of the main repo](https://github.com/catalystneuro/spike-sorting-hackathon), click the "Fork" button at the top. Then clone your forked version to your local machine.

## Create branches on your forked repo

Since you will likely be working on multiple projects (or multiple features within a project) we recommend that you use branches on your forked repo. To create a new branch

```bash
cd spike-sorting-hackathon # your forked version
git checkout -b <branch-name>
```

To create another new branch, switch back to main and then create the second new branch

```bash
git checkout main
git checkout -b <another-branch>
```

It may be helpful to keep a separate working copy for each project or branch you are working on, so you don't need to keep stashing your changes when you switch between tasks.

```bash
spike-sorting-hackathon-proj-dockerize-sorters/ # on branch proj-dockerize-sorters
spike-sorting-hackathon-proj-clustering-in-si/ # on branch proj-clustering-in-si
```

## Collaborating on a project

When collaborating on a project, it is recommended that one developer creates a branch on their forked repo, and then gives the other developers write access to that repo. In this way, all developers can push content to the same branch of the forked repo. Periodically that content can be merged via PR back to the main repo as described below.

## Periodically fetching changes from the main repo

As PRs are merged into the [main repo](https://github.com/catalystneuro/), you will want to keep your fork up-to-date, especially when you are preparing to submit a pull request. Here's one way to do that (I welcome suggestions for a better method):

* Go to your forked repo on github (in browser)
* Click the "Fetch Upstream" button and then "Fetch and Merge" - this will merge the main branch of the central repo into your fork
* On your local system, pull the changes into your main branch, and then merge those changes into the branch you are working on.
* Push the merged changes on your branch to the forked repo. Your collaborators can then pull.

## Periodically submit pull requests

Periodically merge your work back into the [main repo](https://github.com/catalystneuro/spike-sorting-hackathon) via pull requests.
