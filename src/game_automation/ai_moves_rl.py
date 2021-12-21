#!/usr/bin/env python
import pandas as pd
import tensorflow as tf

from tf_agents.agents.dqn import dqn_agent
from tf_agents.drivers import dynamic_step_driver
from tf_agents.environments import tf_py_environment
from tf_agents.networks import q_network
from tf_agents.replay_buffers import tf_uniform_replay_buffer

from game import rl_environment


# Create environment
env = rl_environment.Game2048Env()
tf_env = tf_py_environment.TFPyEnvironment(env)

# Create agent
q_net = q_network.QNetwork(
    tf_env.time_step_spec().observation,
    tf_env.action_spec(),
    fc_layer_params=(100,)
)

agent = dqn_agent.DqnAgent(
    tf_env.time_step_spec(),
    tf_env.action_spec(),
    q_network=q_net,
    optimizer=tf.compat.v1.train.AdamOptimizer(0.000001)
)

# Create replay buffer
replay_buffer_capacity = 1000
replay_buffer = tf_uniform_replay_buffer.TFUniformReplayBuffer(
    agent.collect_data_spec,
    batch_size=tf_env.batch_size,
    max_length=replay_buffer_capacity)

# Add an observer that adds to the replay buffer:
replay_observer = [replay_buffer.add_batch]

collect_steps_per_iteration = 10
collect_op = dynamic_step_driver.DynamicStepDriver(
  tf_env,
  agent.collect_policy,
  observers=replay_observer,
  num_steps=collect_steps_per_iteration).run()


dataset = replay_buffer.as_dataset(
    sample_batch_size=4,
    num_steps=2)

iterator = iter(dataset)

# Training
num_train_steps = 100
ts = pd.Timestamp.now().strftime('%Y%m%d-%H%M%S')
for i in range(num_train_steps):
    trajectories, _ = next(iterator)
    loss = agent.train(experience=trajectories)
    with open(f'../data/results/ai_moves/results_loss_{ts}.csv', 'a') as f:
        f.write(f'{float(loss[0])}\n')
    if i % 25 == 0:
        print(float(loss[0]))
