""" Main entry point for ni_seti cli """
import click
from .. import config, setup, shell_integration


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    """ni_seti - Development environment configuration tool"""
    # If no subcommand is provided, check configuration
    if ctx.invoked_subcommand is None:
        if not config.config_exists():
            # First run - show setup
            setup.run_setup()
        else:
            # Configuration exists, show help
            click.echo(ctx.get_help())


@click.command()
def configure():
    """Configure or reconfigure ni_seti settings"""
    setup.reconfigure()


@click.group()
def aws():
    """AWS environment configuration"""
    click.echo("Set aws environment variables")


@click.command()
def set_env():
    """Set environment variable for AWS"""
    click.echo("Set environment variable for aws!")


@click.command()
def shell_install():
    """Install shell integration (auto-run on new shells)"""
    shell_integration.install_shell_integration()


@click.command()
def shell_uninstall():
    """Uninstall shell integration"""
    shell_integration.uninstall_shell_integration()


# Register commands
main.add_command(configure)
main.add_command(shell_install, name='shell-install')
main.add_command(shell_uninstall, name='shell-uninstall')
main.add_command(aws)
aws.add_command(set_env)
