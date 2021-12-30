# trading-bot

Notes:
- use logging module to log processes

TODO:
- look into best way to do error handling
  - handling of connection errors
  - handling of random runtime errors
  - emergency stop procedure?
  - logging of errors
- plan out dash app for control
- implement dash app

# example authentication json file
{
  "exchange_one": {
    "key": "api_key",
    "secret": "api_secret",
    "password": "api_password"
  },

  "exchange_two_no_password_required": {
    "key": "api_key",
    "secret": "api_secret",
    "password": ""
  }
}