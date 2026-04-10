"""Shell integration for ni_seti"""
import os
import sys
from pathlib import Path


def get_shell_rc_file():
    """Detect the user's shell RC file"""
    shell = os.environ.get('SHELL', '')

    if 'zsh' in shell:
        return Path.home() / '.zshrc'
    elif 'bash' in shell:
        return Path.home() / '.bashrc'
    else:
        # Default to bashrc
        return Path.home() / '.bashrc'


def get_init_script_path():
    """Get the path to the shell init script"""
    # Get the directory where this module is located
    module_dir = Path(__file__).parent
    return module_dir / 'shell_init.sh'


def is_shell_integration_installed():
    """Check if shell integration is already installed"""
    rc_file = get_shell_rc_file()

    # prefer to use a custom binding to seperate code added by niseti
    # to not pollute the bashrc configuration file
    os.path
    if not rc_file.exists():
        return False

    with open(rc_file, 'r') as f:
        content = f.read()
        return 'ni_seti shell initialization' in content


def install_shell_integration():
    """Install shell integration by adding source line to RC file"""
    rc_file = get_shell_rc_file()
    init_script = get_init_script_path()

    if is_shell_integration_installed():
        print(f"✅ Shell integration already installed in {rc_file}")
        return True

    # Prepare the integration line
    integration_line = f'\n# ni_seti shell initialization\n[ -f "{init_script}" ] && source "{init_script}"\n'

    try:
        with open(rc_file, 'a') as f:
            f.write(integration_line)

        print(f"✅ Shell integration installed in {rc_file}")
        print(f"\n🔄 Run 'source {rc_file}' or open a new terminal for changes to take effect.")
        return True

    except Exception as e:
        print(f"❌ Failed to install shell integration: {e}", file=sys.stderr)
        return False


def uninstall_shell_integration():
    """Remove shell integration from RC file"""
    rc_file = get_shell_rc_file()

    if not rc_file.exists():
        print(f"No RC file found at {rc_file}")
        return False

    with open(rc_file, 'r') as f:
        lines = f.readlines()

    # Filter out ni_seti lines
    new_lines = []
    skip_next = False

    for line in lines:
        if 'ni_seti shell initialization' in line:
            skip_next = True
            continue
        if skip_next and 'source' in line and 'shell_init.sh' in line:
            skip_next = False
            continue

        new_lines.append(line)

    with open(rc_file, 'w') as f:
        f.writelines(new_lines)

    print(f"✅ Shell integration removed from {rc_file}")
    return True
