
import os
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from app.gym_env import SupplyChainEnv

def train(output_model_path="/app/models/ppo_supplychain.zip", total_timesteps=10000):
    env = DummyVecEnv([lambda: SupplyChainEnv(days=30)])
    model = PPO('MlpPolicy', env, verbose=1)
    model.learn(total_timesteps=total_timesteps)
    os.makedirs(os.path.dirname(output_model_path), exist_ok=True)
    model.save(output_model_path)
    return output_model_path

if __name__ == "__main__":
    print("Training PPO (this may take some time)...")
    path = train(total_timesteps=20000)
    print("Saved model to", path)
