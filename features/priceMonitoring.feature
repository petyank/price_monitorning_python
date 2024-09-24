Feature: BTC-USD prices volatility

    Scenario Outline: Monitor BTC-USD volatility over a given time interval
        Given I open the Google Finance 'BTC-USD' quote website
        When I monitor the BTC-USD price for a duration of <N> minutes at intervals of <M> seconds
        Then the average BTC-USD price does not vary by more than 1 %
        Then there are no values that vary by more than 2 %
        Examples:
            | N | M |
            | 1 | 10 |
            | 3 | 10 |
            | 5 | 10 |