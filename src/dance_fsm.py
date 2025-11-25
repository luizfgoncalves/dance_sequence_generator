"""
Dance Finite State Machine (FSM) implementation.
This module uses the state, step, and transition modules to create a complete FSM.
"""

from src.transition import get_next_state, get_valid_transitions, TRANSITIONS
from src.state import ALL_STATES, DANCA_FECHADA_ESQUERDA_LIVRE, DanceState
from src.step import ALL_STEPS

class DanceFSM:
    """Finite State Machine for dance sequence generation."""
    
    def __init__(self, state=DANCA_FECHADA_ESQUERDA_LIVRE):
        """
        Initialize the FSM with a starting state.
        
        Args:
            state: Initial state name or DanceState object (default: "DANCA_FECHADA_ESQUERDA_LIVRE")
        """
        if isinstance(state, str):
            if state not in ALL_STATES:
                raise ValueError(f"Invalid initial state: '{state}'")
            self.state = ALL_STATES[state]
        elif isinstance(state, DanceState):
            self.state = state
        else:
            raise ValueError(f"Invalid state type: {type(state)}")
    
    def get_current_state(self):
        """
        Get current state.
        
        Returns:
            Current state object
        """
        return self.state
    
    def get_all_state_set(self):
        """
        Get all available states in the FSM.
        
        Returns:
            List of all state names
        """
        return list(ALL_STATES.keys())
    
    def get_valid_step_set(self):
        """
        Get all valid steps from the current transition mapping.
        
        Returns:
            List of valid step names
        """
        transition_map = get_valid_transitions(self.state)
        return [step.name for step, next_state in transition_map.items()]  
    
    def get_all_step_set(self):
        """
        Get all available steps for each state in the FSM.
        
        Returns:
            Dictionary mapping state names to lists of valid step names
        """
        all_transitions = self.get_all_transition_set()
        state_steps_mapping = {}
        for state, transitions in all_transitions.items():
            for step, _ in transitions.items():
                state_steps_mapping.setdefault(state.name, []).append((step.name, step.description))
        return state_steps_mapping

    def transition(self, step):
        """
        Perform a state transition based on a step.
        
        Args:
            step: Name of the step to perform (string) or DanceStep object
            
        Returns:
            The new state object after the transition
            
        Raises:
            ValueError: If the step is invalid for the current state
        """
        # Convert step to obj if it's an string
        if isinstance(step, str):
            if step not in ALL_STEPS:
                raise ValueError(f"Invalid step: '{step}'")
            step = ALL_STEPS[step]
        
        # Get next state
        next_state = get_next_state(self.state, step)
        
        # Update state to the object
        self.state = next_state
        return self.state
    
    def get_all_transition_set(self):
        """
        Get all transitions in the FSM.
        
        Returns:
            Complete transition dictionary with string names for backward compatibility
        """
        return TRANSITIONS