# Cricket Simulator
Multi-arm Bandits
The goal of the project is to use multi-armed bandit (MAB) algorithms to come up with
effective batting strategies in the game of cricket. We now describe the rules and game
dynamics. There are 6 actions namely A = {0, 1, 2, 3, 4, 6}. The current ball is denoted by
t, and the MAB algorithm will have to play for t = 1, . . . , T balls, and at ball t needs to
pick an action at ∈ A. At each ball the following happen:
1. A wicket can fall with a probability pout(at).
2. In case there is no wicket, then a run is scored with probability prun(at).
In Problems 1, 2, 3, 4 there is only one batter, and every time the batter gets out, the
same batter plays again.
• Problem 1: Let w(a) = pout(a) be the expected wicket per ball for playing action a. Let
w∗ = arg mina∈A w(a). The goal is to minimise the regret Rn =
Pn
t=1(w(at) − w∗). Hint:
KL-UCB might be useful.
• Problem 2: Let s(a) = (1 − pout(a)) × prun(a) × a be the expected run per ball for
P
playing action a. Let s∗ = arg maxa∈A s(a). The goal is to minimise the regret Rn =
n
t=1(s∗ − s(at)).
• Problem 3: Let ρ(a) = (1−pout(a))×prun(a)×a
pout(a)
be the runs gained per wicket for action a.
Let ρ∗ = arg maxa∈A ρ(a). The goal is to minimise the regret Rn =
Pn
t=1(ρ∗ −ρ(at)). Hint:
• Problem 4: In this problem, there will be a total of m = 1, . . . , M matches. Each match
will consist of t = 1, . . . , 60 balls, and there are 4 wickets, i.e., if 4 wickets fall before 60
balls then the match stops. Let sm be the score in match m. MAB algorithm is supposed
to maximise PM
m=1 sm.
• Problem 5: This is same as Problem 4, with a slight change. There are 4 kinds of
batters, i = 1, . . . , 4. This means we have pout(a, i) and pout(a, i) to be functions of the
batter i. Once a batter gets out, the MAB needs to decide which batter will bat next, and
for the current batter the MAB has to choose at
. Here also the MAB algorithm is supposed
to maximise PM
m=1 sm.
