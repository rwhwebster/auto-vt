from jinja2 import Environment, PackageLoader, select_autoescape
import yaml

env = Environment(
    loader=PackageLoader("avt", "templates"),
    autoescape=select_autoescape()
)

def __render_config(target_tables: list[str]) -> dict:

    config_template = env.get_template("config.yaml")

    config_render = config_template.render(tables=target_tables)

    return yaml.safe_load(config_render)


def __write_config(config, dest: str):

    with open(dest, "w") as outfile:
        yaml.safe_dump(config, outfile)


def generate_config(target_tables_str: str, output: str):
    """
    Load the config template and use the provided target tables to
    generate the correct number of fields.

    Saves the rendered config file to the location specified
    in `output`
    """
    target_tables_list: list[str] = target_tables_str.strip().split(",")

    config_dict: dict = __render_config(target_tables_list)

    __write_config(config_dict, output)
