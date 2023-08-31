from dataclasses import dataclass

from avt.dto.target import Target

@dataclass
class Config:
    source_schema: str
    target_schema: str
    targets: list[Target]

    @classmethod
    def from_yaml(cls, config_yaml: dict):

        target_tables = [
            Target.from_yaml(table) for table in config_yaml["target_tables"]
        ]

        new_config = cls(
            source_schema = config_yaml["source_schema"],
            target_schema = config_yaml["target_schema"],
            targets = target_tables
        )

        return new_config