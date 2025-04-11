# from typing import Dict, List, Tuple, Optional, Any
# from .Agent import Agent
# from .Checkpoint import CheckpointManager


# class Environment:
#     """
#     A class representing an environment where agents can interact with each other.
    
#     The Environment class serves as a container and manager for multiple agents,
#     providing functionality to:
#     - Add and remove agents from the environment
#     - Track all agents present in the environment
#     - Facilitate interactions between agents
#     - Maintain a record of agent relationships and activities
    
#     This class is the main entry point for creating and managing multi-agent
#     simulations or interactive scenarios.
    
#     Attributes:
#         name (str): The name of the environment, used for identification
#         agents (Dict[str, Agent]): A dictionary mapping agent IDs to Agent instances
#     """

#     def __init__(self, name: str = "Default Environment"):
#         """
#         Initialize a new environment.
        
#         Creates a new environment instance with the specified name and initializes
#         an empty collection of agents.
        
#         Args:
#             name (str, optional): Name of the environment. Defaults to "Default Environment".
#         """
#         self.name = name
#         self.agents: Dict[str, Agent] = {}

#     def add_agent(self, agent: Agent) -> None:
#         """
#         Add an agent to the environment.
        
#         Registers a new agent in the environment, making it available for
#         interactions with other agents. The agent is stored using its unique
#         agent_id as the key.
        
#         Args:
#             agent (Agent): The agent instance to add to the environment.
#         """
#         self.agents[agent.agent_id] = agent

#     def remove_agent(self, agent_id: str) -> None:
#         """
#         Remove an agent from the environment.
        
#         Removes the specified agent from the environment if it exists.
#         This will prevent the agent from participating in future interactions
#         within this environment.
        
#         Args:
#             agent_id (str): The unique identifier of the agent to remove.
#         """
#         if agent_id in self.agents:
#             del self.agents[agent_id]

#     def get_agent(self, agent_id: str) -> Agent:
#         """
#         Retrieve an agent from the environment by their ID.
        
#         Args:
#             agent_id (str): The unique identifier of the agent to retrieve.
            
#         Returns:
#             Agent: The requested agent instance if found, None otherwise.
#         """
#         return self.agents.get(agent_id)

#     def list_agents(self) -> List[str]:
#         """
#         Get a list of all agent IDs currently in the environment.
        
#         This method provides a way to enumerate all agents currently
#         registered in the environment.
        
#         Returns:
#             List[str]: A list containing the unique identifiers of all registered agents.
#         """
#         return list(self.agents.keys())

#     def record_interaction(self, sender_id: str, receiver_id: str, message: str) -> None:
#         """
#         Record an interaction between two agents in the environment.
        
#         This method delegates the interaction recording to both the sender and
#         receiver agents, ensuring that both parties maintain a record of their
#         communication.
        
#         Args:
#             sender_id (str): The unique identifier of the agent initiating the interaction.
#             receiver_id (str): The unique identifier of the agent receiving the interaction.
#             message (str): The content of the interaction.
            
#         Raises:
#             ValueError: If either the sender or receiver agent is not found in the environment.
#         """
#         sender = self.get_agent(sender_id)
#         receiver = self.get_agent(receiver_id)

#         if not sender or not receiver:
#             raise ValueError(f"Agent {sender_id} or {receiver_id} not found in the environment")

#         sender.record_interaction(sender_id, receiver_id, message)
#         receiver.record_interaction(sender_id, receiver_id, message)

#     def save_checkpoint(self, name: Optional[str] = None) -> str:
#         """
#         Save the current state of the environment to a checkpoint.
        
#         Args:
#             name (str, optional): Custom name for the checkpoint
            
#         Returns:
#             str: Path to the saved checkpoint
#         """
#         checkpoint = CheckpointManager()
#         return checkpoint.save(self, name)
    
#     def load_checkpoint(self, checkpoint_path: str) -> None:
#         """
#         Load the environment state from a checkpoint.
        
#         Args:
#             checkpoint_path (str): Path to the checkpoint directory
#         """
#         checkpoint = CheckpointManager()
#         loaded_env = checkpoint.load(checkpoint_path)
#         self.name = loaded_env.name
#         self.agents = loaded_env.agents
    
#     @staticmethod
#     def list_checkpoints() -> Dict[str, Any]:
#         """
#         List all available checkpoints.
        
#         Returns:
#             Dict[str, Any]: Dictionary of checkpoint names and their metadata
#         """
#         checkpoint = CheckpointManager()
#         return checkpoint.list_checkpoints()

#     def __str__(self) -> str:
#         """
#         Get a string representation of the environment.
        
#         Provides a human-readable description of the environment, including
#         its name and the number of agents it contains.
        
#         Returns:
#             str: A formatted string describing the environment.
#         """
#         return f"Environment: {self.name}\nAgents: {len(self.agents)}"