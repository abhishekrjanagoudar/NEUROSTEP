FROM nvcr.io/nvidia/isaac-sim:4.5.0

SHELL ["/bin/bash", "-lc"]
WORKDIR /workspace

# System deps for Isaac Lab + RL workflows
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

# Clone Isaac Lab (contains stock Isaac-Ant-v0 training entrypoints)
RUN git clone https://github.com/isaac-sim/IsaacLab.git

WORKDIR /workspace/IsaacLab
RUN ./isaaclab.sh --install

# Install RL dependency used by Isaac Lab wrappers
RUN ./isaaclab.sh -p -m pip install rsl-rl-lib

WORKDIR /workspace/NEUROSTEP
COPY . /workspace/NEUROSTEP

CMD ["python", "scripts/train.py", "--task", "Isaac-Ant-v0", "--headless", "--num_envs", "4096"]
