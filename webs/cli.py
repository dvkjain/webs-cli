import click

from .search_command import Code as search

@click.group()
def cli():
    
    "wsearch is a simple command line tool that allows basic spreadsheet manipulation through a terminal window."

cli.add_command(search.search)
