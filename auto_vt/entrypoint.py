import click

from auto_vt.config_generator import generate_config
from auto_vt.config_parser import load_parse_config

@click.group()
def cli():
    pass

@cli.command()
@click.option("--targets", default="TEMP_TABLE", help="Comma-separated list of table names to include as targets in the config")
@click.option("--output", "-o", "output", default="config.yaml", help="Destination filepath for generated config")
def new_config(targets, output):
    """
    Creates a new config file to populate with details for TVT generation
    Takes a list of target tables and an output filepath as options
    """
    generate_config(targets, output)

@cli.command()
@click.option("--config", default="config.yaml", help="Location of the config file from which to generate test cases")
@click.option("--label", "-l", default=None, help="A label used to name the outputted test suite")
def run(config, label):
    """Use a completed config file to auto-generate TVT scripts"""
    load_parse_config(config)


if __name__ == "__main__":

    cli()
    