from typing import List, Optional

from dvc.repo import Repo


def exp_save(
    name: Optional[str] = None,
    force: bool = False,
    include_untracked: Optional[List[str]] = None,
):
    """
    Create a new DVC experiment using `exp save`.

    See https://dvc.org/doc/command-reference/exp/save.

    Args:
        name (str, optional): specify a name for this experiment.
            If `None`, a default one will be generated, such as `urban-sign`.
            Defaults to `None`.
        force (bool):  overwrite the experiment if an experiment with the same
            name already exists.
            Defaults to `False`.
        include_untracked (List[str], optional): specify untracked file(s) to
            be included in the saved experiment.
            Defaults to `None`.

    Returns:
        str: The `Git revision`_ of the created experiment.

    Raises:
        ExperimentExistsError: If an experiment with `name` already exists and
            `force=False`.

    .. _Git revision:
        https://git-scm.com/docs/revisions
    """
    with Repo() as repo:
        return repo.experiments.save(
            name=name, force=force, include_untracked=include_untracked
        )
