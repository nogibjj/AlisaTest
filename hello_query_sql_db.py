#!/usr/bin/env python

import click
from dblib.querydb import querydb

# build a click group
@click.group()
def cli():
    """Execute a SQL query from artist database to find artists of a certain country"""


# build a click command
@cli.command()
@click.option("--country", default="American", help="Please type the nationality of artists you are interested in.")

def cli_query(country):
    """Execute a SQL query from artist database to find artists of a certain country"""
    querydb(country)



# run the CLI
if __name__ == "__main__":
    cli()
