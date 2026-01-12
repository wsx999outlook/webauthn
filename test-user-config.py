#!/usr/bin/env python3
"""
Test script to validate user configuration
This script loads and validates the users-config.json file
"""

import json
import sys
from pathlib import Path

def load_user_config():
    """Load user configuration from JSON file"""
    config_path = Path(__file__).parent / 'users-config.json'
    
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        print(f"Error: Configuration file not found at {config_path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in configuration file: {e}")
        sys.exit(1)

def validate_user(user, index):
    """Validate a single user configuration"""
    required_fields = ['email', 'username', 'credentials', 'status', 'created']
    missing_fields = [field for field in required_fields if field not in user]
    
    if missing_fields:
        print(f"❌ User {index}: Missing required fields: {', '.join(missing_fields)}")
        return False
    
    # Validate email format
    email = user['email']
    if '@' not in email or '.' not in email.split('@')[1]:
        print(f"❌ User {index}: Invalid email format: {email}")
        return False
    
    # Validate credentials
    if 'password' not in user['credentials']:
        print(f"❌ User {index}: Missing password in credentials")
        return False
    
    print(f"✅ User {index}: {user['email']} - Valid")
    return True

def main():
    """Main test function"""
    print("=" * 60)
    print("WebAuthn User Configuration Test")
    print("=" * 60)
    
    # Load configuration
    config = load_user_config()
    print(f"\n📋 Configuration loaded successfully")
    print(f"   Version: {config.get('metadata', {}).get('version', 'unknown')}")
    print(f"   Description: {config.get('metadata', {}).get('description', 'N/A')}")
    
    # Validate users
    users = config.get('users', [])
    print(f"\n👥 Found {len(users)} user(s)")
    print("-" * 60)
    
    all_valid = True
    for i, user in enumerate(users, 1):
        if not validate_user(user, i):
            all_valid = False
    
    print("-" * 60)
    
    # Summary
    if all_valid:
        print("\n✅ All users validated successfully!")
        print("\nUser Summary:")
        for i, user in enumerate(users, 1):
            print(f"  {i}. {user['email']} (Username: {user['username']}, Status: {user['status']})")
        return 0
    else:
        print("\n❌ Validation failed for one or more users")
        return 1

if __name__ == '__main__':
    sys.exit(main())
