
import gym
from gym import spaces
import numpy as np
from .simulation_engine import run_supply_chain_sim

class SupplyChainEnv(gym.Env):
    # Simple Gym wrapper around the SimPy supply chain simulator.
    # Action: [shipment_boost (continuous 0-0.5), reorder (0-200)]
    # Observation: [inventory, demand, lead_time, shipments]
    # Reward: mean service level over simulation horizon
    metadata = {'render.modes': ['human']}
    def __init__(self, days=30, initial_state=None):
        super().__init__()
        self.days = days
        self.initial_state = initial_state or {'inventory':200}
        self.action_space = spaces.Box(low=np.array([0.0, 0.0]), high=np.array([0.5, 200.0]), dtype=np.float32)
        self.observation_space = spaces.Box(low=-1e6, high=1e6, shape=(4,), dtype=np.float32)
        self.current_step = 0
        self.state = None

    def reset(self):
        self.current_step = 0
        self.state = dict(self.initial_state)
        obs = np.array([self.state.get('inventory',0), 0.0, self.state.get('lead_time',5), 0.0], dtype=np.float32)
        return obs

    def step(self, action):
        shipment_boost = float(np.clip(action[0], 0.0, 0.5))
        reorder = float(np.clip(action[1], 0.0, 200.0))
        policy = {'shipment_boost': shipment_boost, 'reorder': int(round(reorder))}
        history = run_supply_chain_sim(self.initial_state.copy(), policy, days=self.days)
        outcomes = [h['outcome'] for h in history]
        reward = float(np.mean(outcomes))
        last = history[-1]
        obs = np.array([last.get('inventory',0), last.get('demand',0), last.get('lead_time',5), last.get('shipments',0)], dtype=np.float32)
        self.state = last
        self.current_step = self.days
        done = True
        info = {'history': history}
        return obs, reward, done, info

    def render(self, mode='human'):
        print(f"Step {self.current_step}, State: {self.state}")
