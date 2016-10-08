#!/opt/local/bin/python3.3
import math


def choose_good_gift(current_gift, gifts_in_bag, gift_number):
    global best
    if gift_number == 1:
        best = current_gift
    elif gift_number < gifts_in_bag / math.e:
        best = max(best, current_gift)
    elif current_gift > best or gift_number == gifts_in_bag:
        return True
    return False


if __name__ == '__main__':
    from random import random, randint, uniform

    scale = (random() + random()) ** randint(0, 1024)

    standings = gift_count = best_gifts = 0
    bag_count = 2000
    for i in range(bag_count):
        gifts_in_bag = randint(10, 1000)
        gift_count += gifts_in_bag

        gifts = []
        selected_gift = None
        for i in range(gifts_in_bag):
            new_gift = uniform(0., scale)
            gifts.append(new_gift)
            decision = choose_good_gift(new_gift, gifts_in_bag, i + 1)
            if decision:
                selected_gift = new_gift
                gifts.extend([uniform(0., scale) for _ in range(gifts_in_bag - i - 1)])
                break
        if selected_gift is None:
            priority = len(gifts)
        else:
            priority = sum(selected_gift < x for x in gifts)
        standings += priority
        best_gifts += not priority
    print('You do won {:n} best gifts from {:n} bags with {:,} gifts!\n'
          'It seems like for bags of {:n} gifts -\n'
          'you would choose the second best gift, silver ;)'
          .format(best_gifts, bag_count, gift_count, round(gift_count / standings) + 1))


#def choose_good_gift(total_gifts, bag, accept_gift):
#    best = 0
#    skip = total_gifts / math.e
#    for i, gift in enumerate(bag()):
#        if i < skip:
#            best = max(best, gift)
#        elif gift > best or i == total_gifts - 1:
#            accept_gift()
#            return
#
#if __name__ == '__main__':
#    from random import random, randint, uniform
#
#    def priority_post_factum(gifts):
#        def do_accept():
#            nonlocal gift_value
#            if gift_value is None:
#                if idx < len(gifts):
#                    gift_value = gifts[idx]
#                else:
#                    print("Is that a joke - to say 'accept' when"
#                          " gift wasn't taken from the bag?")
#            else:
#                print('Sorry, you made your choice already.')
#
#        def gift_generator():
#            nonlocal idx
#            while idx:
#                idx -= 1
#                yield gifts[idx]
#
#        idx, gift_value = len(gifts), None
#        choose_good_gift(idx, gift_generator, do_accept)
#        if gift_value is None:
#            print('Unfortunately, you did not choose anything.')
#            return len(gifts)
#        else:
#            return sum(gift_value < x for x in gifts)
#
#    def check_solution(bag_count):
#        standings = gift_count = best_gifts = 0
#        for i in range(bag_count):
#            gifts_in_bag = randint(10, 1000)
#            gift_count += gifts_in_bag
#            scale = (random() + random()) ** randint(0, 1024)
#            priority = priority_post_factum([uniform(0., scale) for _ in range(gifts_in_bag)])
#            standings += priority
#            best_gifts += not priority
#        print('You do won {:n} best gifts from {:n} bags with {:,} gifts!\n'
#              'It seems like for bags of {:n} gifts -\n'
#              'you would choose the second best gift, silver ;)'
#              .format(best_gifts, bag_count, gift_count, round(gift_count / standings) + 1))
#
#    check_solution(2000)
