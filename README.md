# trading-bot

Notes:
- use logging module to log processes
- put API keys, secrets, and passwords in an authentication.json file in the project directory (using the format specified in authentication_example.json)

TODO:
- implement coinbase exchange
- implement basic trading strategy
- look into best way to do error handling
  - handling of connection errors
  - handling of other runtime errors
  - emergency stop procedure
  - logging of errors
- check code with AWS CodeGuru
- plan out dash app for control
- implement dash app
  - e-mail notification
  - live view of performance over time
  - selection of exchange and bot
  - live view of price data
  - live view trades
- setup CI/CD pipeline to host on AWS