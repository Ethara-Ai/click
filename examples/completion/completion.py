import os

import click
from click.shell_completion import CompletionItem


@click.group()
def cli():
    pass


@cli.command()
@click.option("--dir", type=click.Path(file_okay=False))
def ls(dir):
    pass


def get_env_vars(ctx, param, incomplete):
    # Returning a list of values is a shortcut to returning a list of
    # CompletionItem(value).
    pass


@cli.command(help="A command to print environment variables")
@click.argument("envvar", shell_complete=get_env_vars)
def show_env(envvar):
    pass


@cli.group(help="A group that holds a subcommand")
def group():
    pass


def list_users(ctx, param, incomplete):
    # You can generate completions with help strings by returning a list
    # of CompletionItem. You can match on whatever you want, including
    # the help.
    pass


@group.command(help="Choose a user")
@click.argument("user", shell_complete=list_users)
def select_user(user):
    pass


cli.add_command(group)
