import pandas as pd
import matplotlib.pyplot as mp

p1 = pd.read_csv("player-6607011.csv", usecols = ["player_id", "missed_safe_invitations",
                                                  "accepted_unsafe_invitations", "skill_level_refusal"])
players_list = p1.player_id.unique()
pd.to_numeric(p1["missed_safe_invitations"])
pd.to_numeric(p1["accepted_unsafe_invitations"])
pd.to_numeric(p1["skill_level_refusal"])

p1['accepted_unsafe_invitations'] = p1['accepted_unsafe_invitations'].fillna(0)
p1["missed_safe_invitations"] = p1["missed_safe_invitations"].fillna(0)
p1["skill_level_refusal"] = p1["skill_level_refusal"].fillna(method='ffill')
p1["skill_level_refusal"] = p1["skill_level_refusal"].fillna(method='bfill')

p1["bad_invites"] = p1["accepted_unsafe_invitations"] + p1["missed_safe_invitations"]
p2 = p1.query("bad_invites > 0")

total_bad = 0
total_bad_invites = []
for inv in p2["bad_invites"]:
    total_bad += inv
    total_bad_invites.append(total_bad)
p2["total_bad_invites"] = total_bad_invites
#print(p2.to_string())
df = pd.DataFrame(p2, columns=["total_bad_invites", "skill_level_refusal"])

# plot multiple columns such as population and year from dataframe
df.plot.line(x="total_bad_invites", y="skill_level_refusal")
# display plot
mp.show()

#print(p1.describe())
#for row in p1:
    #for ids in p1.
#print(players_list)
#plotty = plt.plot(p1.loc[:, "event_time_dbl"])
#plotty.show()
#r_frame = p1.corr("pearson")
#print(r_frame.to_string())