# Ni - Seti

# Development:

### Activate environment
-> eval $(poetry env activate) (new versions not tested)
-> poetry shell (will dive you deep down in the environment)

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
        - [ ] virtualenvwrapper (install on base python)
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