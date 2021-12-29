# Alpaca Markets Trading Bot

- ## Description
 
    API based trading bot with **GRID** trading strategy. Since Alpaca Markets does not support separating orders of 
    one instrument into several orders, the bot is practicing on position increasing and reducing to implement 
    grid strategy. Only support long call and not planing in building for short call. Performance still in **TESTING**.
    
- ## Background

    Have been trading for stock index and crypto for few years and have made a lot of profit. However, still want to
    build a more sensitive trading tool to catch more profit. The idea and basic trading logic are same as my manual
    trading. For indexes (ex. NASDAQ, SPX and etc), as long as the U.S. exist, the bot will bring continuous profit 
    with long call only.
    
- ## Basic Logic
    - Place an initial order with around/less than half position.
    - Bot will detect market movement every minute (could be more frequent based on API limitation).
    
    Currently for or **long call only**:
    - When market price moved up and exceeded pre-set bias, reduce the position size to keep current value as same as the market value of the initial position.
    - When market price moved down and exceeded pre-set bias, add to the position to keep current value as same as the market value of the initial position.
    
    - Profit comes from the position reduce in bull market.
    
- ## In Building Features

    - Account position control preventing insufficient position in bear market.
    - Auto initial position.
    - Auto bias calculation based on ATR.
    - Watching different instruments at the same time without running more instance.
 