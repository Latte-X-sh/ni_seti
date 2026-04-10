# Ni - Seti

A CLI tool that allows you to easily setup your development machine on the go.

## Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd ni_seti

# Install with uv
uv pip install -e .
```

## Usage

### First Run

When you first run `niseti` without any configuration, you'll be greeted with an interactive setup:

```bash
niseti
```

This will show you a dropdown menu where you can select what to configure (currently AWS). Use arrow keys to navigate and press Enter to select.

### Configure AWS Profile

The interactive setup will prompt you for your AWS profile:
```
AWS_PROFILE [default]: ...change to profile name of your liking
```

This sets your default AWS profile that will be automatically exported in new shell sessions.

### Commands

- `niseti` - Run interactive setup (first time) or show help
- `niseti configure` - Reconfigure your settings
- `niseti shell-install` - Install shell integration (auto-export AWS_PROFILE on new shells)
- `niseti shell-uninstall` - Remove shell integration
- `niseti aws` - AWS-related commands

### Shell Integration

After configuring AWS, you can install shell integration to automatically export your AWS_PROFILE in every new shell session:

```bash
niseti shell-install
```

This adds a hook to your `.bashrc` or `.zshrc` that will:
- Automatically export your configured AWS_PROFILE when you open a new terminal
- Notify you if ni_seti is not configured yet

To activate immediately:
```bash
source ~/.bashrc  # or ~/.zshrc for zsh users
```

## Configuration

ni_seti stores its configuration in `~/.config/ni_seti/config.json`.

Example configuration:
```json
{
  "aws": {
    "profile": "my-dev-account",
    "program_mappings": {
      "k9s": "cluster-admin",
      "terraform": "infra-admin"
    }
  }
}
```

# Development:
### Note to self
- The current process is not working on my global shell since niseti is only functional
on my activate virtual environment. Being able to have this distributed will allow the cli
to work at a global scale.
- I need to balance interactivity with click as well

### Activate environment
-> eval $(poetry env activate) (new versions not tested)
-> use uv to install dependency packages.

### Installing and using UV (development)
#### installing uv
```
curl -LsSf https://astral.sh/uv/install.sh | sh
# install python versions
uv python install 3.11 3.12 3.13
```
### activate project environment
```
uv sync
source .venv/bin/activate
```

### Test your ansible
-> navigate to ansible folder 
-> run the following command:
ansible my_hosts -m ping -i inventory/inventory.ini -c local 
-> Ensure you place -c local since that indicates that the connection is locally bound.

# Project structure
```bash
├── ni_seti
│   ├── ansible
│   │   ├── inventory (*)
│   │   │   └── inventory.ini
│   │   ├── plays(*)
│   │   │   └── example_play
│   │   │       └── playbook.yml
│   │   ├── roles(*)
│   │   │   └── example_role
│   │   │       └── tasks
│   │   │           └── main.yaml
│   │   └── ssh.cfg
│   └── __init__.py
|   └── cli
├── poetry.lock
├── pyproject.toml
├── README.md
└── tests
    └── __init__.py
```
(Generated the above tree diagram by typing (tree) on the linux shell terminal.)

- The above tree diagram represents the project structure. Breaking it down further,
we have: 
    - 3 sub-parent folders marked in (*)astreix under the ansible folder.
    
        - inventory folder (stores your assets - servers etc)
        - plays folder (set of tasks to run against your servers)
        - roles (modular resuable tasks, default variables that can be shared across plays)
    
    - Folders outside the ansible file structure(the parent folder(ni-seti wrapping it all up)):

        - poetry.lock 
        - pyproject.toml
        - README.me (this file docs here!)
        - tests (at the time of reading, this is going to be a cli tool, have to test functionality)

# RoadMap
- Decided to plan this out to atleast have my desired features implemented.
    - [x] Have atleast one role to execute a task:
        - [ ] uv (install on base python)
        - [ ] docker
        - [ ] python (variants)
    - [ ] Have atleast one play that executes the role
        - [] one playbook with single role
        - [] one playbook with multiple roles
        - [] one playbook with multiple roles with logic
    - [ ] Have atleast a cli interface that executes the ansible code
        - [] the cli interface can print a menu
        - [] user can choose using 1 -4 what to do
        - [] the cli can used as a one liner
    - [ ] A frustration, a cli that detects aws workloasd (profile)
        - [] it prompts you which profile you need to active for each terminal session
    - [ ] Build a cli binary for ni_seti for all platforms
        - [ ] distribution via curl 
        
- Since ansible is used in a single line arg
- The cli will be mostly a menu driven that once it gathers all the input
- and prompts the user to confirm, initiates ansible with all the aquired
- inputs.
-> The flow will look like this
         -> one cli niti that be nested with other subcommands
         -> niti setup dev -> should prompt you
         -> niti
                -> setup (setting up machines enviroment) work_env (dev)
                -> deploy (push some data to x servers)
                -> build (etc)


# For Context switch for claude_code, I need to define explicit rules like GIT,
# For example, if i navigate to a work folder, X company and they have their own settings.
# I can define, teleport settings and even calude code settings (by default)
# I also have the chance to factor in explicit call saying, niti --profile WORK etc (can a default bash env)