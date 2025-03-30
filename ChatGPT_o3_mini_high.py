import random

def chain_of_fools(task: str, iterations: int = 5):
    """
    Simulate the Chain-of-Fools AI method.
    
    This function takes a task (a string describing the problem) and performs several
    iterative "chain-of-thought" steps. In each iteration, the algorithm either
    refines the current idea or injects a random, "foolish" twist to encourage creative,
    unorthodox solutions.
    
    Parameters:
        task (str): The initial task or prompt.
        iterations (int): Number of processing steps.
    
    Returns:
        steps (list): A list of strings representing each chain-of-thought step.
        final_result (str): The final output after all iterations.
    """
    steps = [f"Initial task: {task}"]
    current = task
    
    # Define a list of playful, "foolish" modifiers to inject creative missteps.
    foolish_modifiers = [
        " adding a dash of absurdity",
        " miscalculating with whimsy",
        " inviting a random twist",
        " consulting imaginary experts",
        " defying conventional logic"
    ]
    
    for i in range(1, iterations + 1):
        # Decide randomly whether to refine or to inject a foolish twist
        if random.random() < 0.6:
            # Normal refinement step
            current = current + " → refined"
            step_description = f"Step {i}: refined the idea."
        else:
            # Inject a foolish twist
            twist = random.choice(foolish_modifiers)
            current = current + twist
            step_description = f"Step {i}: {twist.strip()}."
        
        steps.append(step_description)
    
    final_result = f"Final output: {current}"
    return steps, final_result

if __name__ == "__main__":
    user_task = input("Enter a task for the Chain-of-Fools AI: ")
    chain_steps, output = chain_of_fools(user_task, iterations=7)
    
    print("\nChain-of-Fools chain-of-thought steps:")
    for step in chain_steps:
        print(step)
    
    print("\n" + output)
