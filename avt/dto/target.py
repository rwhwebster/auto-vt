from dataclasses import dataclass

@dataclass
class Target:
    name: str
    source: str
    primary_key: str | None
    source_scd_type: int
    target_scd_type: int

    @classmethod
    def from_yaml(cls, config_dict):
        
        return cls(
            name = config_dict["target_table"],
            source = config_dict["source_table"],
            primary_key = config_dict["primary_key"],
            target_scd_type = config_dict["target_scd_type"],
            source_scd_type = config_dict["source_scd_type"]
        )