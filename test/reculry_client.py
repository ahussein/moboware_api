import recurly
from recurly  import Subscription

recurly.SUBDOMAIN = 'moboware'
recurly.API_KEY = '643b428845334d0daafb319e83fc3b46'

#client version <= 2.1.5
# subscriptions = Subscription.all()
# while subscriptions:
#     for subscription in subscriptions:
#         print 'Subscription: %s' % subscription
#     try:
#         subscriptions = subscriptions.next_page()
#     except PageError:
#         subscriptions = ()

#client version 2.1.6+

# get all subscriptions
for subscription in Subscription.all():
    print 'Subscription: %s' % subscription

print dir(subscription)
