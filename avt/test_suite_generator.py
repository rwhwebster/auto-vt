from enum import Enum
from jinja2 import Environment, PackageLoader, select_autoescape

from avt.dto.config import Config

env = Environment(
    loader=PackageLoader("auto_vt", "templates"),
    autoescape=select_autoescape()
)


class TestCases(Enum):
    RECORD_COUNT = "record_count.sql"
    DISTINCT_VALUES = "distinct_values.sql"


def __generate_record_count_test_cases(config) -> list[str]:
    """"""
    test_cases = []

    for table in config.targets:
        template = env.get_template(TestCases.RECORD_COUNT.value)

        rendered_sql = template.render(
            target_schema=config.target_schema,
            source_schema=config.source_schema,
            target_table=table.name,
            source_table=table.source
        )

        test_cases.append(rendered_sql)

    return test_cases


def create_or_replace_test_suite(label: str, location: str, config: Config):
    
    record_count_cases = __generate_record_count_test_cases(config)
