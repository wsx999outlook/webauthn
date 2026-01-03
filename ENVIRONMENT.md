# Environment Configuration for User Testing

## Overview
This environment provides configuration and credentials for testing user authentication functionality within the WebAuthn project.

## User Accounts

### User 1
- **Email**: lam752499@gmail.com
- **Username**: lam752499
- **Password**: SecurePass123!
- **Status**: Active

### User 2
- **Email**: wsx7524999@outloom.com
- **Username**: wsx7524999
- **Password**: SecurePass456!
- **Status**: Active

## Configuration Files

### users-config.json
Contains the complete user configuration including:
- Email addresses
- Usernames
- Credentials (hashed in production)
- Account status
- Creation timestamps

## Testing Instructions

### Local Testing
1. Load the user configuration from `users-config.json`
2. Use the provided credentials to test authentication flows
3. Verify WebAuthn registration and authentication processes

### Environment Variables
For production use, set the following environment variables:
```bash
export WEBAUTHN_USER_1_EMAIL=lam752499@gmail.com
export WEBAUTHN_USER_1_USERNAME=lam752499
export WEBAUTHN_USER_1_PASSWORD=SecurePass123!

export WEBAUTHN_USER_2_EMAIL=wsx7524999@outloom.com
export WEBAUTHN_USER_2_USERNAME=wsx7524999
export WEBAUTHN_USER_2_PASSWORD=SecurePass456!
```

## Security Notes

⚠️ **Important**: 
- The credentials provided in this configuration are for **testing purposes only**
- In production environments, passwords should be properly hashed using bcrypt or similar
- Never commit real user credentials to version control
- Use environment variables or secure secret management for production deployments

## Integration

To integrate these users into a WebAuthn implementation:

1. **Registration Phase**:
   - User provides their email address
   - System creates WebAuthn credentials
   - Public key is stored server-side
   - Private key remains on user's device

2. **Authentication Phase**:
   - User provides their email/username
   - Challenge is issued by server
   - User's device signs the challenge
   - Server verifies the signature

## Example Usage

```javascript
// Example: Loading user configuration
const fs = require('fs');
const config = JSON.parse(fs.readFileSync('users-config.json', 'utf8'));

// Access user data
const users = config.users;
console.log(`Loaded ${users.length} users`);

users.forEach(user => {
  console.log(`Email: ${user.email}, Status: ${user.status}`);
});
```

## Maintenance

- Last Updated: 2026-01-03T21:14:40.000Z
- Configuration Version: 1.0.0
- Contact: Refer to users-config.json for user details
