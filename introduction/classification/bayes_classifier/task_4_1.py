import math

emails = [('SPAM', 19), ('HAM', 23)]
words = [('SPAM', 121), ('HAM', 86)]

online = [('SPAM', 7), ('HAM', 6)]
million = [('SPAM', 6), ('HAM', 5)]
bonus = [('SPAM', 4), ('HAM', 0)]
money = [('SPAM', 4), ('HAM', 3)]
unlimited = [('SPAM', 12), ('HAM', 5)]
offer = [('SPAM', 1), ('HAM', 9)]
purchase = [('SPAM', 25), ('HAM', 8)]
gift = [('SPAM', 1), ('HAM', 10)]
bill = [('SPAM', 52), ('HAM', 34)]
cash = [('SPAM', 9), ('HAM', 6)]

p_spam = emails[0][1] / (emails[0][1] + emails[1][1])
ln_p_spam = math.log(p_spam)

p_ham = emails[1][1] / (emails[0][1] + emails[1][1])
ln_p_ham = math.log(p_ham)

# Cash Million Remove Membership Offer Money Bill


w_cash_spam = cash[0][1] + 1
w_million_spam = million[0][1] + 1
w_remove_spam = 1
w_membership_spam = 1
w_offer_spam = offer[0][1] + 1
w_money_spam = money[0][1] + 1
w_bill_spam = bill[0][1] + 1

w_cash_ham = cash[1][1] + 1
w_million_ham = million[1][1] + 1
w_remove_ham = 1
w_membership_ham = 1
w_offer_ham = offer[1][1] + 1
w_money_ham = money[1][1] + 1
w_bill_ham = bill[1][1] + 1

w_spam = 10 + 121

w_ham = 10 + 86

y_spam = math.log(p_spam) \
         + math.log(w_cash_spam / w_spam) \
         + math.log(w_million_spam / w_spam) \
         + math.log(w_remove_spam / w_spam) \
         + math.log(w_membership_spam / w_spam) \
         + math.log(w_offer_spam / w_spam) \
         + math.log(w_money_spam / w_spam) \
         + math.log(w_bill_spam / w_spam)

y_ham = math.log(p_ham) \
         + math.log(w_cash_ham / w_ham) \
         + math.log(w_million_ham / w_ham) \
         + math.log(w_remove_ham / w_ham) \
         + math.log(w_membership_ham / w_ham) \
         + math.log(w_offer_ham / w_ham) \
         + math.log(w_money_ham / w_ham) \
         + math.log(w_bill_ham / w_ham)

p_letter_spam = 1 / (1 + math.exp(y_ham-y_spam))

print(p_spam)
print(y_spam)
print(y_ham)
print(p_letter_spam)
