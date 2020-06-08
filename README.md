[![number-game](https://circleci.com/gh/circleci/circleci-docs.svg?style=svg)](https://app.circleci.com/pipelines/github/imisi-akande/number-game/8/workflows/b6dd4256-c126-47d8-b38c-8780aa17204a/jobs/11/steps)    [![Coverage Status](https://coveralls.io/repos/github/imisi-akande/number-game/badge.svg?branch=develop)](https://coveralls.io/github/imisi-akande/number-game?branch=develop)

# The Number Game

This Python module allows you to guess random numbers within your selected
number of attempts. It also allows you to guess Prime numbers within your
selected number of attempts.

## Instructions
- Enter your terminal

- Install the module:
    - ```pip install nummer-games```

- Enter your python interactive shell:
    - ```python```

- Import required functions:
    - ```from nummer_games import Classify, Prime```

- Iterate through attempts by guessing random numbers:
    - ```Classify(n).guess_number()```

- Iterate through attempts by guessing prime numbers:
    - ```Prime(n).guess_prime_number()```

- Note:
    - n represents the number of attempts

- Illustration
    - You can look into the screenshots or commands below to follow through the
      process of guessing random numbers and prime numbers in three attempts.

    - ![Random numbers](https://github.com/imisi-akande/number-game/blob/develop/images/guess_numbers.png)
        - ```python```
        - ```from nummer_games import Classify, Prime```
        - ```Classify(3).guess_number()```


    - ![Prime numbers](https://github.com/imisi-akande/number-game/blob/develop/images/guess_prime_numbers.png)
        - ```python```
        - ```from nummer_games import Classify, Prime```
        - ```Prime(3).guess_prime_number()```

Have fun. Please Feel free to contact me if you encounter any issue.