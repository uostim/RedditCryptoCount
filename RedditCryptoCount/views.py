from django.shortcuts import render, redirect
from .models import LastCount, ThisCount, CheckedPosts
import requests
from RedditCryptoCount import secrets
import praw
import re


def latest_count(request):
    table = LastCount.objects.all().order_by("-thiscount")
    return render(request, "latest_count.html", {"table": table})


def get_coin_list():
    r = requests.get("https://api.coinmarketcap.com/v1/ticker/?limit=250")
    print("Status Code: {}".format(r.status_code))
    if r.status_code == 200:
        print("Got details of top 250 coins")
        for coin in r.json():
            if LastCount.objects.filter(coin_symbol=coin["symbol"]).exists() == False:
                LastCount(coin_id=coin["id"], coin_name=coin["name"], coin_symbol=coin["symbol"]).save()


def update_coin_list(request):
    get_coin_list()
    count_mentions()
    return redirect("latest_count")


def count_mentions():
    
    CheckedPosts.objects.all().delete()
    
    user_agent=secrets.user_agent
    client_id=secrets.client_id
    client_secret=secrets.client_secret
    username=secrets.username
    pword=secrets.pword
    
    subreddit_to_read='CryptoMarkets+CryptoCurrency+CryptoCurrencies+CryptoCurrencyTrading'
    new_post_limit = 1000
    
    reddit = praw.Reddit(user_agent=user_agent, client_id=client_id, client_secret=client_secret, username=username, password=pword)
    subreddit = reddit.subreddit(subreddit_to_read)
    submissions = subreddit.new(limit=new_post_limit)
    print("Got {} posts from {}".format(new_post_limit, subreddit_to_read))
    
    submission_list = []
    for s in submissions:
        if CheckedPosts.objects.filter(post_title=s.title).exists() == False:
            CheckedPosts(post_title=s.title).save()
            submission_list.append("{} {}".format(s.title, s.selftext))
    
    coins = LastCount.objects.all()
    
    for coin in coins:
        print("Checking for {}".format(coin))
        coin_count = 0
        for submission in submission_list:
            
            regex_id = r"[A-z]{0}[A-z]|[A-z]{0}|{0}[A-z]".format(coin.coin_id)
            regex_name = r"[A-z]{0}[A-z]|[A-z]{0}|{0}[A-z]".format(coin.coin_name)
            regex_symbol = r"[A-z]{0}[A-z]|[A-z]{0}|{0}[A-z]".format(coin.coin_symbol)
            
            if coin.coin_id in submission or coin.coin_name in submission or coin.coin_symbol in submission:
                if re.match(regex_id, submission) is None and re.match(regex_name, submission) is None and re.match(regex_symbol, submission) is None:
                    coin_count = coin_count + 1

        coin.lastcount6 = coin.lastcount5
        coin.lastcount5 = coin.lastcount4
        coin.lastcount4 = coin.lastcount3
        coin.lastcount3 = coin.lastcount2
        coin.lastcount2 = coin.lastcount
        coin.save()
        lastcount = coin.thiscount
        print("coin.lastcount = {}".format(coin.lastcount))
        print("new thiscount = {}".format(coin_count))
        
        if lastcount is None or lastcount == 0:
            if coin_count > 0:
                pc_diff = 100
            else:
                pc_diff = 0
        else:
            pc_diff = ((coin_count/lastcount)*100)-100
        
        coin.lastount = lastcount
        coin.thiscount = coin_count
        coin.pc_diff = pc_diff
        coin.coin_count = coin_count
        coin.save()
