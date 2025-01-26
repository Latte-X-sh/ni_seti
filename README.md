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

- 