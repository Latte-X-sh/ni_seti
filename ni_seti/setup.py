"""Interactive setup flow for ni_seti"""
import questionary
from questionary import Style
from . import config, shell_integration


# Custom style for the menu
custom_style = Style([
    ('qmark', 'fg:#673ab7 bold'),
    ('question', 'bold'),
    ('answer', 'fg:#2196f3 bold'),
    ('pointer', 'fg:#673ab7 bold'),
    ('highlighted', 'fg:#673ab7 bold'),
    ('selected', 'fg:#2196f3'),
])


def run_setup():
    """Run the interactive setup flow"""
    print("\n🎉 Welcome to ni_seti!")
    print("Let's get your development environment configured.\n")

    # Show dropdown menu
    choice = questionary.select(
        "What would you like to setup?",
        choices=[
            "AWS",
            "(More options coming...)"
        ],
        style=custom_style
    ).ask()

    if choice == "AWS":
        setup_aws()
    elif choice == "(More options coming...)":
        print("Stay tuned for more configuration options!")
        return False

    return True


def setup_aws():
    """Setup AWS configuration"""
    print("\n🔧 AWS Configuration")

    # Prompt for AWS profile
    profile = questionary.text(
        "AWS_PROFILE [default]:",
        default="default",
        instruction="Change to profile name of your liking"
    ).ask()

    if profile:
        config.set_aws_profile(profile)
        print(f"\n✅ AWS profile set to: {profile}")

        # Offer shell integration
        if not shell_integration.is_shell_integration_installed():
            print("\n📋 Shell Integration")
            install_shell = questionary.confirm(
                "Would you like to install shell integration?\n   (This will automatically export AWS_PROFILE in new shell sessions)",
                default=True
            ).ask()

            if install_shell:
                shell_integration.install_shell_integration()
        else:
            print("✅ Shell integration is already installed.")

        return True

    return False


def reconfigure():
    """Reconfigure existing settings"""
    print("\n🔄 Reconfiguration")

    # Load existing config
    existing_config = config.load_config()

    if existing_config:
        print("Current configuration:")
        if 'aws' in existing_config:
            aws_config = existing_config['aws']
            if 'profile' in aws_config:
                print(f"  AWS Profile: {aws_config['profile']}")
            if 'program_mappings' in aws_config and aws_config['program_mappings']:
                print(f"  Program Mappings: {aws_config['program_mappings']}")
        print()

    # Run setup again
    run_setup()
