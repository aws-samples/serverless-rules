#!/usr/bin/env python3


import collections
import os
from typing import List

import cfnlint.core
import cfnlint.decode.cfn_yaml
import pytest

# Loading templates
Template = collections.namedtuple("Template", ["filename", "rule", "mode"])


def get_templates() -> List[Template]:
    def parse_filename(folder: str, filename: str) -> Template:
        values = filename.split(".")
        rule = values[0].split("-")[0].upper()
        mode = values[1].lower()

        return Template(os.path.join(folder, filename), rule, mode)

    template_folder = os.path.join(os.path.dirname(__file__), "templates")
    templates = [parse_filename(template_folder, filename) for filename in os.listdir(template_folder)]

    return templates


templates = get_templates()


@pytest.fixture(scope="session")
def rules():
    return cfnlint.core.get_rules(["cfn_lint_serverless.rules"], [], [])


def test_rule_with_templates(rules):
    """
    Test that all rules have at least one corresponding template
    """

    # Retrieve all serverless rule IDs
    rule_ids = set([r.id for r in rules if r.id[1] == "S"])

    # Retrieve all rule IDs for tests
    test_rule_ids = set([t[1] for t in templates])

    assert rule_ids == test_rule_ids


@pytest.mark.parametrize("filename,rule,mode", templates)
def test_template(filename, rule, mode, rules):
    """
    Automatically test all templates in the ./templates/ folder
    """

    template = cfnlint.decode.cfn_yaml.load(filename)
    matches = cfnlint.core.run_checks(
        filename,
        template,
        rules,
        # TODO: parametrize the region
        ["eu-west-1"],
    )

    match_ids = [match.rule.id for match in matches]

    if mode == "fail":
        # In case of a failure, there should be only one rule matching,
        # otherwise the test might not be scoped properly.
        assert match_ids == [rule]
    else:
        # In case of a pass, there shouldn't be any error.
        assert match_ids == []
