#ライフゲームという隣の状態によって格子の形を変えるゲームを実装していく

import time
from IPython.display import clear_output
from ipythonblocks import BlockGrid, ImageGrid, Color, colors
import random

#周囲のセルに幾つ命が生きているかを数える関数
def count_neighbor(cell,i,j):
  n=0
  for k in range(3):
    for l in range(3):
      if i+k-1 >= 0 and i+k-1 < 4 and j+l-1 >= 0 and j+l-1 < 5:
        n = n+cell[i+k-1][j+l-1]
  
  n = n - cell[i][j]
  return n

#各セルの次の世代の状態を返す関数
def lifegame_rule(cur,neighbor):
  n=0
  if cur == 0:
    if neighbor == 3:
      n=1
  
  else:
    if neighbor == 2 or neighbor == 3:
      n=1
    else:
      n=0
  return n

#ライフゲームのルールに従い、世代を１つ進める関数
def lifegame_step(cell):
  cells=[]
  for i in range(4):
    cell_content=[]
    for j in range(5):
      neighbor=count_neighbor(cell, i,j)
      cur=cell[i][j]
      n=lifegame_rule(cur,neighbor)
      cell_content.append(n)
    cells.append(cell_content)
          
  return cells        

#ルールに従い、2次元配列をprintしながら世代を進める関数
def lifegame_print(cell,steps):
  c1=cell
  print(0,c1)
  for i in range(steps):
    c=lifegame_step(c1)
    c1=c
    print(i+1,c)

#2次元配列を白黒で格子を表示する関数
def cell_show(cell, bsize):
  alive = Color(0, 0, 0)
  dead = Color(240, 240, 240)
  height = len(cell)
  width = len(cell[0])
  grid = BlockGrid(width, height, block_size=bsize)
  for i in range(height):
    for j in range(width):
      if(cell[i][j] == 1):
        grid[i, j] = alive
      else:
        grid[i, j] = dead
  grid.show_image()

#アニメーションで格子を表示しながら世代を進める関数
def lifegame_animation(cell,steps,bside,t):
  c0=cell
  cell_show(cell,bside)
  time.sleep(t)
  clear_output()
  for i in range(steps):
    c=lifegame_step(c0)
    time.sleep(t)
    cell_show(c,bside)
    time.sleep(t)
    clear_output()
    c0=c

#ランダムな数、セルを生成する関数
def make_random_cell(width,height):
  cells=[]
  for i in range(height):
    cell=[]
    for j in range(width):
      cell.append(random.randint(0,1))
    cells.append(cell)
  return cells

rand_cell1 = make_random_cell(10,5)
lifegame_animation(rand_cell1, 10, 30, 1)