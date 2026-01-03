# User Management for WebAuthn Project

This directory contains user configuration and credentials for the WebAuthn project.

## Quick Start

### Validate User Configuration
Run the test script to validate the user configuration:

```bash
python3 test-user-config.py
```

### Load Configuration in Your Code

**JavaScript/Node.js:**
```javascript
const fs = require('fs');
const config = JSON.parse(fs.readFileSync('users-config.json', 'utf8'));
const users = config.users;
```

**Python:**
```python
import json

with open('users-config.json', 'r') as f:
    config = json.load(f)
    users = config['users']
```

## Files

- **users-config.json** - Main user configuration file containing email addresses and credentials
- **test-user-config.py** - Validation script for user configuration
- **.env.example** - Example environment variables configuration
- **ENVIRONMENT.md** - Detailed documentation for environment setup and testing

## Configured Users

1. **lam752499@gmail.com**
   - Username: lam752499
   - Status: Active
   - Created: 2026-01-03

2. **wsx7524999@outloom.com**
   - Username: wsx7524999
   - Status: Active
   - Created: 2026-01-03

## Environment Setup

### For Local Development

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Update `.env` with your local configuration if needed

3. Load environment variables in your application

### For Production

Use a secure secret management system and never commit actual credentials to version control.

## Security Best Practices

⚠️ **Important Security Notes:**

1. **Password Hashing**: The passwords in `users-config.json` are examples. In production:
   - Use bcrypt, argon2, or similar for password hashing
   - Never store plain-text passwords

2. **Secret Management**: 
   - Use environment variables for sensitive data
   - Consider using secret management tools (e.g., HashiCorp Vault, AWS Secrets Manager)

3. **Access Control**:
   - Restrict file permissions on config files: `chmod 600 users-config.json`
   - Use `.gitignore` to prevent committing sensitive `.env` files

4. **Regular Updates**:
   - Rotate passwords regularly
   - Update credentials after any security incident

## Testing

The included test script validates:
- JSON structure integrity
- Required fields presence
- Email format validation
- Credentials structure

Run tests before deploying:
```bash
python3 test-user-config.py
```

## Integration with WebAuthn

These user accounts can be integrated with WebAuthn authentication:

1. **Registration Flow**:
   - User provides email from config
   - Generate WebAuthn credentials
   - Store public key server-side

2. **Authentication Flow**:
   - Identify user by email/username
   - Issue WebAuthn challenge
   - Verify signed response

See [ENVIRONMENT.md](ENVIRONMENT.md) for detailed integration examples.

## Maintenance

- Configuration Version: 1.0.0
- Last Updated: 2026-01-03T21:14:40.000Z
- Maintainer: Project team

## Support

For issues or questions about user configuration:
1. Check [ENVIRONMENT.md](ENVIRONMENT.md) for detailed documentation
2. Run `test-user-config.py` to validate configuration
3. Review the main [README.md](README.md) for project information
