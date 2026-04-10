""" AWS commands"""
import click


@click.command()
def check_aws_install():
    click.echo("Check if user has aws configured in their machine")

@click.command()
def choose_profile_to_work_with():
    click.echo("list user's profile")


@click.command()
def set_env():
    click.echo("Set environment variable for aws!")
    