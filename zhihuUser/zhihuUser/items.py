# -*- coding = utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in =
# https =//docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class UserItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = Field()
    name = Field()
    avatar_url = Field()
    url_token = Field()
    use_default_avatar = Field()
    avatar_url_template = Field()
    is_org = Field()
    type = Field()
    url = Field()
    user_type = Field()
    headline = Field()
    gender = Field()
    is_advertiser = Field()
    vip_info = Field()
    badge = Field()
    allow_message = Field()
    is_following = Field()
    is_followed = Field()
    is_blocking = Field()
    follower_count = Field()
    answer_count = Field()
    articles_count = Field()
    employments = Field()
    is_realname = Field()
    self_recommend = Field()

