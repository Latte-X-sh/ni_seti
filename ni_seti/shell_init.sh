#!/bin/bash
# ni_seti shell initialization
# This script is sourced on every new shell session

# Check if ni_seti is installed
if command -v niseti &> /dev/null; then
    # Export AWS_PROFILE if configured
    NI_SETI_CONFIG="$HOME/.config/ni_seti/config.json"

    if [ -f "$NI_SETI_CONFIG" ]; then
        # Extract AWS profile from config using python
        AWS_PROFILE_VALUE=$(python3 -c "import json; print(json.load(open('$NI_SETI_CONFIG')).get('aws', {}).get('profile', ''))" 2>/dev/null)

        if [ -n "$AWS_PROFILE_VALUE" ]; then
            export AWS_PROFILE="$AWS_PROFILE_VALUE"
        fi
    else
        # No configuration found - notify user
        echo "⚠️  ni_seti: No configuration found. Run 'niseti' to setup."
    fi
fi
