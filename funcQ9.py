import functools
import operator

tweets = ["First ever player to score 6000 runs in #IPL - Just another day at the ‘office’ for #ViratKohli!",
          "My ⁦@rajasthanroyals outfit has arrived! Now to be well enough to wear it....Thanks ⁦@IamSanjuSamson & the RR management! All the best for the rest of the #IPL!",
         "How amazing that both the centuries in this year’s #IPL have been scored by Malayalis, when Kerala has so long been regarded as a cricketing backwater!",
         "Most 10-wicket wins in IPL: 4 - RCB, 2 - MI, 2 - SRH, 2 - CSK #RCBvsRR #RCB #RR #IPL #IPL2021 #CricTracker",
         "India would have never eliminated polio, if people had to BUY polio vaccines. Same logic applies for #COVID19",
         "The Ontario Science Table @COVIDSciOntario has recommended that 50% of all available vaccines go to hotspot neighbourhoods with the highest rates of #COVID19. RT if you agree the Ontario government should immediately do this to save lives.",
         "UPA home minister resigned after terror attack on Mumbai. Why doesn’t NDA health minister resign for this #COVID19 mess? I would prefer Modi to resign as buck stops at him.But being thick skinned, he won’t!",
         "Khalsa Aid India arranges Oxygen concentrators for COVID-19 patients, will deliver them in Delhi. #COVID19"]

ipl = ["#ipl"] * len(tweets)
covid = ["#covid19"] * len(tweets)

def segregate_tweets(lst, topic):
    if topic in lst.lower():
        return lst

resultipl = list(map(segregate_tweets, tweets, ipl))
resultcovid = list(map(segregate_tweets, tweets, covid))

def filter_list(lst):
    if lst != "":
        return lst

result_ipl = list(filter(filter_list, resultipl))
result_covid = list(filter(filter_list, resultcovid))

print("IPL tweets: {}".format(len(result_ipl)))
print("COVID19 tweets: {}".format(len(result_covid)))