#!/usr/bin/env python

from random import randint

import sys

if len(sys.argv) != 3:
    raise ValueError("Usage: python3 parks.py players round")

players = int(sys.argv[1])
round = int(sys.argv[2]) - 1 # for laymen


def generate_trail_length(round=0, players=3):
   special_token_lim = 4 - round
   special_token = randint(1, special_token_lim)
   print(f"Welcome to parks season {round + 1}!")
   print(f"Pick special token {special_token} of {special_token_lim}")

   if round == 0:
      print(f"Player {randint(1, players)} goes first.")
      if players > 3:
         print(f"Go {'clockwise' if randint(1,2) == 1 else 'counterclockwise'}.")

   if players > 3:
      round += 1
   tokens_to_take = []
   for i in range(0, 6 + round):
      token_to_take = randint(0, i) + 1
      tokens_to_take.append(token_to_take)
   print(f"Token order: {' - '.join(str(x) for x in reversed(tokens_to_take))}")
generate_trail_length(round=round, players=players)
