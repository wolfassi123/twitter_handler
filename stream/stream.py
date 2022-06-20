import threading
import os
from typing import Optional

from dotenv import load_dotenv
from tweepy import StreamingClient, StreamRule

load_dotenv()

bearer_token = os.getenv("bearer_token")


class Streamer(StreamingClient):
    # def on_response(self, response):
    #     pass

    def on_tweet(self, tweet):
        pass

    # def on_data(self, data):
    #     pass

    def on_matching_rules(self, rule):
        print(rule)
        print("-" * 50)

    def on_disconnect(self):
        print("*" * 50)
        print("DISCONNECT!")

    def on_closed(self, response):
        print(response)
        print("CLOSED!")

    def delete_all_rules(self):
        list_rules_ids = []
        all_rules = self.get_rules()
        all_rules_data = all_rules['data']
        for rule_data in all_rules_data:
            list_rules_ids.append(rule_data['id'])
        for id in list_rules_ids:
            print(f"Deleting the rule with the following id: {id} ")
            self.delete_rules(id)
            print(f"-----Delete Done-----")

    def delete_rule(self, r_id: str):
        print(f"Deleting the rule with the following id: {r_id} ")
        self.delete_rules(r_id)
        print(f"-----Delete Done-----")

    def create_rule(
        self, r_value: str, r_tag: Optional[str] = None, r_id: Optional[str] = None
    ):
        rule = StreamRule(value=r_value, tag=r_tag, id=r_id)
        self.add_rules(rule)

    def show_all_rules(self):
        list_rules = []
        rules_data = self.get_rules()['data']
        print("Here are the rules that have been defined:")
        num_rules = 0
        for rule_data in rules_data:
            rule_dict = {}
            rule_dict["value"] = rule_data[0]
            rule_dict["tag"] = rule_data[1]
            rule_dict["id"] = rule_data[2]
            print(rule_data)
            num_rules += 1
            list_rules.append(rule_dict)
        print(f"The total number of rules are: {num_rules}")
        return list_rules

    def get_rule(self, r_tag: str):
        all_rules = self.show_all_rules()
        found = False
        for rule in all_rules:
            if rule["tag"] == r_tag:
                print(f"A rule with the following tag '{r_tag}' was found.")
                print(f"The rule has the following id: {rule['id']}")
                found = True
                needed_id = rule["id"]
        if found == False:
            print(f"A rule with the following tag '{r_tag}' was not found")
        return needed_id

    def delete_rule_by_tag(self, r_tag: str):
        print(f"Deleting the rule with the following tag: '{r_tag}' ")
        r_id = self.get_rule(r_tag)
        self.delete_rules(r_id)
        print(f"-----Delete Done-----")

    def get_tag_query(self, r_tag: str):
        all_rules = self.show_all_rules()
        found = False
        for rule in all_rules:
            if rule["tag"] == r_tag:
                print(f"A rule with the following tag '{r_tag}' was found.")
                print(f"The rule has the following id: {rule['id']}")
                found = True
                query = rule["value"]
        if found == False:
            print(f"A rule with the following tag '{r_tag}' was not found")
        return query


# test = Streamer(bearer_token, return_type=dict)

# test.create_rule(r_value = "Premier League",r_tag="premier_league")
# test.create_rule(r_value = "English Football",r_tag="english_football")
# test.show_all_rules()


# test.get_rule("premier_league")
# test.delete_rule_by_tag("premier_league")
# x = test.get_tag_query("english_football")
# print(x)


# test.delete_all_rules()

# test.filter(tweet_fields=["created_at"])
# test.filter(tweet_fields=['created_at','attachments','context_annotations','conversation_id','entities','in_reply_to_user_id','lang','possibly_sensitive','public_metrics','referenced_tweets','reply_settings','source'],
#             expansions=['author_id','referenced_tweets.id','in_reply_to_user_id','attachments.media_keys','attachments.poll_ids','entities.mentions.username','referenced_tweets.id.author_id'],
#             user_fields=['created_at','description','entities','location','pinned_tweet_id','profile_image_url','protected','public_metrics','url','verified'],
#             poll_fields=['duration_minutes','end_datetime','voting_status'],
#             media_fields=['url','duration_ms','height','preview_image_url','public_metrics','alt_text','variants'])

# test.delete_all_rules()
