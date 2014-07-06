#!/usr/bin/env python2
# -*- coding: utf-8 -*- #

from twitterbot import TwitterBot
import yaml
import random

class HeptagonBot(TwitterBot):
    def bot_init(self):
        """
        Initialize and configure your bot!

        Use this function to set options and initialize your own custom bot
        state (if any).
        """

        ############################
        # REQUIRED: LOGIN DETAILS! #
        ############################

        tokens = yaml.load(open('./config.yaml'))
        self.config.update(tokens)

        ######################################
        # SEMI-OPTIONAL: OTHER CONFIG STUFF! #
        ######################################

        # how often to tweet, in seconds
        self.config['tweet_interval'] = 30 * 60     # default: 30 minutes

        # use this to define a (min, max) random range of how often to tweet
        # e.g., self.config['tweet_interval_range'] = (5*60, 10*60) # tweets every 5-10 minutes
        self.config['tweet_interval_range'] = None

        # only reply to tweets that specifically mention the bot
        self.config['reply_direct_mention_only'] = False

        # only include bot followers (and original tweeter) in @-replies
        self.config['reply_followers_only'] = True

        # fav any tweets that mention this bot?
        self.config['autofav_mentions'] = True

        # fav any tweets containing these keywords?
        self.config['autofav_keywords'] = ['heptagon']

        # follow back all followers?
        self.config['autofollow'] = True


        ###########################################
        # CUSTOM: your bot's own state variables! #
        ###########################################
        
        # If you'd like to save variables with the bot's state, use the
        # self.state dictionary. These will only be initialized if the bot is
        # not loading a previous saved state.

        # self.state['butt_counter'] = 0

        # You can also add custom functions that run at regular intervals
        # using self.register_custom_handler(function, interval).
        #
        # For instance, if your normal timeline tweet interval is every 30
        # minutes, but you'd also like to post something different every 24
        # hours, you would implement self.my_function and add the following
        # line here:
        
        # self.register_custom_handler(self.my_function, 60 * 60 * 24)

        # Add custom functions that respond to searches run at regular intervals
        # using self.register_search_handler('query', function, interval [, searchparams] )
        #
        # If using search handlers, you must set self.state['search_handlers']
        self.state['search_handlers'] = {}
        self.register_search_handler("'a love heptagon'", self.on_love_heptagon, 600)


    def on_love_heptagon(self, results):
        """
        Generate porn music in response to phrase 'a love heptagon'
        """
        for tweet in results:
            wakachika = ''

            if random.randrange(0,4):
                wakachika += self._make_bow() + ' ' + self._make_chicka() + ' ' + self._make_bow()
            else:
                wakachika += 'O' + 'h' * random.randrange(1,4) + ' '
                wakachika += 'm' + 'y' * random.randrange(2,8)
                wakachika += '!' * random.randrange(0,2)

            url = 'http://twitter.com/' + tweet.author.id_str + '/status/' + tweet.id_str
            text = wakachika + '\r\n' + url

            self.post_tweet(text)


    def _make_bow(self):
        bow = ''

        if random.randrange(2):
            bow += 'b'
        else:
            bow += 'w'

        bow += 'ow'

        while random.randrange(2):
            bow += ' '
            if random.randrange(2):
                bow += 'b'
            else:
                bow += 'w'
            if random.randrange(4):
                bow += 'ow'
            else:
                bow += 'aw'
            while random.randrange(3) > 2:
                bow += 'w'

        return bow


    def _make_chicka(self):
        chicka = ''

        reps = 0
        while reps < 1 + random.randrange(0,1):
            if random.randrange(3):
                chicka += 'chi'
                if random.randrange(2):
                    chicka += 'ck'
                else:
                    chicka += 'kk'
            else:
                chicka += 'w'
                if random.randrange(2):
                    chicka += 'a'
                else:
                    chicka += 'o'
                if random.randrange(2):
                    chicka + 'k'
                else:
                    chicka += 'kk'
            chicka += 'a'
            reps += 1

        return chicka


    def on_scheduled_tweet(self):
        """
        Make a public tweet to the bot's own timeline.

        It's up to you to ensure that it's less than 140 characters.

        Set tweet frequency in seconds with TWEET_INTERVAL in config.py.
        """
        # text = function_that_returns_a_string_goes_here()
        # self.post_tweet(text)

        pass
        

    def on_mention(self, tweet, prefix):
        """
        Defines actions to take when a mention is received.

        tweet - a tweepy.Status object. You can access the text with
        tweet.text

        prefix - the @-mentions for this reply. No need to include this in the
        reply string; it's provided so you can use it to make sure the value
        you return is within the 140 character limit with this.

        It's up to you to ensure that the prefix and tweet are less than 140
        characters.

        When calling post_tweet, you MUST include reply_to=tweet, or
        Twitter won't count it as a reply.
        """
        # text = function_that_returns_a_string_goes_here()
        # prefixed_text = prefix + ' ' + text
        # self.post_tweet(prefix + ' ' + text, reply_to=tweet)

        # call this to fav the tweet!
        # if something:
        #     self.favorite_tweet(tweet)

        pass


    def on_timeline(self, tweet, prefix):
        """
        Defines actions to take on a timeline tweet.

        tweet - a tweepy.Status object. You can access the text with
        tweet.text

        prefix - the @-mentions for this reply. No need to include this in the
        reply string; it's provided so you can use it to make sure the value
        you return is within the 140 character limit with this.

        It's up to you to ensure that the prefix and tweet are less than 140
        characters.

        When calling post_tweet, you MUST include reply_to=tweet, or
        Twitter won't count it as a reply.
        """
        # text = function_that_returns_a_string_goes_here()
        # prefixed_text = prefix + ' ' + text
        # self.post_tweet(prefix + ' ' + text, reply_to=tweet)

        # call this to fav the tweet!
        # if something:
        #     self.favorite_tweet(tweet)

        pass

if __name__ == '__main__':
    bot = HeptagonBot()
    bot.run()
