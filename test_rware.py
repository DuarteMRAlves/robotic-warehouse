import gym
import rware
import time 
env = gym.make("rware-tiny-2ag-v1")

print(env.n_agents)  # 2
print(env.action_space)  # Tuple(Discrete(5), Discrete(5))
print(env.observation_space)  # Tuple(Box(XX,), Box(XX,))

obs = env.reset()  # a tuple of observations

num_steps = 100

for _ in range(num_steps):
    actions = env.action_space.sample()  # the action space can be sampled

    n_obs, reward, done, info = env.step(actions)
    print(n_obs)
    env.render()
    input()

    time.sleep(1)

env.close()