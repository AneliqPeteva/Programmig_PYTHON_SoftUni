from math import floor
name_serial = input()
count_season = int(input())
count_episodes = int(input())
duration_episode_without_ads = float(input())

#logic
duration_episode_with_ads = duration_episode_without_ads + (duration_episode_without_ads * 0.20)
time_special_episodes = count_season * 10

all_time = floor(duration_episode_with_ads * count_episodes * count_season + time_special_episodes)

print(f"Total time needed to watch the {name_serial} series is {all_time} minutes.")