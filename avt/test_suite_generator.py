from enum import Enum
import os
import shutil
from jinja2 import Environment, PackageLoader, select_autoescape

from avt.dto.config import Config
from avt.dto.test_case import TestCase

env = Environment(
    loader=PackageLoader("avt", "templates"),
    autoescape=select_autoescape()
)


class TestCases(Enum):
    RECORD_COUNT = "record_count.sql"
    DISTINCT_VALUES = "distinct_values.sql"


def __generate_test_cases_for_scenario(config: Config, scenario: str) -> list[TestCase]:
    """"""
    test_cases: list[TestCase] = []

    for table in config.targets:
        template = env.get_template(scenario)

        rendered_sql = template.render(
            target_schema=config.target_schema,
            source_schema=config.source_schema,
            target=table
        )

        test_case = TestCase.new(table.name, scenario, rendered_sql)

        test_cases.append(test_case)

    return test_cases

def __create_and_set_suite_dir(label: str, location: str) -> str:
    """
    Create or replace folder for test suite
    Returns the location filepath of the new folder
    """
    folder_name: str = "_".join([label, "test_suite"])
    full_path: str = os.path.join(location, folder_name)

    if os.path.exists(full_path):
        shutil.rmtree(full_path)

    os.mkdir(full_path)

    return full_path
            

def create_or_replace_test_suite(label: str, location: str, config: Config):

    test_cases: list[TestCase] = [
        __generate_test_cases_for_scenario(config, TestCases.RECORD_COUNT.value),
        __generate_test_cases_for_scenario(config, TestCases.DISTINCT_VALUES.value)
    ]

    suite_path = __create_and_set_suite_dir(label, location)

    print(test_cases)

    for case in sum(test_cases, []):  # sum(x, []) here does quick and dirty flatten
        case.save_query(suite_path)
    
