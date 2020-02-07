from random import shuffle
import random
import numpy as np

from sys import exit

# 初始化扑克
playing_cards = {
    '♦10':10, '♦2':2, '♦3':3, '♦4':4, '♦5':5, '♦6':6, '♦7':7, '♦8':8, '♦9':9, '♦A':1, '♦J':10, '♦K':10, '♦Q':10,
    '♣10':10, '♣2':2, '♣3':3, '♣4':4, '♣5':5, '♣6':6, '♣7':7, '♣8':8, '♣9':9, '♣A':1, '♣J':10, '♣K':10, '♣Q':10,
    '♥10':10, '♥2':2, '♥3':3, '♥4':4, '♥5':5, '♥6':6, '♥7':7, '♥8':8, '♥9':9, '♥A':1, '♥J':10, '♥K':10, '♥Q':10,
    '♠10':10, '♠2':2, '♠3':3, '♠4':4, '♠5':5, '♠6':6, '♠7':7, '♠8':8, '♠9':9, '♠A':1, '♠J':10, '♠K':10, '♠Q':10
}

poker_name = list(playing_cards.keys())
# 扑克的数量，几副扑克
poker_count = 1
poker_list = poker_name * poker_count

# 用于判断手中的牌是否有A，根据分数来进行确定A的分值是0还是1
four_a = ['♦A','♣A','♥A','♠A']

# 计分器，玩家-电脑，初始分数都是零
total_score = np.array([0,0])

# 记录游戏是第几个回合
game_round = 1

'''
洗牌：重新对扑克牌进行随机排列
'''
def random_card(poker_name_list):
    shuffle(poker_name_list)
    
'''
计算手里的牌的分数，传进来的参数是一个列表
'''
def score_count(hand_pocker):
    # 声明一个变量，用这个变量来记录牌的总分数
    poker_score = 0
    # 标记：判断是否有A的标记，默认没有
    have_a = False
    
    # 计算手中牌的分数
    for k in hand_pocker:
        poker_score += playing_cards[k]
        
    # 判断手中的牌是否有A，然后再根据A的规则进行分数计算
    for i in hand_pocker:
        if i in four_a:
            have_a = True
            break
        else:
            continue
            
    if have_a == True
        if 
