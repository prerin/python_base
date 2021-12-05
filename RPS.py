#ジャンケンの実装
#今回は自分で好きな手（数字）を入力して、ランダムな手をコンピュータが考えて勝負するというものを実装していく
import random

#自分の手の入力結果を出力する
def read_hand():
  while True:
    hand = input('あなたの手は？（ぐ＝0, ちょき=1, ぱー=2) :')
      if hand == '0' or hand == '1' or hand == '2':
        return int(hand)
        break
      else:
        print('0,1,2のいずれかを入力してください')

#ジャンケンの勝敗を判定する
#ここでユーザの勝ちには１、引き分けは０、負けには-1を返す
def judge(player, computer):
  if player < computer:
    return 1
  elif player ==computer:
    return 0
  else:
    return -1

#最終的なジャンケンプログラムのコード
def hand(player):
  if player == 0:
    return 'ぐー'
  elif player == 1:
    return  'ちょき'
  else:
    return 'ぱー'
    
def insult(match):
  if match == -1:
    return 'You win!'
  elif match == 0:
    return 'its a draw'
  else:
    return 'I win'
    
    
def janken_game():
  point_me=0
  point_you=0
  print('あなたの現在の勝ち点は{}です。'.format(point_you))
  print('あなたの現在の勝ち点は{}です。'.format(point_me))
  for i in range(9):
      print('第{}試合'.format(i+1))
    computer=random.randint(0,2)
    player=read_hand()
    match=judge(player,computer)
    if  match == 1:
      point_me +=3
      point_you+=1
    elif match == -1:
      point_you +=3
      point_me+=1
    else:
      point_me+=1
      point_you+=1
    print('あなた:{}'.format(hand(player)))
    print('コンピュータ:{}'.format(hand(computer)))
    print(insult(match))
    print('あなたの現在の勝ち点は{}です。'.format(point_you))
    print('私の現在の勝ち点は{}です。'.format(point_me))
  print('第10試合')
  computer=random.randint(0,2)
  player=read_hand()        
  match=judge(player,computer)
  if  match == 1:
    point_me +=3
    point_you+=1
  elif match == -1:
    point_you +=3
    point_me+=1
  else:
    point_me+=1
    point_you+=1
  print('あなた:{}'.format(hand(player)))
  print('コンピュータ:{}'.format(hand(computer)))
  print(insult(match))
  
  print('ゲーム終了')
  print('あなたの最終的な勝ち点は{}です。'.format(point_you))
  print('私の最終的な勝ち点は{}です。'.format(point_me))
  final_match=judge(point_you,point_me)
  print(insult(final_match))

janken_game()

#授業の内容に沿っての実装なため、出力結果を合わすためのコードとなっている