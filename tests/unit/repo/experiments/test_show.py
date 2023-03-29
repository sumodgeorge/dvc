from funcy import first

from dvc.repo.experiments.show import get_branch_names, update_names


def test_get_show_branch(tmp_dir, scm, dvc, exp_stage):
    new_branch = "new"

    baseline = scm.get_rev()
    base_branch = scm.active_branch()
    results = dvc.experiments.run(exp_stage.addressing, params=["foo=2"])
    exp_a = first(results)
    dvc.experiments.branch(exp_a, new_branch)

    scm.checkout(new_branch, force=True)

    result = {
        "workspace": {"baseline": {"data": {}}},
        exp_a: {"baseline": {"data": {}}},
        baseline: {"baseline": {"data": {}}, exp_a: {"data": {}}},
    }

    branch_names = get_branch_names(scm, ["workspace", exp_a, baseline])
    assert branch_names == {exp_a: new_branch, baseline: base_branch}

    update_names(dvc, branch_names, result)
    assert result[exp_a]["baseline"]["data"] == {"name": new_branch}
    assert result[baseline]["baseline"]["data"] == {"name": base_branch}
    assert result[baseline][exp_a]["data"] == {"name": new_branch}
